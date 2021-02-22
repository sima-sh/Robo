#manually open/close canopy
#imports
import RPi.GPIO as GPIO #calling header file which helps us use GPIO’s of PI
from time import sleep #calling time to provide delays in program

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
                            
#assign GPIO pins
in1_pin = 17
in2_pin = 27
pwm_pin = 18
frequency = 10 # Hz
duty_cycle = 20 # Percent

#setup GPIO pins
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

#generate PWM signal with 0% duty cycle
pwm = GPIO.PWM(pwm_pin, frequency)
pwm.start(duty_cycle)

GPIO.output(in1_pin, False)
GPIO.output(in2_pin, False)

#function definitions
def dc_forward(rot_dur_sec = 1):
    """
    Rotates motor forward for rot_dur_sec amout of time.
    """
    GPIO.output(in1_pin, False)    
    GPIO.output(in2_pin, True)
    print("Opening the canopy ...")
    sleep(rot_dur_sec)
    print("Done!")
    GPIO.output(in2_pin, False)
    
def dc_backward(rot_dur_sec = 1):
    """
    Rotates motor backward for rot_dur_sec amout of time.
    """
    GPIO.output(in1_pin, True)    
    GPIO.output(in2_pin, False)
    print("Closing the canopy ...")
    sleep(rot_dur_sec)
    print("Done!")
    GPIO.output(in1_pin, False)

    