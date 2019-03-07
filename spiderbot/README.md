
What Is It?
===========

Spiderbot is a hexapod robot build using an esp8266 and a PCA9686 Adafruit Servo controller.
This code is Micropython code for the Esp to control it.

How Do I use it?
=================

First you need to have micropython Flashed on the Esp8266. Ampy is a good tool to upload files and run them.

You will need the following libraries:

  * micropython-adafruit-pca9685 - servo.py and pca9685.py.
  * https://bitbucket.org/thesheep/micropython-servo/src/f562a6abeaf0e83b752838df7cd31d88ea10b2c7/servo.py?at=default&fileviewer=file-view-default
      * as direct_servo.py with class DServo.
      
Upload these files.

Then upload the spiderbot.py, spiderbot_demo.py and the gait files you want to test.
