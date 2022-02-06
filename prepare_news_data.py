# -*- coding: utf-8 -*-
"""
Kabul Ramadhan - 311810315
"""

import pandas as pd
import ast
import re
import news_utils
#%%

def prepare(news_site_name, year):
  news_link = pd.read_csv('data/input/'+news_site_name+'_'+str(year)+'.csv')
  news_link_flat_url = []
  
  news_link_flat_date = []
  news_link_flat_month = []
  news_link_flat_year = []
  
  for i,item in news_link.iterrows():
    url_group=item['links']
    current_url_group = ast.literal_eval(url_group)
    
    current_datetime = item['dates']

    
    sep = news_utils.date_separator[news_site_name]
    for url_news in current_url_group:
      news_link_flat_url.append(url_news)
      news_link_flat_year.append(current_datetime.split(sep)[0])
      news_link_flat_month.append(current_datetime.split(sep)[1].replace("0"," "))
      news_link_flat_date.append(current_datetime.split(sep)[2].replace("0"," "))
      
  
  raw_news_text = []
  for i in range(len(news_link_flat_url)):
    content =  "UNSET"

    raw_news_text.append(content)
              
              
  final_dataset = pd.DataFrame()
  final_dataset['year'] = news_link_flat_year
  final_dataset['month'] = news_link_flat_month
  final_dataset['date'] = news_link_flat_date
  final_dataset['url'] = news_link_flat_url
  final_dataset['article'] = raw_news_text
  
  final_dataset.to_csv('data/intermediate/'+news_site_name+'_'+str(year)+'_news_data.csv', index=False)
  

