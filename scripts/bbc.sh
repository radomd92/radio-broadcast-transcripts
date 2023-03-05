#!/bin/bash
if [[ -f /mnt/radio/bbc4/last_pid ]]; then 
    kill $(cat /mnt/radio/bbc4/last_pid)
fi
echo $$ > /mnt/radio/bbc4/last_pid

NOW=$(date +%Y-%m-%d-%Hh%Mm)
STREAM_URL="http://stream.live.vc.bbcmedia.co.uk/bbc_radio_fourfm"
OUTPUT_FILE=/mnt/radio/bbc4/$NOW.mp3
echo $OUTPUT_FILE > /mnt/radio/bbc4/latest

curl -L $STREAM_URL -o - > $OUTPUT_FILE &
echo $! > /mnt/radio/bbc4/last_pid
