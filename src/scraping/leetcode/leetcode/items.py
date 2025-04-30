# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeetcodeItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    label = scrapy.Field()
    
