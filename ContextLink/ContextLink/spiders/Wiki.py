import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import ContextlinkItem
import nltk
import string
import re
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
		text=k.text
		text=re.sub('—',' ',text)
		#table=str.maketrans('','',string.punctuation)
		#text=text.translate(table)
		tokens=nltk.word_tokenize(text)
		pos_tag1=nltk.pos_tag(tokens)
		grammer=r"""NP: {<NN.?>+<IN>+<NN.?>+}
						{<NN.?>+}
		  """
		cp=nltk.RegexpParser(grammer)
		result=cp.parse(pos_tag1)
		foll_links = scrapy.Selector(text=str(k))
		link_list=foll_links.css('a').xpath('@href').extract();
		title_tags=[ h1_tag for h1_tag in soup.find_all('h1')]
		ol_text=foll_links.css('a::text').extract();
		doc2=[subtree for subtree in result.subtrees(filter=lambda t: t.label() == 'NP')]
		text1=[]
		for element in doc2:
			ist=""
			for (text, tag) in element:
				if text not in string.punctuation: 
					ist += text
					ist+=' '
			text1.append(ist[0:len(ist)-1])
		#result.draw()
		i=0
		for word in text1:
			if word in ol_text:
				i=i+1
		p=i/len(text1)
		r=i/len(ol_text)
		items['title']=title_tags[0].text
		items['url']=response.url
		items['text']=k.text
		items['pages']=link_list
		items['entities_nltk']=text1
		items['nouns_from_site']=ol_text
		items['precision_s']=p
		items['recall']=r
		yield items
		for link in link_list:
			if link is not None:
				yield response.follow(link, self.parse)