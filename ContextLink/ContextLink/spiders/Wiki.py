import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import ContextlinkItem
class WikiSpider(scrapy.Spider):
	name='wiki'
	start_urls=['https://en.wikipedia.org/wiki/Government_of_India']
	allowed_domains = ['wikipedia.org']
	def parse(self,response):
		items=ContextlinkItem()
		soup = BeautifulSoup(response.text, "html.parser")
		req_info_list=[ p_tag for p_tag in soup.find_all('p')]
		global k;
		for w in req_info_list:
			if(len(w)>10):
				k=w;
				break;

		foll_links = scrapy.Selector(text=str(k))
		link_list=foll_links.css('a').xpath('@href').extract();
		title_tags=[ h1_tag for h1_tag in soup.find_all('h1')]
		items['title']=title_tags[0].text
		items['url']=response.url
		items['text']=k.text
		items['pages']=link_list
		yield items
		for link in link_list:
			if link is not None:
				yield response.follow(link, self.parse)