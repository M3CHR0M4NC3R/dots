#!/bin/sh

# add more args here according to preference
ARGS="--no-video"

notification(){
# change the icon to whatever you want. Make sure your notification server 
# supports it and already configured.

# Now it will receive argument so the user can rename the radio title
# to whatever they want

	notify-send "Playing now: " "$@" --icon=media-tape
}

# number of the stream as per the $choice variable
# name of the stream
# additional tag to filter similar type of streams

menu(){
	printf "1. Lofi Girl <lofi>\n"
	printf "2. Chillhop <lofi>\n"
	printf "3. NDTV 24x7 <news>\n"
	printf "4. WION Live <news>\n"
	printf "5. dreamstation.fm <breakcore>\n"
	printf "6. Synthwave Boy <synthwave>\n"
}

main() {
	choice=$(menu | rofi -dmenu -p "Radio" -config $HOME/.config/rofi/radio.rasi | cut -d. -f1)

	case $choice in
		1)
			notification "Lofi Girl ☕️🎶";
            URL="https://www.youtube.com/watch?v=jfKfPfyJRdk"
	    ADDITIONAL_ARGS="--volume=50"
			break
			;;
		2)
			notification "Chillhop ☕️🎶";
            URL="https://youtu.be/7NOSDKb0HlU"
	    ADDITIONAL_ARGS="--volume=60"
			break
			;;
		3)
			notification "NDTV 24x7 📰";
            URL="https://youtu.be/WB-y7_ymPJ4"
	    ADDITIONAL_ARGS=""
			break
			;;
		
		4)
			notification "WION Live 📰"
            URL="https://youtu.be/lmZRiDMK3OU"
	    ADDITIONAL_ARGS=""
			break
			;;
		
		5)
			notification "breakcore radio 🔪💀🎵"
            URL="https://www.youtube.com/watch?v=fQjhvU0ocao"
	    ADDITIONAL_ARGS="--volume=60 --no-resume-playback"
			break
			;;
		6)
			notification "synthwave radio 🏙🖥🎶"
            URL="https://www.youtube.com/watch?v=4xDzrJKXOOY"
	    ADDITIONAL_ARGS="--volume=50 --no-resume-playback"
			break
			;;
		
		esac
    # run mpv with args and selected url
    # added title arg to make sure the pkill command kills only this instance of mpv
    mpv $ARGS --title="radio-mpv" $URL $ADDITIONAL_ARGS
}

pkill -f radio-mpv || main
