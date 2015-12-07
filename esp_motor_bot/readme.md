# Introduction

This is an esp8266/NodeMCU based robot with 2 wheels that is both inexpensive, and a starting platform for fun and experimentation.

Video: https://www.youtube.com/watch?v=ZYZelug2SW0&feature=youtu.be

# Bill Of Materials

* Robot Chassis - many on ebay as "smart robot chassis". These are extremely cheap, you shouldn't pay more than about £15 for it. It should have:
** The main chassis - some precut perspex.
** 2 motors with wheels - preferably with cables soldered on.
** A front castor.
** All fixing screws.
* It may have:
** Encoder slots and wheels
* If the chassis didn't come with one, you need a 4xAA battery box.
* 4xAA batteries
* SOme sticky tack, or double sided sticky pads.
* A NodeMCU dev board module.
* an L298N motor control module - there are designs that jumper the enable pins so they are pulled up - for the current build, remove this jumper.
* A breadboard (400 point type with voltage rails)
* Some breadboard jump wires - of varying lengths - get a selection of these.
* 8 male to female jump wires with crimped ends.

# Building it

First - remove any backing from the perspex chassis.

If the motors didn't come wired then solder the wires on before the next step.

Bolt the motors onto the chassis.
Fix the wheels onto the motors.
Bolt the castor onto the chassis too.

Looking at the video for reference - lay out the motor control board so the motor cables can reach it.
Put the battery box at one end, and leave room for the breadboard the other.

Screw the motors, and battery cables into the L298N motor controller.

# Wiring the breadboard

Wire the breadboard before sticking it on the chassis. This needs a bit of thought.
Test fit the nodemcu on the breadboard - don't push all the way down. Note down the row numbers for pins d0-d5, vIn and Gnd.
Leaving space for the ESP pins - bring the vIn and round pins to the voltage rails on the board. 
Then wire d1 to d6 to a space on the board, where you will attach it to the motor controller.

Push the NodeMCU board into place. 

Attach the board to the chassis.

Connect the voltage rails to the 5v and ground connections on the L298.
Connect D1, 2, 3 from the ESP to ENA, 1, 2 on the L298.
And
D4, 5, 6 on then ESP to to 3, 4, ENB on the L298.

# Code

If you've not done so, flash the esp8266 with the NodeMCU firmware - I se the NodeMCU Flasher tool.
Get the start code from this project and upload it. Warning - If you've already put batteries in, have a hand ready to catch the robot as it drives off the table!

# Go!

Put the batteries in, and press the reset button to see it move.

# Problems

This first needs a power switch - currently removing a battery is the only way to turn it off.
Also - a few resistors may be needed between the esp and the motor controller. IT was designed for 5v use, and I noticed the esp getting a bit warm - so these could limit current if it's not being particular good with power.
The L298N uses 6 io, with some jumpered designs only needing 4. Other motor controller solutions may need fewer pins - leaving them free for experimenting.

These will be addressed in follow up work.





