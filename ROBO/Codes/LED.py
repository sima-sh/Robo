#Turn lights on/off
#imports
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)

#function definitions
def light_on():
    """
    Turns the LED on.
    """
    GPIO.output(6,GPIO.HIGH)
    
def light_off():
    """
    Turns the LED off.
    """
    GPIO.output(6,GPIO.LOW)

