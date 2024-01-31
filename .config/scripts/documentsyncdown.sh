#!/bin/bash
udisksctl mount -b /dev/sdb1 && notify-send "SYNKPAD" "starting sync" || notify-send "SYNKPAD" "failed to mount"
rsync -ruv /run/media/sam/Synkpad/Documents/College $HOME/Documents &
rsync -ruv /run/media/sam/Synkpad/Documents/wiki $HOME/Documents;
udisksctl unmount -b /dev/sdb1 && notify-send "SYNKPAD" "sync complete!" || notify-send "SYNKPAD" "failed to unmount"
