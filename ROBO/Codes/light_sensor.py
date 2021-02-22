#Return True if it is day, Returns false if it is night
#imports
import time
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

#import module from library
import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()

#function definitions
def is_day():
    """
    checks if it is day
    """
    lux = sensor.Lux
    print ('Lux: %d'%lux)
    if lux>10:
        return True
    else:
        return False



