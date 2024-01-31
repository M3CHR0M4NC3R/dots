#!/bin/bash
THEME=$(wpg --theme | rofi -dmenu -i -p "Color Schemes" -scroll-method 1)
exec wpg -n --theme $THEME
