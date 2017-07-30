"""Using a WS2801 LED strip (spi) as a servo motor controller"""
from machine import Pin, SPI
from time import sleep

# setup
clock = Pin(5)
mosi = Pin(4) # Out
miso = Pin(2) # In - a dummy here
# Presume the -1 means hware here.
spi = SPI(-1, baudrate=100000, sck=clock, mosi=mosi, miso=miso)
spi.init()

# Loop
def sweep(waitsec):
    for n in range(255):
        spi.write(bytes([n]*3))
        sleep(waitsec)
    for n in range(255, 0, -1):
        spi.write(bytes([n]*3))
        sleep(waitsec)

 
