from libqtile import bar, hook, pangocffi
from libqtile.utils import send_notification
from libqtile.log_utils import logger
from libqtile.widget import base
from libqtile.lazy import lazy
from screeninfo import get_monitors
#from qtile_extras import widget

'''
PriorityBox() pseudocode
accepts list of widgets, from most to least important
'''

#@hook.subscribe.enter_chord
#@hook.subscribe.leave_chord
#def show_hide_chord(*args):
#    send_notification("qtile", "Started key chord.")
#    qtile.widgets_map["windowclassbox"].toggle()
#    qtile.widgets_map["chordbox"].toggle()
monitorWidth=get_monitors()[0].width
monitorHeight=get_monitors()[0].height

class WindowClass(base._TextBox):
    """Displays the name of the window that currently has focus"""

    defaults = [
        ("for_current_screen", False, "instead of this bars screen use currently active screen"),
        (
            "empty_group_string",
            " ",
            "string to display when no windows are focused on current group",
        ),
        ("format", "{state}{class}", "format of the text"),
        (
            "parse_text",
            None,
            "Function to parse and modify window names. "
            "e.g. function in config that removes excess "
            "strings from window name: "
            "def my_func(text)"
            '    for string in [" - Chromium", " - Firefox"]:'
            '        text = text.replace(string, "")'
            "   return text"
            "then set option parse_text=my_func",
        ),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, **config)
        self.add_defaults(WindowClass.defaults)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        hook.subscribe.client_name_updated(self.hook_response)
        hook.subscribe.focus_change(self.hook_response)
        hook.subscribe.float_change(self.hook_response)
        hook.subscribe.current_screen_change(self.hook_response_current_screen)

    def remove_hooks(self):
        hook.unsubscribe.client_name_updated(self.hook_response)
        hook.unsubscribe.focus_change(self.hook_response)
        hook.unsubscribe.float_change(self.hook_response)
        hook.unsubscribe.current_screen_change(self.hook_response_current_screen)

    def hook_response(self, *args):
        if self.for_current_screen:
            w = self.qtile.current_screen.group.current_window
        else:
            w = self.bar.screen.group.current_window
        state = ""
        if w:
            if w.maximized:
                state = "[] "
            elif w.minimized:
                state = "_ "
            elif w.floating:
                state = "V "
            var = {}
            var["state"] = state
            var["name"] = w.name
            if callable(self.parse_text):
                try:
                    var["name"] = self.parse_text(var["name"])
                except:  # noqa: E722
                    logger.exception("parse_text function failed:")
            wm_class = w.get_wm_class()
            var["class"] = wm_class[-1].capitalize() if wm_class else ""
            unescaped = self.format.format(**var)
        else:
            unescaped = self.empty_group_string
        self.update(pangocffi.markup_escape_text(unescaped))

    def hook_response_current_screen(self, *args):
        if self.for_current_screen:
            self.hook_response()

    def finalize(self):
        self.remove_hooks()
        base._TextBox.finalize(self)

@lazy.function
def increase_gaps(qtile):
    if(qtile.current_layout.margin<50):
        qtile.current_layout.margin += 5
    qtile.current_group.layout_all()
    layout.cmd_reset

@lazy.function
def decrease_gaps(qtile):
    if(qtile.current_layout.margin>0):
        qtile.current_layout.margin -= 5
    qtile.current_group.layout_all()
    layout.cmd_reset
