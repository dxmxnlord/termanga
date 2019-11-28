#!/bin/bash

path=$1
pagecount=$(ls "$path" | wc -l)

# if [ -n "$WINDOWID" ]
# then
#     xwininfo -id $WINDOWID | awk '
#     BEGIN { px = 0; py = 0; chars = "?x?"; }
#     /Height:/ { py = $2; }
#     /Width:/ { px = $2; }
#     /-geometry/ { chars = $2; sub("+.*","",chars); }
#     END { printf "%dx%d pixels, %s chars\n", py, px, chars; }
#     '
# else
#     printf '? no WINDOWID found\n'
# fi

height=$( xwininfo -id $WINDOWID | grep -o -e "Height: .*" | grep -o -e "[0-9]*")
height=$((height - 30))
width=$( xwininfo -id $WINDOWID | grep -o -e "Width: .*" | grep -o -e "[0-9]*")
width=$(( width - 30 ))
xoffset=0
yoffset=0
draw=0
current=0
tput civis
while [ true ]; do
	clear
	# echo -e '0;1;0;0;630;668;;;;;${path}\n4;\n3;' | /usr/lib/w3m/w3mimgdisplay
    if test -e "${path}${current}.jpg"; then
        echo -e "${draw};1;${xoffset};${yoffset};${width};${height};;;;;${path}${current}.jpg\n4;\n3;" | /usr/lib/w3m/w3mimgdisplay
	elif test -e "${path}${current}.jpeg"; then
        echo -e "${draw};1;${xoffset};${yoffset};${width};${height};;;;;${path}${current}.jpeg\n4;\n3;" | /usr/lib/w3m/w3mimgdisplay
    elif test -e "${path}${current}.png"; then
        echo -e "${draw};1;${xoffset};${yoffset};${width};${height};;;;;${path}${current}.png\n4;\n3;" | /usr/lib/w3m/w3mimgdisplay
    fi
    read -rsn1 input
    # quit
	if [ $input = "q" ]; then
		clear
		break
	fi
    # next
    if [ $input = "d" ]; then
        ((current++))
        if [ $current -gt $pagecount ]; then
            clear
            break
        fi
    fi
    # previous
    if [ $input = "a" ]; then
        ((current--))
        if [ $current -lt 0 ]; then
            clear
            break
        fi
    fi
    # shrink height
    if [ $input = "w" ]; then 
        height=$((height - 10))
    fi
    # shrink width
    if [ $input = "s" ]; then 
        width=$((width - 10))
    fi
    # grow height
    if [ $input = "W" ]; then 
        height=$((height + 10))
    fi
    # grow width
    if [ $input = "S" ]; then 
        width=$((width + 10))
    fi
    # reset to normal
    if [ $input = "r" ]; then 
        height=$( xwininfo -id $WINDOWID | grep -o -e "Height: .*" | grep -o -e "[0-9]*")
        height=$((height - 30))
        width=$( xwininfo -id $WINDOWID | grep -o -e "Width: .*" | grep -o -e "[0-9]*")
        width=$(( width - 30 ))
        xoffset=0
        yoffset=0
    fi
    # center 
    if [ $input = "c" ]; then
        xoffset=$((width/4))
        width=$((width/2))
    fi  
done
tput cnorm