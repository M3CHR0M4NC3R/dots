#!/bin/bash
COLOR=$(sed -n -e 2p $HOME/.cache/wal/colors)
sed -i "s/foreground = .*/foreground = \"$COLOR\"/" $HOME/.config/dunst/dunstrc
COLOR=$(sed -n -e 1p $HOME/.cache/wal/colors)
sed -i "s/background = .*/background = \"$COLOR\"/" $HOME/.config/dunst/dunstrc
pkill dunst && dunst

