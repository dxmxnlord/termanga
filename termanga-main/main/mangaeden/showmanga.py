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

def show_manga(anchors_data):
	count=1
	hrefs=[]
	titles=[]
	for anchor in anchors_data[0]:
		if(anchor==None):
			continue
		else:
			print(count,' ',anchor.b.string)
			titles.append(anchor.b.string)
			hrefs.append('https://www.mangaeden.com'+anchor['href'])
			count+=1
	print()
	print('(enter \'x\' to exit)')
	choice=input('enter number: ')
	if(choice=='x'):
		exit()
	else:
		choice=int(choice)
	return (hrefs[choice-1],titles[choice-1],anchors_data[1])

