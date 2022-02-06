#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kabul Ramadhan - 311810315
"""
import scraper
date_separator = {
        'kompas':'-',
        'tempo':'/', 
        'detik': '/',
        'metrotvnews': '/',
        'suara': '/',
        'sindo': '-'
        }

get_article = {
        'kompas':scraper.get_news_kompas,
        'tempo':scraper.get_news_tempo, 
        'detik' : scraper.get_news_detik,
        'metrotvnews' : scraper.get_news_metrotvnews,
        'suara' : scraper.get_news_suara,
        'sindo' : scraper.get_news_sindo
        }
