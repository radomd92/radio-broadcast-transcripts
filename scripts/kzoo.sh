#!/bin/bash
if [[ -f /mnt/radio/kzoo/last_pid ]]; then
    kill $(cat /mnt/radio/kzoo/last_pid)
fi
echo $$ > /mnt/radio/kzoo/last_pid

NOW=$(date +%Y-%m-%d-%Hh%Mm)
STREAM_URL=https://us2.streamingpulse.com/ssl/KZOO
OUTPUT_FILE=/mnt/radio/kzoo/$NOW.mp3
echo $OUTPUT_FILE > /mnt/radio/kzoo/latest

curl -L $STREAM_URL -o - > $OUTPUT_FILE &
echo $! > /mnt/radio/kzoo/last_pid

