from pathlib import Path
import pdb
import scrapy


class LeetcodeSpider(scrapy.Spider):
    name = "leetcode"
    language_to_scrape = "Python"

    allowed_domains = ["https://walkccc.me"]
    start_urls = ["https://walkccc.me/LeetCode/problems/3/"] 

    def parse(self, response):
        # Parse time complexity label
        
        #pdb.set_trace()        
        complexity_labels = response.xpath("//ul[@class='task-list']/li[1]/text()").getall() 
        # Remove empty strings (save only if after stripping a string, the string is still non NaN)
        complexity_labels = [l for l in complexity_labels if l.strip()]

        # Parse python tabbed code
        # (choose the language the solution should be displayed in)
        
        ## Saved anchors to follow
        language_anchors = []
        
        ## Parse solution language labels
        anchors = response.css("div.tabbed-labels > label::text").getall()

        ## Parse the positions of python code anchor boxes
        idxs = [idx for idx, anchor in enumerate(anchors) if anchor == 'Python']

        ## Parse the code boxes
        code_selectors = response.xpath("//code")

        ### Parsing only the Python selectors based on the idxs we've parsed earlier
        code_selectors = [code_selectors[i] for i in idxs]

        # Codes formatting (indentations and spaces)
        codes_formatting = [cs.xpath("text()").getall() for cs in code_selectors]
        # Actual codes
        actual_codes = [cs.xpath("span/text()").getall() for cs in code_selectors]
        pdb.set_trace()
        

        # Opening python code anchors and parsing
        #for tab in language_anchors:
            #response.follow(url=tab, callback=self.parse_code)
        response.follow_all(urls=language_anchors, callback=self.parse_code)

    def parse_code(self, response):
        print("\n\n", response.url, "\n\n")