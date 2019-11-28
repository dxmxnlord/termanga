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

def download_page(link,count):
	try: 
		req=ur.Request(link,headers=hdr)
	except:
		req=ur.Request(link,headers=hdr)
	reg_obj=re.compile('[\s\S]*.(jpg|jpeg|png)')
	extension=re.match(reg_obj,link)
	file_name=str(count)+"."+extension.groups()[0]
	with ur.urlopen(req) as response, open(file_name,'wb') as write_file:
		try:
			meta=response.info()
			file_size = int(meta.get("Content-Length"))
			print("Downloading: %s Bytes: %s" % (file_name, file_size))
			file_size_dl = 0
			block_sz = 8192
			while True:
			    buffer = response.read(block_sz)
			    if not buffer:
			        break
			    file_size_dl += len(buffer)
			    write_file.write(buffer)
			    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl*100/file_size)
			    status = status + chr(8)*(len(status)+1)
			    print(status)
		except:				
			data=response.read()
			write_file.write(data)