#!/bin/sh
exec > $HOME/tmp/xkeysnal.log 2>&1
xhost +SI:localuser:xkeysnail
sudo -u xkeysnail DISPLAY=$DISPLAY /usr/local/bin/xkeysnail /etc/opt/xkeysnail/config.py &
