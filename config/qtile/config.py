import os
import subprocess 

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings.keys import mod, mouse, keys
from settings.layouts import layouts
from settings.rules import floating_layout
from settings.groups import groups
from settings.colors import colors

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=18,
    background = "#1d1d2d",
    foreground=colors['black'],
    padding = 10,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='text',
                    this_current_screen_border = colors['yellow'],
                    active = colors['blue'],
                    background = "#101213",
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground="#101213",
                    background=colors['grey'],
                    padding=0,
                    fontsize = 35,
                    ),
                widget.WindowName(
                    background = colors['grey'],
                    format = "{name}",
                    foreground = colors['fg'],
                    empty_group_string = 'Desktop',
                    width = 400,
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    background=colors['bg'],
                    foreground=colors['grey'],
                    padding=0,
                    fontsize = 35,
                    ),
                widget.Prompt(
                    prompt = "Run:",
                    foreground=colors['cyan']
                    ),
                widget.Spacer(),
                widget.TextBox(
                    text='',
                    foreground=colors['grey'],
                    padding=-15,
                    fontsize=108
                    ),
                widget.CheckUpdates(
                    background=colors['grey'],
                    distro='Arch_checkupdates',
                    display_format = '  {updates}',
                    no_update_string='  0'
                    ),
                 widget.TextBox(
                    text='',
                    background=colors['grey'],
                    foreground=colors['blue'],
                    padding=-15,
                    fontsize=108
                ),
                widget.CurrentLayout(
                    background=colors['blue'],
                ),
                widget.TextBox(
                    text='',
                    background=colors['blue'],
                    foreground=colors['pink'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.CPU(
                    background=colors['pink'],
                    format = '  {load_percent}%'
                    ),
                widget.TextBox(
                    text='',
                    background=colors['pink'],
                    foreground=colors['orange'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.Memory(
                    background=colors['orange'],
                    format='  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                    measure_mem='G'
                        ),
                widget.TextBox(
                    text='',
                    background=colors['orange'],
                    foreground=colors['green'],
                    padding=-15,
                    fontsize=108
                ),
                widget.TextBox(
                    text='墳 ',
                    background=colors['green'],
                    padding=0,
                    ),
                widget.PulseVolume(
                    background=colors['green'],
                    ),
                widget.TextBox(
                    text='',
                    background=colors['green'],
                    foreground=colors['yellow'],
                    padding=-16,
                    fontsize=108
                    ),
                widget.Clock(
                        format='  %I:%M %p',
                        background=colors['yellow'],
                        ),
                widget.Systray(
                    icon_size = 50
                        ),
            ],
            39,
            margin = [9, 9, 9, 9],
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
wmname = "Qtile"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
