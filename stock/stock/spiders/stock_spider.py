# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector  
from stock.items import StockItem
import scrapy
#from stock.pipelines import StockPipelineCSV
class StockSpider(Spider):
    name = "stock"
    allowed_domains = ["q.10jqka.com.cn/"]
    #start_urls = [
    #   "http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/",
    #    ]

    def start_requests(self):
    	#StockPipelineCSV.from_crawler(self)
    	for i in range(1,137):
    		yield scrapy.Request('http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/%s/ajax/1/' % i)

    def parse(self,response):
    	sel = Selector(response)
    	stocks = sel.xpath("//tbody/tr")
    	items = []
    	for stock in stocks:
    		item = StockItem()
    		item['code'] = stock.xpath("td[2]/a/text()")[0].extract()
    		item['link'] = stock.xpath("td[2]/a[1]/@href")[0].extract()
    		item['name'] = stock.xpath("td[3]/a/text()")[0].extract()
    		item['curprice'] = stock.xpath("td[4]/text()")[0].extract()
    		item['change_rate'] = stock.xpath("td[5]/text()")[0].extract()
    		item['change_price'] = stock.xpath("td[6]/text()")[0].extract()
    		item['up_speed'] = stock.xpath("td[7]/text()")[0].extract()
    		item['turnover_rate'] = stock.xpath("td[8]/text()")[0].extract()
    		item['ratio'] = stock.xpath("td[9]/text()")[0].extract()
    		item['amplitude'] = stock.xpath("td[10]/text()")[0].extract()
    		item['turnover_volume'] = stock.xpath("td[11]/text()")[0].extract()
    		item['tradable_shares'] = stock.xpath("td[12]/text()")[0].extract()
    		item['circulation_market_value'] = stock.xpath("td[13]/text()")[0].extract()
    		item['P_E_ratio'] = stock.xpath("td[14]/text()")[0].extract()
    		items.append(item)
    	return items