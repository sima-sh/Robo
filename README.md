The hardware components used in this project are as follows:
- Raspberry Pi4 (RPi)
- TSL25911FN QCrobot light sensor
- HiLetgo LM393 Rain Drops Sensor
- TT dc 6v motor
- Rack and pinion system
- A breadboard, LED lights, push buttons, and jumper wires
- Material and equipment to make the physical model

Module Testing
Before putting the modules together, each one of the modules should be working separately. Below are the ways modules can be tested:
Test Description	                                  Expected Result
1 Manual button is pressed	                        The test LED is turns on
2 Manual button is pressed when test LED is on	        The test LED turns off
3 Blocking the Light sensor 	                        The lux value is lower than 10
4 Light sensor in bright room	                        The lux value is more than 10
5 Dripping water on Raindrop sensor board	        The DO value is low
6 Drying water off the Raindrop sensor board	        The DO value is high
1 DC motor driver in dark room	                        DC motor rotates forward
2 DC motor driver in bright room	                DC motor rotates backward
3 LED in dark room 	                                Turns on 
4 LED in bright room 	                                Turns off
5 Open Push button	                                Lights up a test LED
6 Close Push button	                                Lights up a test LED
