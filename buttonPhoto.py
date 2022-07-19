from gpiozero import Button
from picamera import PiCamera
from signal import pause
 
import time
 
camera = PiCamera()
 
def take_picture_with_camera():
 
    image_path = '/home/pi/images/image_%s.jpg' % int(round(time.time() * 1000))
    camera.capture(image_path)
    print('Took photo')
 
button = Button(4)
button.when_pressed = take_picture_with_camera
 
pause()
