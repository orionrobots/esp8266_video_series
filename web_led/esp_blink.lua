-- Config
local pin = 3            --> GPIO0
local value = gpio.LOW
local duration = 1000    --> 1 second

print("Setting up")
-- Initialise the pin
gpio.mode(pin, gpio.OUTPUT)
gpio.write(pin, value)

print("Starting timer")
-- Create an interval
tmr.alarm(0, duration, 1, function ()
    if value == gpio.LOW then
        value = gpio.HIGH
        print("High")
    else
        value = gpio.LOW
        print("Low")
    end

    gpio.write(pin, value)
end)
