import bs4
import urllib.request as ur
import re
import os
import time
import json

# from downloadpage import download_page

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
		os.chdir('../../data/Mangafast/'+chap[2])
	except:
		os.chdir('../../data/Mangafast/')
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

	reg_comp=re.compile('.*chapter-([\d-]+)/$')
	chap_num=re.match(reg_comp,chap[0]).groups()[0]
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
	img_links = []
	# is_manga_img=re.compile('^/ads/.*')
	divs = soup.find_all('div',{'id':'Read'})
	for div in divs:
		for img in div.find_all('img'):
			try:
				img_links.append(img['data-src'].replace('?q=70',''))
			except:
				try:
					if img['itemprop'] == "image":
						img_links.append(img['src'].replace('?q=70',''))
				except:
					continue;
	no_of_img = len(img_links)
	img_links = '" "'.join(img_links)
	os.chdir('../../../../main/mangafast/')
	args = f'"{chap[0]}" "{chap[2]}" "{chap[1]}" {str(no_of_img)} "{img_links}"'
	os.system("python3 downloadpage.py "+args)