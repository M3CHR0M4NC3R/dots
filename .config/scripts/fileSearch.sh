#!/bin/bash

#v2
#locate -i $HOME | rofi -threads 0 -dmenu -keep-right -i -p "Files" | xargs -r0 xdg-open

#v1
FILE=$(locate $HOME | rofi -threads 0  -keep right -dmenu -i -config $HOME/.config/rofi/search.rasi)

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
