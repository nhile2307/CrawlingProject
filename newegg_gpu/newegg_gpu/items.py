# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggItem(scrapy.Item):
    itemID = scrapy.Field()
    item = scrapy.Field()
    branding = scrapy.Field()
    rating = scrapy.Field()
    ratingNum = scrapy.Field()
    price = scrapy.Field()
    shippingFee = scrapy.Field()
    imgUrl = scrapy.Field()
    maxResolution = scrapy.Field()
    displayPort = scrapy.Field()
    hdmi = scrapy.Field()
    directX = scrapy.Field()
    model = scrapy.Field()
