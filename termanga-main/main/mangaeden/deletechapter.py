import urllib.request as ur
import re
import os
import time
import json

def delete_chapter():
	with open('../../data/MangaEden/titles.json','r') as json_file:
		titles=json.load(json_file)
	count=1
	if titles["titles"] == "empty":
		exit()
	for title in titles["titles"]:
		print(str(count)+" "+title)
		count+=1
	print()
	print('(enter \'x\' to exit)')
	choice=input('enter the number: ')
	if(choice=='x'):
		exit()
	os.system('clear')
	title=titles["titles"][int(choice)-1]
	with open('../../data/MangaEden/'+title+'/chapters.json','r') as json_file:
		chapters=json.load(json_file)
	choice=1
	for chapter in chapters["chapters"]:
		print(str(choice)+" "+chapter["chaptername"])
		count+=1
	print()
	print('(enter \'x\' to exit)')
	choice=input('enter the number: ')
	if(choice=='x'):
		exit()
	chapter=chapters["chapters"][int(choice)-1]
	os.system('rm -fr '+'"../../data/MangaEden/'+title+'/'+chapter["chaptername"]+'"')
	with open('../../data/MangaEden/'+title+'/chapters.json','w') as json_file:
		json_object={}
		for json_a in chapters:
			if(json_a=="chapters"):
				json_object[json_a]=[]
				for json_b in chapters[json_a]:
					if json_b != chapter:
						json_object[json_a].append(json_b)
				if len(json_object[json_a])==0 :
					status=True
			else:
				json_object[json_a]=chapters[json_a]
		json.dump(json_object,json_file)
	if(status):
		with open('../../data/MangaEden/titles.json','w') as json_file:
			json_object={}
			for json_a in titles:
				json_object[json_a]=[]
				for json_b in titles[json_a]:
					if json_b != title:
						json_object[json_a].append(json_b)
				if len(json_object[json_a]) == 0 :
					json_object[json_a]="empty"
			json.dump(json_object,json_file)
		os.system('rm -fr '+'"../../data/MangaEden/'+title+'"')
	print('deleted')