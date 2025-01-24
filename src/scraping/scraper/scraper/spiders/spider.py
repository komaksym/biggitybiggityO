import scrapy
from scrapy import Request
import json
import re
from ..items import ScraperItem
import pdb


class NeetcodeSpider(scrapy.Spider):
    name = "neetcode"

    def start_requests(self):
        url = "https://neetcode.io/practice?tab=neetcode150"
        yield Request(url, self.parse_problem_names, meta={"playwright": True})

    def parse_problem_names(self, response):
        problem_names = response.xpath(
            "//a[contains(@class, 'table-text text-color ng-star-inserted')]/@href"
        ).getall()

        # Stripping the excess part to have a needed format
        clean_problem_names = [link.replace("/problems/", "") for link in problem_names]

        for name in clean_problem_names:
            yield from self.parse_solution([name])

    def parse_solution(self, problem_names):
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

        #        body = '{"data":{"problemId":"duplicate-integer"}}'
        #        yield Request(
        #            url=url,
        #            callback=self.parse_response,
        #            method="POST",
        #            dont_filter=True,
        #            headers=headers,
        #            body=body,
        #        )

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

    def regex_find_code(self, json_load):
        pattern = r"(?<=python\n)(.*\n)*?(?=`{3})"
        python_code = re.finditer(pattern, json_load)
        return list(python_code)

    def regex_find_complexity(self, json_load):
        pattern = r"(?<=Time complexity: \$)O.+(?=\$)"
        time_complexity = re.findall(pattern, json_load)
        return time_complexity

    def populate_items(self, code, complexities):
        item = ScraperItem()

        for i, sample in enumerate(code):
            item["code"] = sample.group()
            item["time_complexity"] = complexities[i]
            yield item

    def check_total_parsed(self, code, complexities):
        assert len(code) == len(complexities), (
            "The length of codes does not equal to the length of time complexities."
            "Expected: len(code) == len(complexities)."
            f"Got: len(code) = {len(code)}, len(complexities) = {len(complexities)}."
        )

    def parse_response(self, response):
        #        pdb.set_trace()
        solutions_json = json.loads(response.text)["result"]["article_body"]

        # Regex parsing the data
        code = self.regex_find_code(solutions_json)
        complexities = self.regex_find_complexity(solutions_json)

        # Checking if regex didn't miss anything and all the code has the corresponding time complexity
        self.check_total_parsed(code, complexities)

        # Consuming the generator returned by populate item
        for item in self.populate_items(code, complexities):
            yield item
