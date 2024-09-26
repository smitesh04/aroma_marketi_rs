# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AromaMarketiRsItemCoffee(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    mrp = scrapy.Field()
    country = scrapy.Field()
    pagesave = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
