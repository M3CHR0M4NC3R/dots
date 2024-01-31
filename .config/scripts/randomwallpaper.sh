#!/bin/bash
#picks a random wallpaper and sets it, go figure
#the next two lines can be used to use multiple backends, but I only use colorz
#BACKEND=$(wal --backend | grep - | rofi -dmenu)
#BACKEND="${BACKEND:3}"
export PATH=$PATH:$HOME/.config/scripts/walLightDarkToggle/
lastUsed=$(getLastUsedLorD.sh)
[ "$lastUsed" = "light" ] &&
	wal -l -a 80 -i $HOME/Pictures/wallpapers/ --recursive --cols16 --backend colorz -o manualReload.sh ||
	wal -a 80 -i $HOME/Pictures/wallpapers/ --recursive --cols16 --backend colorz -o manualReload.sh
