import RPi.GPIO as GPIO
import time
import picamera
import datetime  # new

save_directory = "/home/pi/vid/"

def get_file_name():  # new
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

sensor = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

cam = picamera.PiCamera()
cam.resolution = (960, 540)

print("Starting PIR")
time.sleep(1)
print("Ready...")

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        if current_state:
            new_state = "HIGH"
        else:
            new_state = "LOW"

        print("GPIO pin %s is %s at " % (sensor, new_state) + datetime.datetime.now().strftime("%H:%M:%S"))

        if current_state:
            cam.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fileName = "%s%s" % (save_directory, get_file_name())
            cam.start_preview()
            cam.start_recording(fileName)
        else:
            cam.stop_preview()
            cam.stop_recording()  
