-- my wifi setup
wifi.setmode(wifi.STATION)  
wifi.sta.config("ssid","password")
print(wifi.sta.getip())

dofile("led_server.lua")

