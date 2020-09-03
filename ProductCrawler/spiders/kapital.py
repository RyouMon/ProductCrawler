# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from .generic import GenericSpider


class KapitalSpider(GenericSpider):
    name = 'kapital'
    allowed_domains = ['kapital-webshop.jp']
    rules = [
        # matching each item in item list
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//ul[@class="item_list clearfix"]/li//div[@class="img_inner"]/a'
            ),
            callback='parse_item',
        ),
        # matching other pages
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@class="pager"]//a'
            ),
            callback='parse',
            follow=True
        )
    ]
