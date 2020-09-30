import bs4
import urllib.request as ur
import requests
import re
import os
import time
import json
import sys
from selenium import webdriver

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Referer': 'https://cssspritegenerator.com',
     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
     'Accept-Encoding': 'none',
     'Accept-Language': 'en-US,en;q=0.8',
     'Connection': 'keep-alive'}

def download_page(link,count,s):

	resp = s.get(link,stream=True)

	# reg_obj=re.compile('[\s\S]*.(jpg|jpeg|png)$')
	# extension=re.match(reg_obj,link)
	# file_name=str(count)+"."+extension.groups()[0]

	# # print(s.cookies)
	# with open(file_name, 'wb') as out_file:
	# 	resp.raw.decode_content = True
	# 	shutil.copyfileobj(resp.raw, out_file)  

if(len(sys.argv) > 1):
	os.chdir(f'../../data/Mangakakalot/{sys.argv[2]}/{sys.argv[3]}/')
	os.system('pwd')
	count = int(sys.argv[4])
	s = requests.Session()
	s.get(sys.argv[1])
	s.headers = hdr
	scraper = cfscrape.create_scraper(sess=s)
	cookie_arg, user_agent = cfscrape.get_cookie_string(sys.argv[1])
	result = subprocess.check_output(["curl", "--cookie", cookie_arg, "-A", user_agent, sys.argv[5]])
	# for c in range(0,count):
	# 	print(sys.argv[c+5])
		# download_page(sys.argv[c+5],c,scraper)