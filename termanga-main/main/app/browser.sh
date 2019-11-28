#!/bin/bash
abs_dir="$(pwd)/"
base_dir=$abs_dir
curr_dir=$base_dir
old_dir=$base_dir

function display {
	beg=$1
	end=$2
	curr=$3
	line=0
	for var in $(ls -p $base_dir); do
		if [ $line -ge $beg ] && [ $line -lt $end ]; then
			if [ ${#var} -gt $(($columns-4)) ]; then
			    var=$(echo $var | cut -c 1-$(($columns-4)))
			fi
			if [ $line -eq $curr ]; then
                # curr_dir=$(echo $base_dir | sed "s/\/[^\/]*$/\/${var}/")
                curr_dir="${base_dir}${var}"
                echo $curr_dir >> "curr.txt"
			    tput smso
			    echo -e "$line $var"
			    tput rmso
			else
			    echo -e "$line $var"
			fi 
		fi
		((line++))
	done
}

function goback {
    minicount=$1
    while [ $minicount -gt 0 ]; do
        echo -e "\r\b\r"
        ((minicount--))
    done
}

columns=$(tput cols)
rows=$(tput lines)

tput civis
clear
tput cup 0 0
count=$(ls $base_dir| wc -l)
top=0
current=0
# cut output
if [ $count -lt $rows ]; then
	bottom=$count
else
	bottom=$(($rows-1))
fi

# display $top $bottom $current
doclear=0

while true; do
	if [ $doclear -eq 1 ]; then
		read -rsn1 ui
	fi
    
    case "$ui" in
    $'\x1b')
        read -rsn1 -t 0.1 tmp
        if [[ "$tmp" == "[" ]]; then
            read -rsn1 -t 0.1 tmp
            case "$tmp" in
            "A") 
				if [[ $(($current)) -gt $top ]]; then 
					((current--))
				fi
                ;;
            "B") 
				if [[ $(($current+1)) -lt $bottom ]]; then 
					((current++))
				fi
                ;;
            "C")
                old_dir=$base_dir
                base_dir=$curr_dir
                curr_dir=$base_dir
                top=0
                current=0
                count=$(ls $base_dir| wc -l)
                if [ $count -lt $rows ]; then
                    bottom=$count
                else
                    bottom=$(($rows-1))
                fi
                clear
                ;;
            "D")
                base_dir=$old_dir
                old_dir=$abs_dir
                curr_dir=$base_dir
                top=0
                current=0
                count=$(ls $base_dir| wc -l)
                if [ $count -lt $rows ]; then
                    bottom=$count
                else
                    bottom=$(($rows-1))
                fi
                clear
                ;;
            esac
        fi
        read -rsn5 -t 0.1
        ;;
    q) 
        tput cnorm
        clear
        break
        ;;

    n) 
        if [[ $(($top + $rows)) -lt $count ]]; then 
            top=$bottom
            if [[ $(($bottom+$rows)) -lt $count ]]; then
                bottom=$(($bottom+$rows-1))
            else
                bottom=$(($count-1))
            fi
            current=$(($top))
            clear
            # tput cup 0 0
            # echo $top $bottom $current
        fi
        ;;

    p) 
        if [[ $(($top - $rows+1)) -ge 0 ]]; then 
            top=$(($top-$rows+1))
            bottom=$(($top+$rows-1))
            current=$top
            clear
            # tput cup 0 0
            # echo $top $bottom $current
        fi
        ;;

    esac

    tput cup 0 0
    display $top $bottom $current
    # echo $curr_dir
    goback $(($bottom-$top))

    if [[ $doclear -eq 0 ]]; then 
    	doclear=1
    fi
done