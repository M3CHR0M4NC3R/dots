#!/bin/bash
#this script is a little superfluous, but it is more
#readable in my qtile config to have this long command
#in a script
#
rofi -show power-menu -modi power-menu:rofi-power-menu -config $HOME/.config/rofi/power.rasi
