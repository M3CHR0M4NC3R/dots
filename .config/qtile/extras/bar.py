from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
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
    for string in ["Chromium", "Firefox", "Spotify", "spotify", "Alacritty", "Discord"]: #Add any other apps that have long names here
        if string in text:
            text = string
        else:
            text = text
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
nodecoration_group = {
    "decorations": [
     ],
}
decoration_group = {
    "decorations": [
        RectDecoration(colour=colors[0],
        radius=15,
        filled=True,
        group=True,
        margin_x=20,
        )
    ],
}
widget_defaults = dict(
    font="SF Pro Display, Symbols Nerd Font Mono",
    fontsize=16,
    padding=10,
    rounded=True,
    foreground = colors[15],
    fontshadow=(colors[0]+"FA"),
    **decoration_group,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
        [
            #widget.Spacer(length=widget_defaults["padding"]*2,), 
            widget.TextBox(
                "󰣇",
                mouse_callbacks={
                    "Button1": lazy.spawn("rofi -show drun"),
                    "Button3": lazy.spawn(home+"/.config/scripts/rofi-power.sh"),
                }
            ),
            widget.GroupBox(
                highlight_method='text',
                hide_unused=False,
                this_current_screen_border=(colors[3]),
                inactive=(colors[1]+"40"),
                active=(colors[1]),
                margin_x=0,
                padding=(widget_defaults["padding"]*.5),
            ),
            widget.CurrentLayoutIcon(scale=.6,),
            #widget.Chord(fmt='<b>{}</b>'),

            widget.Spacer(length=bar.STRETCH,**nodecoration_group),

            #widget.WindowName(
            #    fmt='<b>{}</b>',
            #    format='{name}',
            #    #format='{class}',
            #    empty_group_string='Desktop',
            #    #max_chars=20,
            #    parse_text=longNameParse,
            #    #width=widget_defaults["fontsize"]*10,
            #),

            widget.Spacer(length=bar.STRETCH,**nodecoration_group),

            widget.Mpris2(
                format='{xesam:title} - {xesam:artist}',
                objname = "org.mpris.MediaPlayer2.spotify",
                poll_interval=2,
                scroll=True,
                width=(widget_defaults["fontsize"]*15),
            ),
            widget.WidgetBox(widgets=[
                widget.CPU(
                    format=' {freq_current}GHz {load_percent}%',
                    font="SF Mono, Symbols Nerd Font"
                    ), 
                widget.ThermalSensor(tag_sensor="CPUTIN",format=' {temp:3.1f}{unit}'),
                widget.ThermalSensor(tag_sensor="edge",format='󰢮 {temp:3.1f}{unit}'),
                widget.Memory(
                    format=' {MemUsed:.0f}',
                    font="SF Mono, Symbols Nerd Font"
                    ),
                widget.Spacer(length=5),
                ],
                text_closed='󰨚',
                text_open='󰔢',
                close_button_location='right',
            ),
            widget.Syncthing(
                background='#FFFFFF'
            ),
            widget.PulseVolume(
                emoji_list=['󰝟','󰕿', '󰖀', '󰕾'],
                emoji=True,
                mouse_callbacks={"Button3": lazy.spawn("pavucontrol"),},
            ), 
            widget.Wlan(
                    format='󰖩 {percent:3.0%}',
                font="SF Mono, Symbols Nerd Font",
                mouse_callbacks={"Button1": lazy.spawn("iwgtk"),},
            ),
            widget.Clock(
                format='%a %b %d %I:%M %p',
            ),
            #too proud of this one
            #widget.Spacer(length=widget_defaults["padding"]*2),
        ], 
            35, 
            #background=[(colors[0]+"AA")],
            margin=(5,5,0,5),
            background = "#00000000",
        ),
        #bottom=bar.Bar(
        #    [
        #        #widget.Spacer(length=bar.STRETCH,**nodecoration_group),
        #        widget.TaskList(
        #            highlight_method='block',
        #            parse_text=longNameParse,
        #            theme_mode='preferred',
        #            theme_path=('/usr/share/icons/Adwaita'),
        #            border=(colors[1]+"2A"),
        #            center_aligned=True,
        #            ),
        #        #widget.Spacer(length=bar.STRETCH,**nodecoration_group),
        #    ],
        #    35,
        #    background = "#00000000",
        #    margin=(0,5,5,5),
        #),
    )
]
