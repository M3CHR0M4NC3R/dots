#!/bin/bash
#path to scrips folder
SCRIPTS=$HOME/.config/scripts/
selected=$(ls $SCRIPTS --ignore rofiScriptMenu.sh |rofi -dmenu -i -p "Scripts Menu")
exec $selected
