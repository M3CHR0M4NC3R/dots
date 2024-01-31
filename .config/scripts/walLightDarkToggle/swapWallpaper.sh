#!/bin/bash
wallpaper=$(cat $HOME/.cache/wal/wal)
lastword=$(echo ${wallpaper::-4} | awk '{print $NF}')
if [ $lastword == "Dark" ]
then
	newWord="Light"
elif [ $lastword == "Night" ]
then
	newWord="Day"
elif [ $lastword == "Light" ]
then
	newWord="Dark"
elif [ $lastword == "Day" ]
then
	newWord="Night"
else
	newWord=$lastword
fi

wallpaper=${wallpaper//$lastword/$newWord}
echo $wallpaper
