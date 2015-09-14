So far I've found NodeMCU to be the most useful and fun way of getting things done with the esp8266. It is based aorund the Lua language. While I like the idea of Micropython, it is not as well supported for the 8266 yet.


# How do I get NodeMCU Flashed Onto an 8266 with Windows

## Download the image

Node MCU is right here on github at [https://github.com/nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware).
There is a tool for use in Windows NodeMCUFlasher. It can be used to flash other code onto the 8266 as well with other images.
[https://github.com/nodemcu/nodemcu-flasher/blob/master/Win64/Release/ESP8266Flasher.exe](https://github.com/nodemcu/nodemcu-flasher/blob/master/Win64/Release/ESP8266Flasher.exe)

## Find the serial port

ASsuming you have got you esp8266 connected to a computer and powered, first you need to find the Serial port for it. Open up Device Manager (Windows Key, "Device Manager" on windows 8, or start, control panel, device manager).

In device manager, look for COM ports - there should be a new entry there. This COM number is what you will need.

## Find the device in the flasher tool

Start up the flasher above, type in your serial port details - and you should be able to detect an 8266 and flash it. Once this is done - you are ready to go.

