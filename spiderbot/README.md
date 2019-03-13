
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

# Upload files:

../web_led/python_web_led/serve.py
../web_led/python_web_led/connect.py
spiderbot.py
spider_menu.py
spider_serve.py
crab_grait.py
leg_by_leg_gait.py

## Notes on server

* Generator/coroutines  
  * https://stackoverflow.com/questions/12637768/python-3-send-method-of-generators
  * https://docs.python.org/3/library/asyncio-task.html
  * https://www.youtube.com/watch?v=tIgu7q38bUw&feature=youtu.be
  * https://stackoverflow.com/questions/21622193/python-3-2-coroutine-attributeerror-generator-object-has-no-attribute-next/21622696
  * https://forum.micropython.org/viewtopic.php?t=4234
  