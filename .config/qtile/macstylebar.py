from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import bimbolib
import os
#wal color support
home = "/home/"+os.getlogin()
colors = []
cache=home+'/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)
def longNameParse(text):
    for string in ["Chromium", "Firefox", "Spotify", "spotify", "Alacritty", "Discord", "Thunderbird"]: 
#Add any other apps that have long names here
        if string in text:
            text = string
        else:
            text = text
    if text == "Navigator":
        text = "Firefox"
    return text

def noText(text):
    return ""
'''bar
 ▄▄▄▄    ▄▄▄       ██▀███  
▓█████▄ ▒████▄    ▓██ ▒ ██▒
▒██▒ ▄██▒██  ▀█▄  ▓██ ░▄█ ▒
▒██░█▀  ░██▄▄▄▄██ ▒██▀▀█▄  
░▓█  ▀█▓ ▓█   ▓██▒░██▓ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
▒░▒   ░   ▒   ▒▒ ░  ░▒ ░ ▒░
 ░    ░   ░   ▒     ░░   ░ 
 ░            ░  ░   ░     
      ░                    
'''
decoration_group = {
    "decorations": [
        RectDecoration(colour=colors[0]+"B0", radius=12, filled=True, padding_y=2, group=True)
    ],
}
widget_defaults = dict(
    font="SF Pro Display, Symbols Nerd Font Mono",
    fontsize=14,
    padding=5,
    rounded=True,
    foreground = colors[15],
    fontshadow=(colors[0]+"FA"),
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
        [
            widget.Spacer(length=widget_defaults["padding"]*2,), 
            widget.CPU(
            format=' {load_percent}%',
            font="SF Mono, Symbols Nerd Font"
            ), 
            widget.ThermalSensor(tag_sensor="CPUTIN",format=' {temp:3.1f}{unit}'),
            widget.ThermalSensor(tag_sensor="edge",format='󰢮 {temp:3.1f}{unit}'),
            widget.CurrentLayoutIcon(scale=.6,),
            widget.WidgetBox(
            widgets=[
                bimbolib.WindowClass(fmt='<b>{}</b>'),
            ],
                name="windowclassbox",
                start_opened=True,
                text_closed='',
                text_open='',
            ),
            widget.WidgetBox(
                widgets=[
                    widget.Chord(fmt='<b>{}</b>'),
                ],
                name="chordbox",
                start_opened=True,
                text_closed='',
                text_open='',
            ),
            widget.Spacer(length=bar.STRETCH,),
            widget.TextBox(
                "󰣇",
                padding=widget_defaults["padding"]*2,
                mouse_callbacks={
                    "Button1": lazy.spawn("rofi -show drun"),
                    "Button3": lazy.spawn(home+"/.config/scripts/rofi-power.sh"),
                },
                **decoration_group,
            ),
            widget.GroupBox(
                highlight_method='text',
                hide_unused=False,
                this_current_screen_border=(colors[3]),
                inactive=(colors[8]),
                active=(colors[1]),
                margin_x=0,
                padding=(widget_defaults["padding"]*.5),
                urgent_alert_method='line',
                urgent_border=colors[6],
                **decoration_group,
            ),
            widget.TextBox(
                "",
                padding=widget_defaults["padding"]*2,
                mouse_callbacks={
                    "Button1": lazy.spawn(home+"/.config/scripts/fileSearch.sh"),
                    "Button3": lazy.spawn(home+"/.config/scripts/fileSearch.sh hidden"),
                },
                **decoration_group,
            ),
            widget.Spacer(length=bar.STRETCH,),
            widget.Mpris2(
                format='{xesam:title} - {xesam:artist}',
                objname = "org.mpris.MediaPlayer2.spotify",
                poll_interval=2,
                scroll=True,
                width=int(bimbolib.monitorWidth*.1)
            ),
            widget.Spacer(length=widget_defaults["padding"]*2),
            #widget.Battery(),
            widget.PulseVolume(
                emoji_list=['󰝟','󰕿', '󰖀', '󰕾'],
                emoji=True,
                mouse_callbacks={"Button3": lazy.spawn("pavucontrol"),},
            ), 
            widget.Wlan(
                    format='󰖩 {percent:03.0%}',
                font="SF Mono, Symbols Nerd Font",
                mouse_callbacks={"Button1": lazy.spawn("iwgtk"),},
            ),
            widget.Clock(
                format='%a %b %d %I:%M %p',
                width=widget_defaults["fontsize"]*11
            ),
            #too proud of this one
            widget.Spacer(length=widget_defaults["padding"]*2),
        ], 
        int(bimbolib.monitorHeight*.0261111), 
        background=[(colors[0]+"A0")],
        #background = "#00000000",
        ),
    )
]
