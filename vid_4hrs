#!/usr/bin/env python

from picamera import PiCamera
import time
import datetime

camera = PiCamera()
camera.rotation = 180
camera.led = False
camera.framerate = 25
camera.resolution = (960, 540)
save_dir = "/home/pi/vid/"
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for i in range(48):
    def get_file_name():
      return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    filename = "%s%s" % (save_dir, get_file_name()) 
    print("4 hours recording starting now")
    time.sleep(1)
    print("Starting to record 5 minutes at %s" % (time_now))
    camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.start_preview()
    camera.start_recording(filename) 
    time.sleep(300)
    camera.stop_recording()
    camera.stop_preview()
    print("Finished recording")
