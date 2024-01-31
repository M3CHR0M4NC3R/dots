#!/bin/bash
udisksctl mount -b /dev/sdb1 && notify-send "SYNKPAD" "starting sync" || notify-send "SYNKPAD" "failed to mount"
rsync -ruv $HOME/Documents/College /run/media/sam/Synkpad/Documents/ &
rsync -ruv $HOME/Documents/wiki /run/media/sam/Synkpad/Documents/ &&
udisksctl unmount -b /dev/sdb1 && notify-send "SYNKPAD" "sync complete!" || notify-send "SYNKPAD" "failed to unmount"
