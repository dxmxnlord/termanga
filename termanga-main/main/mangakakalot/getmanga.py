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
	lis=soup.find_all('li',{'class':'a-h'})
	links=[]
	names=[]
	for li in lis:
		links.append(li.a['href'])
		names.append(li.a.string)

	count = len(names)
	for name in names:
		print(count,' ',name)
		count-=1
	print()
	print('(enter \'x\' to exit)')
	choice=input('enter number: ')
	if(choice=='x'):
		exit()
	else:
		choice=int(choice)
	return (links[len(names)-choice],names[len(names)-choice],manga_link[1])