#!/usr/bin/env bash
set -e -x
pip3 install rshell adafruit-ampy
# wget things

mkdir -p ../deps
pushd ../deps
export FILE_PATH=https://github.com/adafruit/micropython-adafruit-pca9685/raw/master
wget -nc ${FILE_PATH}/pca9685.py
wget -nc ${FILE_PATH}/servo.py
popd

# add files

ampy put ../deps/servo.py servo.py
ampy put ../deps/pca9685.py pca9685.py
ampy put ../web_led/python_web_led/serve.py serve.py
ampy put ../web_led/python_web_led/connect.py connect.py
ampy put ../python_libs/direct_servo.py direct_servo.py
ampy put tweening_control.py tweening_control.py
ampy put spiderbot.py spiderbot.py
ampy put spider_menu.html spider_menu.html 
ampy put spider_serve.py main.py
ampy put crab_gait.py crab_gait.py
ampy put leg_by_leg_gait.py leg_by_leg_gait.py
ampy put ant_gait.py ant_gait.py
ampy ls
