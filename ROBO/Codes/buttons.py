#turns open/closed button state
#turns on/off rotation duration light
#manually open/close canopy 
#imports
import RPi.GPIO as GPIO
from time import sleep
from dc_motor import dc_forward, dc_backward
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#assign GPIO pins
openbutton = 16
closebutton = 26
LED = 12

#setup GPIO pins
GPIO.setup(openbutton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(closebutton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

#updating open/closed button state
open_button_state = GPIO.input(openbutton)
close_button_state = GPIO.input(closebutton)

def get_open_button_state():
    """
    returns open button state
    """
    open_button_state = GPIO.input(openbutton)
    sleep(.1)
    return open_button_state
def get_close_button_state():
    """
    returns close button state
    """
    close_button_state = GPIO.input(closebutton)
    sleep(.1)
    return close_button_state
    
def manual_open(rot_dur_sec = 1):
    """
    manually opening the canopy.
    """
    GPIO.output(LED,GPIO.HIGH)
    dc_forward(rot_dur_sec)
    GPIO.output(LED,GPIO.LOW)
    
    
def manual_close(rot_dur_sec = 1):
    """
    manually closing the canopy.
    """
    GPIO.output(LED,GPIO.HIGH)
    dc_backward(rot_dur_sec)
    GPIO.output(LED,GPIO.LOW)
    

