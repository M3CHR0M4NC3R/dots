#!/bin/bash
current=$(wmctrl -d | grep '\*' | sed 's/.*\ //')
next=$((current+1))
prev=$((current-1))
if [[ $1 == "next" ]]
then
	echo $next
i3-msg workspace number "$next"
fi
if [[ $1 == "prev" ]]
then
	echo $prev
i3-msg workspace number "$prev"
fi
