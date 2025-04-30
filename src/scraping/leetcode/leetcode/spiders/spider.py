import scrapy
from ..items import LeetcodeItem


class LeetcodeSpider(scrapy.Spider):
    name = "leetcode"
    language_to_scrape = "Python"

    allowed_domains = ["walkccc.me"]
    #start_urls = ["https://walkccc.me/LeetCode/problems/3/"]
    start_urls = ["https://walkccc.me/LeetCode/problems/1/"]

    def parse(self, response):
        # Parse time complexity label
        complexity_labels = response.xpath("//ul[@class='task-list']/li[1]/text()").getall()

        # Remove empty strings (save only if after stripping a string, the string is still non NaN)
        complexity_labels = [label for label in complexity_labels if label.strip()]

        # Parse python tabbed code
        # (choose the language the solution should be displayed in)
        ## Parse solution language labels
        anchors = response.css("div.tabbed-labels > label::text").getall()

        ## Parse the positions of python code anchor boxes
        idxs = [idx for idx, anchor in enumerate(anchors) if anchor == "Python"]

        ### Keep parsing only if there's Python code box available
        if idxs:
            # Parse the code boxes
            code_selectors = response.xpath("//code")

            ## Parsing only the Python selectors based on the idxs we've parsed earlier
            code_selectors = [code_selectors[i] for i in idxs]

            ## Actual codes
            actual_codes = [
                "".join(cs.xpath(".//text()").getall()) for cs in code_selectors
            ]

            # Creating an item
            item = LeetcodeItem()

            # Yielding Data
            for label, code in zip(complexity_labels, actual_codes):
                item['label'] = label
                item['code'] = code

            yield item

            #import pdb
            #pdb.set_trace()

        # Follow next page if exists
        next_page = response.xpath(
            "//a[@class='md-footer__link md-footer__link--next']/@href"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
