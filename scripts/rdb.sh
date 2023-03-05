#!/bin/bash
if [[ -f /mnt/radio/rdb/last_pid ]]; then 
    kill $(cat /mnt/radio/rdb/last_pid)
fi
echo $$ > /mnt/radio/rdb/last_pid

NOW=$(date +%Y-%m-%d-%Hh%Mm)
STREAM_URL="https://onair15.xdevel.com/proxy/radiodonbosco?mp=/;"
OUTPUT_FILE=/mnt/radio/rdb/$NOW.mp3
echo $OUTPUT_FILE > /mnt/radio/rdb/latest

curl -L $STREAM_URL -o - > $OUTPUT_FILE &
echo $! > /mnt/radio/rdb/last_pid
