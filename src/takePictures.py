from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview()
for i in range(3):
    sleep(5)
    camera.capture('/home/pi/Pictures/image%s.jpg' % i)
camera.stop_preview()
