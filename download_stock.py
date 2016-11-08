
import urllib.request
import os
import csv

code_name = {}

def download_file(url,folder):
	req = urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
	response = urllib.request.urlopen(req)
	os.chdir(folder)
	code = response.info().get('Content-Disposition').split("=")[-1]
	filename = code.split('.')[0] + "_" + code_name.get(code.split('.')[0]).replace('*', '_') + '.csv'
	with open(filename,'wb') as f:
		f.write(response.read())
		f.close()
#download_file('http://quotes.money.163.com/service/chddata.html?code=1000004&start=19910102&end=20161104&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP','D:/')

def get_dict():
	with open('D:/scrapy study/stock/stocks_02.csv') as f:
		reader = csv.DictReader(f)
		for row in reader:
			code_name[row['代码']] = row['名称']

def get_url(code):
	return 'http://quotes.money.163.com/service/chddata.html?code=' + code + '&start=19800101&end=20161104&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

if __name__ == '__main__':
	print('Start downloading...')
	get_dict()
	for key in code_name.keys():
		print(key + ':' + code_name.get(key) + '...')
		if key.startswith('6'):
			key = '0' + key
		else:
			key = '1' + key
		url = get_url(key)
		download_file(url, 'D:/stock data')
	print('Finished...')