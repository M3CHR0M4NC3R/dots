#!/bin/bash
#path to scrips folder
DISPLAYS=$HOME/.screenlayout/
selected=$(ls $DISPLAYS|rofi -dmenu -i -p "Which display do you want?: ")
exec $DISPLAYS/$selected &
~/.fehbg
