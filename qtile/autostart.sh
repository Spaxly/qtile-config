#!/bin/sh

feh --bg-fill ~/.config/qtile/wallpapers/aesthetic4k.jpg &
picom --config ~/.config/qtile/picom/picom.conf --experimental-backends --animations &
xsetroot -cursor_name left_ptr &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst -config $HOME/.config/qtile/dunst/dunstrc &
