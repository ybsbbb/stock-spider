# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
	#num = scrapy.Field()
	link = scrapy.Field()
	code = scrapy.Field()
	name = scrapy.Field()
	curprice = scrapy.Field()
	change_rate = scrapy.Field()
	change_price = scrapy.Field()
	up_speed = scrapy.Field()
	turnover_rate = scrapy.Field()
	ratio = scrapy.Field()
	amplitude = scrapy.Field()
	turnover_volume = scrapy.Field()
	tradable_shares = scrapy.Field()
	circulation_market_value = scrapy.Field()
	P_E_ratio = scrapy.Field()