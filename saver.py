# -*- coding: utf-8 -*-
"""
Kabul Ramadhan - 311810315
"""
import re
import time
import pandas as pd
import numpy as np
import random
from news_utils import scraper
from prepare_news_data import prepare

agents = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246']


def get_article(news_site_name, url, headers):
    #TODO : change to select function from dict
    if news_site_name == 'kompas':
        return scraper.get_news_kompas(url, headers)
    elif news_site_name == 'tempo':
        return scraper.get_news_tempo(url, headers)
    elif news_site_name == 'detik':
        return scraper.get_news_detik(url, headers)
    elif news_site_name == 'metrotvnews':
        return scraper.get_news_metrotvnews(url, headers)
    
def start_scrap(news_site_name, start, end):
  try:
    news_data = pd.read_csv('data/intermediate/'+news_site_name+'_news_data.csv', encoding='ISO-8859-1')
  except IOError:
    prepare(news_site_name)
    print("file not found, preparing new file..")
    news_data = pd.read_csv('data/intermediate/'+news_site_name+'_news_data.csv', encoding='ISO-8859-1')
  
  if end == 'max':
    end = len(news_data)
  
  for i in range(start,end):
    news_item = news_data.ix[i]
    if news_item['article'] == "WAITING":
      # Add random sleep time at maximum 3 seconds to prevent suspicious action
      time.sleep(np.random.randint(1,3)) 
      
      # Some site specific worpkaround
      # TODO : Very bad workaround, try something else please
      if news_site_name=='tempo':
        if(news_item['url'][:5] == '/read'):
          url='http://tempo.co'+news_item['url']
        else:
          url=news_item['url']
      else:
        url = news_item['url']

      # Shuffeling user agents
      selected_agent = random.choice(agents)
      headers = {'User-Agent': selected_agent}
      
      # Call get_article_function, save to downloaded_article
      downloaded_article = get_article(news_site_name, url, headers)
      if news_site_name=='detik':
        news_data.set_value(i, 'article', downloaded_article)
        print(downloaded_article)
      else:
        news_data.set_value(i, 'article', re.sub(r'[^\x00-\x7F]+',' ', downloaded_article))
      news_data.to_csv('data/intermediate/'+news_site_name+'_news_data.csv', index=False)
      print(str(news_item['date'])+'/'+str(news_item['month'])+'/'+str(news_item['year'])+ ' data '+ str(i)+ ' saved!')
        
if __name__ == "__main__":   
  site='detik'
  start_scrap(site,0,2)
