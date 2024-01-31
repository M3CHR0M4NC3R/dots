#!/bin/bash
#returns either light or dark depending on the contents of
#%HOME/.cache/wal/last_used_theme
firstLine=$(head $HOME/.cache/wal/colors -n1)
COLOR=${firstLine:1}
COLOR=$((0x$COLOR))
[ $COLOR -lt 8388608 ] && echo "dark" || echo "light"
