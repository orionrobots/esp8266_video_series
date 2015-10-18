These are steps taken in my [web LED 8266 video series](http://orionrobots.co.uk/2015/06/10/esp-8266-wifi-led/).


# Getting this running

The steps in brief (details below):

* Build the circuit
* Flash the device with Node MCU
* Play with that a bit! (there should always be play)
* setup your wifi details
* Use the nodemcu tools to upload the blinking led example and try it.
* Use the nodemcu tools to upload the hello_world_server.lua and try it.
* Use the nodemcu tools to upload the web page html.
* Use the nodemcu tools to upload the led_server.lua and try this.

# Bill of Materials

* Small breadboard (301 pin pictured, but any will do)
* esp8266 - the circuits shown are the esp-01. If you know electronics, you can use any of the esp modules here.
* Red LED (for power, during testing - you can remove later)
* Green LED (for controllable - you can swap these when you want)
* 2 x 100 Ohm resistors (R1, R2)
* 1 x 10k Ohm resistor (R3)
* 1 x 3.3uF Electrolytic Capacitor
* 1 x LD33V (or LD1117v33) 3.3v regulator
* A bunch of jump wires - single core stiff wire for breadboarding.
* 8 male to female prototyping cables.

* A 6v battery box - thats 4 x AA.

# Tools

* A Computer
* A serial adaptor - I used a USB to TTL adaptor not based on an FTDI.
* Pair of needle-nosed pliers - optional, but helps to make bends in component legs.

# Build the circuit

There are 3 parts to the circuit. 

![}(https://github.com/orionrobots/esp8266_video_series/raw/master/fritzing%20circuits/RemoteLedControl_bb.svg)

The first is the power supply - the esp needs 3.3v. The LD33V with a filter cap will give a clean 3.3v from 5v or above. The serial cable will have a 5v output, and the battery box 6v. 
Do not connect both at the same time as you may damage your computer.
The middle pin is the output voltage, and looking at it so the metal tab is at the back, the leftmost pin is ground, with voltage in on the right.
The capacitor muust be connected across ground and the 3.3v out. Since it is electrolytic and polarised, make sure the marked leg goes into ground.
It is good practice to connect these out to the breadboard top and bottom rails - so one is 3.3v volts, and the other rail ground.

Next is the serial input. This needs an area with 6 clear columns on the breadboard. 

First build [the circuit](../fritzing_circuits/RemoteLedControl.fzz). Note here that you 
