import scrapy
from scrapy import Request
import json
import re
from ..items import ScraperItem


class NeetcodeSpider(scrapy.Spider):
    name = "neetcode"

    def start_requests(self):
        url = "https://us-central1-neetcode-dd170.cloudfunctions.net/getProblemMetadataFunction"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://neetcode.io/",
            "Authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgxYjUyMjFlN2E1ZGUwZTVhZjQ5N2UzNzVhNzRiMDZkODJiYTc4OGIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTWFrc3ltIEtvdmFsIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0l0dG9BWUVROUxsVmhyaFhITzQwX0FxQkd4R0VPbzFpVG1mSUlPMjV6NlFiMlJpczA9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbmVldGNvZGUtZGQxNzAiLCJhdWQiOiJuZWV0Y29kZS1kZDE3MCIsImF1dGhfdGltZSI6MTczNDk3NjE2MSwidXNlcl9pZCI6ImZsMmtVaXBKNExWSU5hQ25hWnpKRzV6cW5IUzIiLCJzdWIiOiJmbDJrVWlwSjRMVklOYUNuYVp6Sk…ZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTA3MzMxNTY4MDg2NTU2NDczODkxIl0sImVtYWlsIjpbImtvdmFsbWFrc3ltMkBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.KHDOkbmzBpBmehUmbo8o09EchKauV-ZoVYL5pWlpcksrPpo4w_GL-7rjl1x0e2X4CMSkVHJTU9vR4HBEzk0KW2LVLAkgp9yIfCW3M2w0ZvhC0LPQWRWwkze_CcODThKHn7ECGaZ5Or9H1fUGdqST4AgsWRiWcpkKjZaA7U9wellQj2gjMXtUPxlxdGKj44Nl7-smEmfPhoTscgS7Nq_qO2GB8ZxtYA6Tsk4TT4wUbNazvh_7EgKtvG-Ec7KpgTfpiQdKwmRnHWCFWMtHVfcDf0LWYx0yaUaFYHOPFzVNGvrvbqxL9MxdWlSt1QTLUubMeFH7JOhF_9byCrRaoSIcIA",
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

        body = '{"data":{"problemId":"valid-sudoku"}}'

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
        solutions_json = json.loads(response.text)["result"]["article_body"]

        # Regex parsing the data
        code = self.regex_find_code(solutions_json)
        complexities = self.regex_find_complexity(solutions_json)

        # Checking if regex didn't miss anything and all the code has the corresponding time complexity
        self.check_total_parsed(code, complexities)

        # Consuming the generator returned by populate item
        for item in self.populate_items(code, complexities):
            yield item
