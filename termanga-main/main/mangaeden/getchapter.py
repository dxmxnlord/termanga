import bs4
import urllib.request as ur
import re
import os
import time
import json
from downloadpage import download_page

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

def get_chapter(chap):
	req=ur.Request(chap[0],headers=hdr)
	obj=ur.urlopen(req)
	soup=bs4.BeautifulSoup(obj,features='lxml')
	try:
		os.chdir('../../data/MangaEden/'+chap[2])
	except:
		os.chdir('../../data/MangaEden/')
		os.mkdir('./'+chap[2])
		with open('./titles.json','r') as json_file:
			json_object=json.load(json_file)
		with open('./titles.json','w') as json_file:
			if json_object["titles"]=="empty" :
				json_object["titles"]=[chap[2]]
			elif chap[2] not in json_object["titles"] :
				json_object["titles"].append(chap[2])
			json.dump(json_object,json_file)
		os.chdir('./'+chap[2])
		os.system('touch chapters.json')
		with open('chapters.json','w') as json_file:
			json_object={"name":chap[2],"chapters":[]}
			json.dump(json_object,json_file)
	next='https://www.mangaeden.com'+soup.find_all(id='nextA')[0]['href']
	reg_comp=re.compile('[\s\S]*/(\d*)/\d*/')
	chap_num=re.match(reg_comp,next).groups()[0]
	img_link='https:'+soup.find_all(id='mainImg')[0]['src']
	try: 
		os.chdir('./'+chap[1])
	except:
		os.mkdir('./'+chap[1])
		with open('./chapters.json','r') as json_file:
			json_object=json.load(json_file)
		with open('./chapters.json','w') as json_file:
			if str(chap_num) not in list(filter(lambda x: x["chapternumber"]==str(chap_num),json_object["chapters"])) :
				json_object["chapters"].append({"chaptername":chap[1],"chapternumber":chap_num})
				json.dump(json_object,json_file)
				os.chdir('./'+chap[1])
	else:
		print('chapter exists')
		exit()
	os.system('clear')
	counter=0
	while(re.match(reg_comp,next).groups()[0] == chap_num):
		download_page(img_link,counter)
		counter+=1
		req=ur.Request(next,headers=hdr)
		obj=ur.urlopen(req)
		soup=bs4.BeautifulSoup(obj,features='lxml')
		next='https://www.mangaeden.com'+soup.find_all(id='nextA')[0]['href']
		img_link='https:'+soup.find_all(id='mainImg')[0]['src']
	download_page(img_link,counter)
	print('downloaded all')