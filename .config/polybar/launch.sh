#!/bin/bash

#Terminate already runnning bar instances
killall -q polybar
#If al lyour bars have ipc enabled, you can also use
#polybar-msg cmd quit
#
#Launch polybar, using default ocfig location ~/.config/polybar/config.ini
polybar
echo "Polybar launched..."
