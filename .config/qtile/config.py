from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import send_notification
from libqtile import hook
from qtile_extras import widget

'''bar import'''
from macstylebar import widget_defaults, extension_defaults, screens

import os
import subprocess
'''
  █████  ▄▄▄█████▓ ██▓ ██▓    ▓█████     ▄████▄   ▒█████   ███▄    █   █████▒██▓  ▄████
▒██▓  ██▒▓  ██▒ ▓▒▓██▒▓██▒    ▓█   ▀    ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▓██   ▒▓██▒ ██▒ ▀█▒
▒██▒  ██░▒ ▓██░ ▒░▒██▒▒██░    ▒███      ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒████ ░▒██▒▒██░▄▄▄░
░██  █▀ ░░ ▓██▓ ░ ░██░▒██░    ▒▓█  ▄    ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█▒  ░░██░░▓█  ██▓
░▒███▒█▄   ▒██▒ ░ ░██░░██████▒░▒████▒   ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒█░   ░██░░▒▓███▀▒
░░ ▒▒░ ▒   ▒ ░░   ░▓  ░ ▒░▓  ░░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒ ░   ░▓   ░▒   ▒
 ░ ▒░  ░     ░     ▒ ░░ ░ ▒  ░ ░ ░  ░     ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░ ░      ▒ ░  ░   ░
   ░   ░   ░       ▒ ░  ░ ░      ░      ░        ░ ░ ░ ▒     ░   ░ ░  ░ ░    ▒ ░░ ░   ░
    ░              ░      ░  ░   ░  ░   ░ ░          ░ ░           ░         ░        ░
                                        ░
'''                                     

home = "/home/"+os.getlogin()
#wal color support
colors = []
cache=home+'/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

'''keybinds
 ██ ▄█▀▓█████▓██   ██▓ ▄▄▄▄    ██▓ ███▄    █ ▓█████▄   ██████
 ██▄█▒ ▓█   ▀ ▒██  ██▒▓█████▄ ▓██▒ ██ ▀█   █ ▒██▀ ██▌▒██    ▒
▓███▄░ ▒███    ▒██ ██░▒██▒ ▄██▒██▒▓██  ▀█ ██▒░██   █▌░ ▓██▄
▓██ █▄ ▒▓█  ▄  ░ ▐██▓░▒██░█▀  ░██░▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒
▒██▒ █▄░▒████▒ ░ ██▒▓░░▓█  ▀█▓░██░▒██░   ▓██░░▒████▓ ▒██████▒▒
▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ░▒▓███▀▒░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ▒░▒   ░  ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░
░ ░░ ░    ░   ▒ ▒ ░░   ░    ░  ▒ ░   ░   ░ ░  ░ ░  ░ ░  ░  ░
░  ░      ░  ░░ ░      ░       ░           ░    ░          ░
              ░ ░           ░                 ░
'''
mod = "mod4"
terminal = "alacritty"

#this string is for opening apps inside a terminal and loading colors first
#ranger etc when opened from qtile will skip reading xResources etc
def terminalOpen(application):
    return terminal + " -e " + application
email = "thunderbird"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "o", lazy.window.toggle_floating()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "y", lazy.next_layout(), desc="Toggle between layouts"),
    #bind changed to mimick pop-os
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    #Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "p", lazy.spawn(home+"/.config/scripts/rofi-power.sh"), desc="Pull up power menu"),
    Key([mod], "x", lazy.hide_show_bar("bottom"), desc="Toggle taskbar"),

    #move left and right between groups
    Key([mod, "control"], "left", lazy.screen.prev_group(), desc="previous workspace"),
    Key([mod, "control"], "right", lazy.screen.next_group(), desc="next workspace"),

    #application shortcuts
    Key([mod], "w", lazy.spawn("firefox"), desc="Summon web browser"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Summon terminal"),
    Key([mod], "e", lazy.spawn(email), desc="Summon email client"),
    Key([mod], "s", lazy.spawn("spotify-launcher"), desc="Summon Spotify"),
    Key([mod], "Space", lazy.spawn("rofi -show drun"), desc="Summon rofi"),
    Key([mod], "Tab", lazy.spawn(home+"/.config/scripts/SuperTab.sh"), desc="Windows/MacOS window switcher"),
    Key([mod, "control"], "Space", lazy.spawn("rofi -modi emoji -show emoji"), desc="Summon rofi emoji menu"),
    Key([mod, "control"], "m", lazy.spawn(home+"/.config/scripts/rofi-radio.sh"), desc="Summon rofi radio"),
    Key([mod], "p", lazy.spawn(terminalOpen("btop")), desc="Summon rofi"),
    Key([mod], "b", lazy.spawn(terminalOpen("bluetuith")), desc="Summon bluetuith"),
    Key([mod], "t", lazy.spawn(home+"/.config/scripts/wpgThemeMenu.sh"), desc="Summon theme menu"),

    #file browsers
    KeyChord([mod], "f", [
        Key([], "f", lazy.spawn(terminalOpen("ranger")), desc="Summon ranger"),
        Key([], "g", lazy.spawn("pcmanfm"), desc="Summon pcmanfm"),
        Key([], "s", lazy.spawn(home+"/.config/scripts/fileSearch.sh"), desc="Summon a file search"),
        ],
        #mode=True,
        name="File Browsers",
    ),

    #vim apps
    KeyChord([mod], "v", [
        Key([], "v", lazy.spawn(terminalOpen("vim"))),
        Key([], "w", lazy.spawn(terminalOpen("vim " + home + "/Documents/wiki/index.wiki"))),
        Key([], "e", lazy.spawn(terminalOpen("vim +Calendar"))),
        Key([], "c", lazy.spawn(terminalOpen("vim " + home + "/.config/qtile/config.py"))),
        ],
        name="Vim"
    ),
    #Take a screenshot
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Summon flameshot"),
    Key(["control"], "Print", lazy.spawn("scrot"), desc="Summon flameshot"),

    #brightness keys
    Key([], "XF86MonBrightnessUp", lazy.spawn(home + "/.config/scripts/brightness.sh up"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(home + "/.config/scripts/brightness.sh down"), desc="Brightness down"),
    #additional keybind for desktop
    Key([mod], "up", lazy.spawn(home + "/.config/scripts/brightness.sh up"), desc="Brightness up"),
    Key([mod], "down", lazy.spawn(home + "/.config/scripts/brightness.sh down"), desc="Brightness down"),

    #volume keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn(home + "/.config/scripts/volume.sh up"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(home + "/.config/scripts/volume.sh down"), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn(home + "/.config/scripts/volume.sh mute"), desc="Volume mute"),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Pause media"),
    #keybind for hhkb, I know this bind sucks, bite me
    Key([mod], "d", lazy.spawn("playerctl play-pause"), desc="Pause media"),

    Key([], "XF86AudioPause", lazy.spawn("pactlrctl play-pause"), desc="Play media"),
    Key([], "XF86AudioNext", lazy.spawn("pactlrctl next"), desc="skip media"),
    Key([], "XF86AudioPrev", lazy.spawn("pactlrctl previous"), desc="rewind media"),
    Key([], "XF86AudioStop", lazy.spawn("pactlrctl stop"), desc="stop media"),
]
@hook.subscribe.startup_once
def autostart_once():
    startupscript = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([startupscript])

#start with taskbar hidden
#@hook.subscribe.startup
#def startup():
#    bottom.show(False)

'''groups
  ▄████  ██▀███   ▒█████   █    ██  ██▓███    ██████ 
 ██▒ ▀█▒▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██▒▒██    ▒ 
▒██░▄▄▄░▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒░ ▓██▄   
░▓█  ██▓▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒  ▒   ██▒
░▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░▒██████▒▒
 ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░
  ░   ░   ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░     ░ ░▒  ░ ░
░ ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░       ░  ░  ░  
      ░    ░         ░ ░     ░                    ░  
'''
groups=[
    Group(i, label="") for i in "1234567"
]
#groups.append(Group("6", matches=[Match(wm_class="spotify")], persist=False, init=True, label=""))
#groups.append(Group("7", matches=[Match(wm_class="discord")], persist=False, init=True, label="󰙯"))
#groups.append(Group("8", matches=[Match(wm_class="thunderbird")], persist=False, init=True, label="󰛮"))

group_labels = ["","","","","󰙯","6","7"]
#for i in range(len(group_labels)):
#    groups.append(
#            Group(
#                name=i+1,
#                label=group_labels[i],
#            )
#    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
'''layouts
 ██▓    ▄▄▄     ▓██   ██▓ ▒█████   █    ██ ▄▄▄█████▓  ██████ 
▓██▒   ▒████▄    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▒██    ▒ 
▒██░   ▒██  ▀█▄   ▒██ ██░▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░░ ▓██▄   
▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒██   ██░▓▓█  ░██░░ ▓██▓ ░   ▒   ██▒
░██████▒▓█   ▓██▒ ░ ██▒▓░░ ████▓▒░▒▒█████▓   ▒██▒ ░ ▒██████▒▒
░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ▒ ▒▓▒ ▒ ░
░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░    ░ ░▒  ░ ░
  ░ ░    ░   ▒   ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░   ░      ░  ░  ░  
    ░  ░     ░  ░░ ░         ░ ░     ░                    ░  
                 ░ ░                                        
'''
layouts = [
    layout.MonadTall(
        border_focus=colors[1],
        border_normal=colors[8],
        border_width=3,
        margin=5
        ),
    layout.Columns(
        border_focus=colors[1],
        border_normal=colors[8],
        border_width=3,
        margin=5
        ),
    layout.Floating(
        border_focus=colors[7],
        border_normal=colors[1],
        border_width=0
        ),
]

def getMargin():
    #we gonna try to return the margins set with this
    from libqtile import qtile
    return qtile.current_layout.name
def getTerminal():
    print(terminal)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "QTile"
