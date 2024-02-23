#!/bin/bash

#there are two options for this script, one will omit hidden files
[ "$1" = "hidden" ] && FILE=$(find ~ | rofi -threads 0  --keep-right -dmenu -i)
[ "$1" != "hidden" ] && FILE=$(find ~ -not -path '*/\.*' | rofi -threads 0  --keep-right -dmenu -i)

#save the above output as a variable first, then query what .desktop opens it
#if that desktop file has terminal=true, hit that shit with alacritty -e
#
#this line gets true or false for a desktop file
PROGRAM=$(xdg-mime query default $(xdg-mime query filetype "$FILE"))
TERMPGRM=$(grep -i '^Terminal=' /usr/share/applications/$PROGRAM | cut -d '=' -f2)
#echo $FILE $PROGRAM $TERMPGRM
[ "$TERMPGRM" = "true" ] && {
	$($HOME/.config/scripts/getTerminal.sh) -e xdg-open "$FILE"
} || {
	xdg-open "$FILE"
}
