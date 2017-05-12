#!/bin/bash
# Script to start our application
echo "VLC Steam..."

raspivid -o - -t 0 -n -w 640 -h 480 \
-rot 0 -ex night \
| cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
