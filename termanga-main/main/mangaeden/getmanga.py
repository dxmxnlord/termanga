import bs4
import urllib.request as ur
import re
import os
import time
import json

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def get_manga(manga_link):
	link=manga_link[0]
	req=ur.Request(link,headers=hdr)
	obj=ur.urlopen(req)
	soup=bs4.BeautifulSoup(obj,features='lxml')
	tds=soup.find_all('td')
	anchors=[]
	for td in tds:
		try:
			if td.a['class']==['chapterLink']:
				anchors.append(td.a)
		except:
			continue
	return (anchors,manga_link[1])