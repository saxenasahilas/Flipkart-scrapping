# -*- coding: utf-8 -*-


import scrapy
from ..items import frndsscrapingItem

class FrndsSpider(scrapy.Spider):

    name='frnds'

    start_urls=['https://www.flipkart.com/mens-clothing/tshirts/pr?sid=2oq%2Cs9b%2Cj9y&otracker=nmenu_sub_Men_0_T-Shirts&page={}'.format(i) for i in range(1000)]

    def parse(self,response):

        a=response.css('._2B_pmu::text').getall()
        b=response.css('._1vC4OE::text').getall()
        c=response.css('.VGWI6T span::text').getall()
        d=response.css('._2mylT6::text').getall()
        e=response.css('._3auQ3N::text').getall()
        for item in zip(a,b,c,d,e):
             yield {
                    'title':item[0],
                    'price':item[1],
                    'discount':item[2],
                    'description':item[3],
                    'actualprice':item[4]
                    
                }
        
      
