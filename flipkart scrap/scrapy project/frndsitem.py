import scrapy


class frndsscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    price=scrapy.Field()
    discount=scrapy.Field()
    description=scrapy.Field()
    actualprice=scrapy.Field()
    pass
