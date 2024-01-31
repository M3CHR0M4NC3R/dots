#!/bin/bash
#this script is used to manually reload apps that
#don't do it themselves after pywal resolves

#discord (requires betterdiscord and pywal-discord)
pywal-discord default &
#zathura (requires zathura pywal)
#zathura-pywal -a .94 &
#firefox (requires pywalfox)
#pywalfox update &
#sync colors with conky
#conky_colors.sh &
#sync colors with dunst, and restart it
#dunst_colors.sh
qtile cmd-obj -o cmd -f reload_config

#change lightdm background and theme
echo updating lightdm theme!
cp "$HOME/.config/wpg/wallpapers/$(wpg -c| sed 's/ /_/g')" /usr/share/wallpapers/background.png &
cp -r $HOME/.themes/FlatColor /usr/share/themes/
