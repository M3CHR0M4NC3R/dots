#!/bin/bash
#
#Script to send a notification for volume changes
#

#case statement for inputs to this script


INTERVAL=250
#INTERVAL=0
case $1 in
	up)
		[ "$(brillo)" = "1.00" ] && {
			brillo -u $INTERVAL -S 5
		} || {
		brillo -u $INTERVAL -p -A 5
		}
		;;
	down)
		brillo -u $INTERVAL -p -U 5
		;;
esac


BRIGHTNESS=$(brillo)
BRIGHTNESS=${BRIGHTNESS::-3}
BAR=$(seq -s "󰹞" $(($BRIGHTNESS / 5)) | sed 's/[0-9]//g')

notify-send "Brightness $BRIGHTNESS%" $BAR -t 1500 -r 2593

