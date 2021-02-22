#turns manual light on and off AND returns manual button state
#imports
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#assign GPIO pins
button = 24
LED = 23

#setup GPIO pins
GPIO.setup(button, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

#function definitions
def manual_light_on():
    """
    turns manual light on
    """
    GPIO.output(LED,GPIO.HIGH)

def manual_light_off():
    """
    turns manual light off
    """
    GPIO.output(LED,GPIO.LOW)
    
def get_manual_button_state():
    """
    Returns manual state button
    """
    button_state = GPIO.input(button)
    sleep(.1)
    return button_state
 