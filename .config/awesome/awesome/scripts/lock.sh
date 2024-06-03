scrot /tmp/screenshot.png -o
convert /tmp/screenshot.png -blur 0x5 /tmp/screenshotblur.png
i3lock -i /tmp/screenshotblur.png
rm /tmp/screenshot.png
