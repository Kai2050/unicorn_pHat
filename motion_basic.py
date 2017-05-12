from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
pir = MotionSensor(7)
#camera.rotation = 180
camera.framerate = 30
camera.resolution = (480, 270)
save_path = '/home/pi/vid/'

while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")
    camera.start_recording(filename)
    print("Motion")
    camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    pir.wait_for_no_motion()
    print("Motion stopped")
    camera.stop_recording()
