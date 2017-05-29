-- Config
local read_x = 5
local read_y = 6
local duration = 500    --> In milis

-- Initialise the pins
function init_joystick( read_x, read_y )
    gpio.mode(read_x, gpio.OUTPUT)
    gpio.mode(read_y, gpio.OUTPUT)
    gpio.write(read_x, gpio.LOW)
    gpio.write(read_y, gpio.LOW)
end

function read_joystick( read_x, read_y )
    gpio.write(read_x, gpio.HIGH)
    local x = adc.read(0)
    gpio.write(read_x, gpio.LOW)
    gpio.write(read_y, gpio.HIGH)
    local y = adc.read(0)
    gpio.write(read_y, gpio.LOW)
    return {x, y}
end

print("Setting up")
init_joystick(read_x, read_y)
-- Create an interval
tmr.alarm(0, duration, 1, function () 
    local pos = read_joystick(read_x, read_y)
    print("X is", pos[1], "Y is ", pos[2])
end)
