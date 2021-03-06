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

def search_manga():
	term=input("enter search term: ")
	term=ur.pathname2url(term)
	search_link='https://www.mangaeden.com/en/en-directory/?title='+term+'&author=&artist=&releasedType=0&released='
	req=ur.Request(search_link,headers=hdr)
	obj=ur.urlopen(req)
	soup=bs4.BeautifulSoup(obj,features='lxml')
	links=[]
	names=[]
	anchors=soup.find_all('a')
	for anchor in anchors:
		try:
			if anchor['class'] == ['openManga'] or anchor['class'] == ['closedManga']:
				names.append(anchor.string)
				links.append('https://www.mangaeden.com'+anchor['href'])
		except:
			continue
	count=1
	for name in names:
		print(str(count)+" "+name)
		count+=1
	print()
	print('(enter \'x\' to exit)')
	choice=input("enter the number: ")
	if(choice=='x'):
		exit()
	return (links[int(choice)-1],names[int(choice)-1])
