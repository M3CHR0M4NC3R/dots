#!/bin/bash
#
#Script to send a notification for volume changes
#

#case statement for inputs to this script
case $1 in
	up)
		pactl set-sink-volume @DEFAULT_SINK@ +5%
		;;
	down)
		pactl set-sink-volume @DEFAULT_SINK@ -5%
		;;
	mute)
		pactl set-sink-mute @DEFAULT_SINK@ toggle
		;;
esac

VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | awk '{print$12}' | tr -dc '0-9')
BAR=$(seq -s "◼" $(($VOLUME / 5)) | sed 's/[0-9]//g')
EMPTYBAR=$(seq -s "◻" $((20-${#BAR}))  | sed 's/[0-9]//g')



notify-send "Volume $VOLUME%" "$BAR$EMPTYBAR" -t 1500 -r 2593
