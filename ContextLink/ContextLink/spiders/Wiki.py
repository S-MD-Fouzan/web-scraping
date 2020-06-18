import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import ContextlinkItem
class WikiSpider(scrapy.Spider):
	name='wiki'
	start_urls=['https://en.wikipedia.org/wiki/Bareilly_Ki_Barfi']
	def parse(self,response):
		items=ContextlinkItem()
		soup = BeautifulSoup(response.text, "html.parser")
		a=[ pt for pt in soup.find_all('p')]
		b=[ h1t for h1t in soup.find_all('h1')]
		items['title']=b[0].text
		items['url']=response.url
		items['text']=a[1].text
		yield items