# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoponlineItem(scrapy.Item):
    pass

class ProductItem(scrapy.Item):
    category_id = scrapy.Field()
    product_id = scrapy.Field()
    product_name = scrapy.Field()
    price_sale = scrapy.Field()
    price = scrapy.Field()
    link_image = scrapy.Field()
    link_url = scrapy.Field()
