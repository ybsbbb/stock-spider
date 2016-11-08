# stock-spider
stock文件夹是使用Scrapy框架写的股票爬虫，爬取当前所有股票的信息，使用时需要python3.5.2环境和scarpy框架，

python3.5.2安装可见官方网站:python.org  scrapy安装方式可见官方文档:docs.scrapy.org

其他版本未必能用


download_stock可以爬取所有股票的的历史数据，数据来源：网易财经，使用时需要上一个爬虫爬取到的数据，同时需要修改一些文件路径的参数，

以及get_url()中返回链接的参数，将end后面的参数改为当天日期，否则只能得到截止至2016年11月4日的数据
