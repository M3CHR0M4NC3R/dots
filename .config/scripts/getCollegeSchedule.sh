#!/bin/bash
SCHEDULEPATH="$HOME/Documents/wiki/College/Schedule.wiki"

TODAY=$(sed -n "/$(date '+%A')/,/^\s*$/p" $SCHEDULEPATH)
#TODAY=$(sed -n "/Friday/,/^\s*$/p" $HOME/Documents/wiki/Schedule.wiki)
if [ "$TODAY" = "" ]
then
	echo '* No class today.'
else
	echo "$TODAY"
fi
