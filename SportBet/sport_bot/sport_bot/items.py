# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Team(scrapy.Item):
    # define the fields for your item here like:
    team_id = scrapy.Field()
    name = scrapy.Field()

class Site(scrapy.Item):
    team_id = scrapy.Field()
    propability = scrapy.Field()
    site = scrapy.Field()
