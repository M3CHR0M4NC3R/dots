#!/bin/bash
export PATH=$PATH:$HOME/.config/scripts/walLightDarkToggle/
lastUsed=$(getLastUsedLorD.sh)
wallpaper=$(swapWallpaper.sh)
[ "$lastUsed" = "light" ] && {
	wal -a 80 -i "$wallpaper" --cols16 --backend colorz -o $HOME/.config/scripts/manualReload.sh & pywalfox dark
} || {
	wal -l -a 80 -i "$wallpaper" --cols16 --backend colorz -o $HOME/.config/scripts/manualReload.sh & pywalfox light
}
