#!/bin/bash
#calls the lock script after a time

time=${1:-10}
notify=${2:-30}
echo $1 $2
exec xautolock -time $time -notify $notify -locker "~/.config/awesome/scripts/lock.sh" -notifier "notify-send 'screen will be locked soon'" -corners -000 -detectsleep
