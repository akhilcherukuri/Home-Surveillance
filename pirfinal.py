import RPi.GPIO as GPIO
import time
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIP.OUT)

camera = PiCamera()

i=0

while True:
        i+=1
        state = GPIO.input(20)
        if state==0:
		GPIO.output(21, GPIO.LOW)
                print "NO MOTION, CAMERA IDLE!"
                time.sleep(1.0)
        elif state==1:
		GPIO.output(21, GPIO.HIGH)
                print "MOTION DETECTED, PICTURE TAKEN!"
                camera.capture('/home/pi/Pictures/image{0:04d}.jpg'.format(i))
		time.sleep(1.0)