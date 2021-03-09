How to make a ROBO

Robo is a 1/50 scale physical model prototype empowered by a RPi4. The same microcontroller can be used for a scale model.

1. Prerequisite
Skills that are needed for this project are as follows: 
• Be able to python programming,
• Be aware of basic Linux,
• Be able to make physical model,
• Be aware of electrical wiring and circuit,

2. Hardware Setup
Sensors and actuators used in this project are:

• Raspberry Pi4,
• TSL25911FN QCrobot light sensor,
• HiLetgo LM393 Rain Drops Sensor,
• DC TT 6V motors,
• Pinion and bracket gears
• LED lights and push buttons,
• Model making material and equipment


4. Robo moves in three scenarios: 

1. Closes when it is day:
When lux (unit of illumination) is equal or more than 10
2. Opens when it is night, LED in balcony turns on:
When lux (unit of illumination) is less than 10
3. Opens when it is rainy or snowy 
When raindrop sensor detects water drop, regardless of lux amount


5.Python programming:
Program starts assuming automatic mode is on and Robo is open, if manual button is pressed at any time after program is run, program goes to manual mode and can be controlled by open or closed push buttons. There are six modules that will be imported to create the main file:

• Manual: Turns manual mode On and OFF
• Buttons: manually opens or closes with buttons
• Light_sensor: detects if it is day or night
• Rain_sensor: detects if it is rainy 
• Dc_motor: rotates the motor backward and forward
• LED: Turn the night lights on


5.1. Manual
Manual module turns manual mode on and off. It turns on a blue LED when the manual mode is on:
• When manual_button is pressed and blue LED is already off, manual mode turns on.
• When manual_button is pressed and blue LED is already on, automatic mode turns on.

5.2. Buttons
This module opens and closes manually, using two push buttons:
• Open_button checks if the canopy is already closed and if yes, it opens the canopy and turns the lights on.  
• Close_button checks if the canopy is already open and if yes, it closes the canopy and turns the lights off. 

5.3. Light sensor 
Light sensor and waveshare_TSL2591 checks the lux (unit of illumination) and detects if it is day or night. If outdoor light level is 10 lux or more it is detected as day. Here are the requirements for assembling the circuit for this sensor:
• CQRobot Ambient Light Sensor Built-in TSL25911FN chip 
• Jumper wire (F-M and M-M DuPont connectors) 

5.4. Raindrop sensor
This module detects if there is a water drop on the raindrop sensing board. A large drop of water that spans 3 lines of copper on the raindrop detection board is enough to trigger the detection of rainfall. Adjusting the potentiometer will change the sensitivity of the digital trigger. DO is HIGH when the sensor is dry and LOW when triggered. Here are the requirements for assembling this sensor:
• HiLetgo 3pcs LM393 Rain Drops Sensing board 
• Control board
• Jumper wire (F-F DuPont connectors) 

5.4. DC motor
This module rotates the motor forward and backward. This motion results in opening and closing the Robo respectively. The variable pulse width modulation named pwm is defined for adjusting the rotation speed. Controlling the speed is important for testing the mechanical part of the physical prototype. Rotation takes a specified amount of time that is defined in the module and can be edited. Here are the requirements for setting up the dc-motor:

• L293 or SN755410 motor driver chip 
• One DC TT 6V motor
• 4x AA batteries 
• Jumper wire (F-F DuPont connectors) 
	
5.5. LED
This module turn on/off the LED located in the balconies of prototype. Here are the requirements for setting the hardware up:
• LED
• 330 Ω resistor
• Jumper wire (M-F DuPont connectors) 

6. module testing
Before putting the modules together, each one of the modules should be working separately. Below are the ways modules can be tested:
# Test Description	                                Expected Result
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

7. writing the main 
Main file can be written by importing the modules one by one. It would be necessary to test if the module is still working after getting imported in the main. After importing all the necessary modules into the main and defining a few variables, the program starts in a while loop. It starts assuming Robo is closed and manual mode is off. Program includes three chunks of code:
• It checks if manual mode is on or off. 
• If manual mode is on it opens or closes Robo manually.
• If manual mode is off it opens or closes Robo automatically. 
