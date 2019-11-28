#!/bin/bash

while [ true ]; do
	tput civis
	clear
	toilet -f mono12 -F metal termanga 
	toilet -f smblock -F metal "  Download  (  1 )                Read  (  2 )" 
	echo -e "\n\n\n"
	toilet -f smblock -F metal " >> "
	read -rsn1 inp
	case "$inp" in
		1)
			clear
			python3 "../mangaeden/mangascript.py"
			;;
		2)
			./read.sh
			;;
		q)
			break
			;;
	esac
	echo -e "\r"
	tput cnorm
done
clear
