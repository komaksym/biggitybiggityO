import scrapy
from scrapy import Request
from scrapy.http.response import Response
from typing import Generator, List, Match
import json
import re
from ..items import ScraperItem


class NeetcodeSpider(scrapy.Spider):
    """Spider for scraping coding problems and solutions from Neetcode.io."""

    name = "neetcode"

    def start_requests(self) -> Generator[Request, None, None]:
        """Initialize the spider with the starting URL.

        Returns:
            Generator yielding the initial request with playwright enabled.
        """
        url = "https://neetcode.io/practice?tab=neetcode150"
        yield Request(url, self.parse_problem_names, meta={"playwright": True})

    def parse_problem_names(self, response: Response) -> Generator[Request, None, None]:
        """Extract problem names from the response and initiate solution parsing.

        Args:
            response: Response object containing the webpage data.

        Returns:
            Generator yielding requests for each problem's solutions.
        """
        problem_names = response.xpath(
            "//a[contains(@class, 'table-text text-color ng-star-inserted')]/@href"
        ).getall()

        # Stripping the excess part to have a needed format in problem name
        clean_problem_names = [link.replace("/problems/", "") for link in problem_names]

        # Send names to solution parser
        for problem_name in clean_problem_names:
            yield from self.parse_solutions([problem_name])

    def parse_solutions(
        self, problem_names: List[str]
    ) -> Generator[Request, None, None]:
        """Generate requests for fetching solution metadata for each problem.

        Args:
            problem_names: List of problem identifiers to fetch solutions for.

        Returns:
            Generator yielding POST requests for solution metadata.
        """
        url = "https://us-central1-neetcode-dd170.cloudfunctions.net/getProblemMetadataFunction"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://neetcode.io/",
            "Authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjBhYmQzYTQzMTc4YzE0MjlkNWE0NDBiYWUzNzM1NDRjMDlmNGUzODciLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTWFrc3ltIEtvdmFsIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0l0dG9BWUVROUxsVmhyaFhITzQwX0FxQkd4R0VPbzFpVG1mSUlPMjV6NlFiMlJpczA9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbmVldGNvZGUtZGQxNzAiLCJhdWQiOiJuZWV0Y29kZS1kZDE3MCIsImF1dGhfdGltZSI6MTczNDk3NjE2MSwidXNlcl9pZCI6ImZsMmtVaXBKNExWSU5hQ25hWnpKRzV6cW5IUzIiLCJzdWIiOiJmbDJrVWlwSjRMVklOYUNuYVp6Sk…ZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTA3MzMxNTY4MDg2NTU2NDczODkxIl0sImVtYWlsIjpbImtvdmFsbWFrc3ltMkBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.KT4IK021Qj3ZhPOoJDz9wKhsb_ghi3ip7KdWIW5QowdElh92GoGu4ZbdXzPccsD3ldTghN6YfAURY5ZLDosRWCh3h6x2pA-zVyUzxM6MWXIOqvQedtYzaNxlCYvbci6Y_4NOKnlFh3q7kr91YjZfP5WtCrYGTCYkAVPvuVscQAw1q5NAHCpOKxYBHI0EmFAX-9NnMQIzeHN7sz7FzvIyHtCRfKYX-i-zYOXSNVlIY7Px3CL26nJZUx4t3KYXJnThqHIlXkldZJ3mMCO6VpvXY4jBeqWFaDgC3NcVGIahYrYl-fWrbk4xOufReFxwXLVp54UNZlmdLsP5un7y3AW3XA",
            "Content-Type": "application/json",
            "Origin": "https://neetcode.io",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "DNT": "1",
            "Sec-GPC": "1",
            "Priority": "u=4",
            "TE": "trailers",
        }

        # Parse every single problem solution
        for problem_name in problem_names:
            body = json.dumps({"data": {"problemId": problem_name}})
            yield Request(
                url=url,
                callback=self.parse_response,
                method="POST",
                dont_filter=True,
                headers=headers,
                body=body,
            )

    def regex_find_code(self, json_load: str) -> List[Match[str]]:
        """Extract Python code blocks from the solution text.

        Args:
            json_load: JSON string containing the solution article body.

        Returns:
            List of regex match objects containing Python code blocks.
        """
        pattern = r"(?<=python\n)(.*\n)*?(?=`{3})"
        python_code = re.finditer(pattern, json_load)
        return list(python_code)

    def regex_find_complexity(self, json_load: str) -> List[str]:
        """Extract time complexity annotations from the solution text.

        Args:
            json_load: JSON string containing the solution article body.

        Returns:
            List of time complexity strings.
        """
        pattern = r"(?<=Time complexity: \$)O.+(?=\$)"
        time_complexity = re.findall(pattern, json_load)
        return time_complexity

    def populate_items(
        self, code: List[Match[str]], complexities: List[str]
    ) -> Generator[ScraperItem, None, None]:
        """Create ScraperItems from matched code and complexity pairs.

        Args:
            code: List of regex matches containing code blocks.
            complexities: List of corresponding time complexities.

        Returns:
            Generator yielding ScraperItems with populated fields.
        """
        item = ScraperItem()

        # Populating items
        for i, sample in enumerate(code):
            item["code"] = sample.group()
            item["time_complexity"] = complexities[i]
            yield item

    def check_total_parsed(
        self, code: List[Match[str]], complexities: List[str]
    ) -> None:
        """Verify that the number of code blocks matches the number of complexities.

        Args:
            code: List of regex matches containing code blocks.
            complexities: List of corresponding time complexities.

        Raises:
            AssertionError: If the lengths of code and complexities lists don't match.
        """
        assert len(code) == len(complexities), (
            "The length of codes does not equal to the length of time complexities."
            "Expected: len(code) == len(complexities)."
            f"Got: len(code) = {len(code)}, len(complexities) = {len(complexities)}."
        )

    def parse_response(self, response: Response) -> Generator[ScraperItem, None, None]:
        """Parse the solution metadata response and extract code and complexity information.

        Args:
            response: Response object containing the solution metadata.

        Returns:
            Generator yielding ScraperItems containing solution data.
        """
        solutions_json = json.loads(response.text)["result"]["article_body"]

        # Regex parsing the data
        code = self.regex_find_code(solutions_json)
        complexities = self.regex_find_complexity(solutions_json)

        # Checking if regex didn't miss anything and all the code has the corresponding time complexity
        self.check_total_parsed(code, complexities)

        # Consuming the generator returned by populate item
        for item in self.populate_items(code, complexities):
            yield item
