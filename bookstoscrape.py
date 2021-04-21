# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookstoscrapeSpider(CrawlSpider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/h3/a"), callback= 'parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"), callback = 'parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'Book_name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'Book_price': response.xpath("//p[@class='price_color']/text()").get()
        }
