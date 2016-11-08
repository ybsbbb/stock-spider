# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import json, codecs, csv
from scrapy import signals
from scrapy.exporters import CsvItemExporter

class StockPipelineJSON(object):

    def open_spider(self,spider):
        self.file = codecs.open('stocks.json', 'w', encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        #line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        code = json.dumps("股票代码:"+str(item['code']),ensure_ascii=False)
        link = json.dumps("链接:"+str(item['link']),ensure_ascii=False)
        name = json.dumps("名称:"+str(item['name']),ensure_ascii=False)
        curprice = json.dumps("现价:"+str(item['curprice']),ensure_ascii=False)
        change_rate = json.dumps("涨跌幅:"+str(item['change_rate']),ensure_ascii=False)
        change_price = json.dumps("涨跌:"+str(item['change_price']),ensure_ascii=False)
        up_speed = json.dumps("涨速:"+str(item['up_speed']),ensure_ascii=False)
        turnover_rate = json.dumps("换手率:"+str(item['turnover_rate']),ensure_ascii=False)
        ratio = json.dumps("量比:"+str(item['ratio']),ensure_ascii=False)
        amplitude = json.dumps("振幅:"+str(item['amplitude']),ensure_ascii=False)
        turnover_volume = json.dumps("成交额:"+str(item['turnover_volume']),ensure_ascii=False)
        tradable_shares = json.dumps("流通股:"+str(item['tradable_shares']),ensure_ascii=False)
        circulation_market_value = json.dumps("流通市值:"+str(item['circulation_market_value']),ensure_ascii=False)
        P_E_ratio = json.dumps("市盈率:"+str(item['P_E_ratio']),ensure_ascii=False)
        line = code + link + name + curprice + change_rate + change_price + up_speed + turnover_rate + ratio + amplitude + turnover_volume + tradable_shares + circulation_market_value + P_E_ratio + "\n"
        self.file.write(line)
        return item


class StockPipelineCSV2(object):
    def open_spider(self,spider):
        self.file = open('stocks_02.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        line = ['代码','链接','名称','现价','涨跌幅','涨跌','涨速','换手','量比','振幅','成交额','流通股','流通市值','市盈率']
        self.writer.writerow(line)

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        #code = str.encode("\"" + item['code'] + "\"").decode()
        code = item['code']
        link = str.encode(item['link']).decode()
        name = str.encode(item['name']).decode()
        curprice = str.encode(item['curprice']).decode()
        change_rate = str.encode(item['change_rate']).decode()
        change_price = str.encode(item['change_price']).decode()
        up_speed = str.encode(item['up_speed']).decode()
        turnover_rate = str.encode(item['turnover_rate']).decode()
        ratio = str.encode(item['ratio']).decode()
        amplitude = str.encode(item['amplitude']).decode()
        turnover_volume = str.encode(item['turnover_volume']).decode()
        tradable_shares = str.encode(item['tradable_shares']).decode()
        circulation_market_value = str.encode(item['circulation_market_value']).decode()
        P_E_ratio = str.encode(item['P_E_ratio']).decode()
        line = [code, link, name, curprice, change_rate, change_price, up_speed, turnover_rate, ratio, amplitude, turnover_volume, tradable_shares, circulation_market_value, P_E_ratio]
        self.writer.writerow(line)
        return item

class StockPipelineCSV(object):

    def open_spider(self,spider):
        self.file = open('stocks_01.csv', 'w')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item