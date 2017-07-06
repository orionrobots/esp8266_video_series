-- Config
local read_xy = 5
local duration = 50    --> In milis

-- Initialise the pins
function init_joystick( read_xy )
    gpio.mode(read_xy, gpio.OUTPUT)
    gpio.write(read_xy, gpio.LOW)
end

function read_joystick( read_xy )
    gpio.write(read_xy, gpio.HIGH)
    local x = adc.read(0)
    gpio.write(read_xy, gpio.LOW)
    local y = adc.read(0)
    return {x, y}
end

print("Setting up")
init_joystick(read_xy)

-- Create an interval

tmr.alarm(0, duration, 1, function () 
    local pos = read_joystick(read_xy)
    print("X is", pos[1], "Y is ", pos[2])
end)
