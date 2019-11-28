#!/bin/bash

export open_path
dir=$(pwd | sed 's/main\/app/data\/MangaEden\//')
while [ true ]; do 
	source ./select.sh $dir
	if [ $open_path = "exit" ]; then
		break
	else
		./disp.sh "$open_path"
	fi
done