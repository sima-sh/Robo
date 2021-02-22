#importing all necessary functions
from rain_sensor import is_rainy
from LED import light_on, light_off
from dc_motor import dc_forward, dc_backward
from light_sensor import is_day
from buttons import manual_open, manual_close, get_open_button_state, get_close_button_state
from manual import get_manual_button_state, manual_light_on, manual_light_off

#define variables
ROT_DUR = 9
canopy_closed = True
is_manual= False
old_button_state = 1

#program starts here
while True:
    try:
        # Listening for manual button status and setting is_manual accordingly
        button_state = get_manual_button_state()
        if old_button_state==1 and button_state == 0 and not is_manual:
            print('manual is on')
            manual_light_on()
            is_manual = True
        elif old_button_state==1 and button_state == 0 and is_manual:
            print('automatic is on')
            manual_light_off()
            is_manual = False
        old_button_state = button_state
        ##################################
        
        #manual mode
        #listening for close/open button state and manual open/manual close accordingly
        if is_manual:
            print("it is manual now.")
            open_button_state = get_open_button_state()
            close_button_state = get_close_button_state()
            if canopy_closed and open_button_state == 0:
                print("Opening canopy manually...")
                manual_open(ROT_DUR)
                canopy_closed = False
            elif not canopy_closed and close_button_state == 0:
                print("closing canopy manually...")
                manual_close(ROT_DUR)
                canopy_closed = True
                ##################################
                
                # In automatic mode
                #listens for is_day and is_rainy status and open/close canopy accordingly
        else:
            if is_day() and not is_rainy():
                # Close the Pergola if not already closed
                if not canopy_closed:
                    dc_backward(ROT_DUR)
                    canopy_closed = True
                    # Turn off the balcony lights
                    light_off()

            elif is_day() and is_rainy():
                # Open the Pergola if not already open
                if canopy_closed:
                    print('it is rainy')
                    dc_forward(ROT_DUR)
                    canopy_closed = False
                    
            else:
                # Open the Pergola if not already open
                if canopy_closed:
                    dc_forward(ROT_DUR)
                    canopy_closed = False
                    # Turn on the baclony lights
                    light_on()
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")    

    
