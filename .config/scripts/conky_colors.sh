#!/bin/bash
LINES=$(wc -l < $HOME/.cache/wal/colors)
n=1
while [ $n -le $LINES ]
do
	NUMBER=$(($n-1))
	COLOR=$(sed -n -e $n\p $HOME/.cache/wal/colors)
	COLOR="${COLOR:1}"
	sed -i "s/color$NUMBER=.*/color$NUMBER='$COLOR',/" $HOME/.config/conky/conky.conf &
	sed -i "s/color$NUMBER=.*/color$NUMBER='$COLOR',/" $HOME/.config/conky/college\ widget.conf
	n=$(($n+1))
done
COLOR=$(sed -n -e 1p $HOME/.cache/wal/colors)
COLOR="${COLOR:1}"
sed -i "s/own_window_colour=.*/own_window_colour='$COLOR',/" $HOME/.config/conky/conky.conf &
sed -i "s/own_window_colour=.*/own_window_colour='$COLOR',/" $HOME/.config/conky/college\ widget.conf
