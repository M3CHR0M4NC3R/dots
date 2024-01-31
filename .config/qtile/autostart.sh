#!/bin/bash

#sxhkd
#$HOME/.config/sxhkd/launch.sh
#sxhkd & disown

light-locker &
lxpolkit &

#wal colors
$HOME/.config/wpg/wp_init.sh
#feh wallpaper
~/.fehbg


#autostart programs for qtile
#polybar &
#$HOME/.config/polybar/launch.sh

compfy & disown
#$HOME/.config/conky/launch.sh

