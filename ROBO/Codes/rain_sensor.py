#Return True if it is rainy, Returns false if it not rainy
#imports
from time import sleep
from gpiozero import Buzzer, InputDevice
 
# raindrop sensor DO connected to GPIO21
no_rain = InputDevice(21)

#function definitions 
def is_rainy():
    """
    checks if it is rainy
    """
    if not no_rain.is_active:
        return True
    else:
        return False
