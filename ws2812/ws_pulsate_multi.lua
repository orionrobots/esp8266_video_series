red = 0
green = 1
blue = 2
purple = 3

pin = 1
leds = 29

--Multi Pulsate
current = 1
current_dir = 4
current_colour = 0

tmr.alarm(0, 20, 1, function() 
    current = current + current_dir
    if current_dir > 0 and current >= 250 then
      current_dir = -4
    elseif current_dir < 0 and current <= 1 then
      current_dir = 4
      current_colour = current_colour + 1
      current_colour = current_colour % 4
    end
    if current_colour == red then
        colour = string.char(current % 255, 0, 0)
    elseif current_colour == green then
        colour = string.char(0, current % 255, 0)
    elseif current_colour == blue then
        colour = string.char(0, 0, current % 255)
    else    
        colour = string.char(current % 255, 0, current % 255)
    end    
    ws2812.writergb(1, colour:rep(leds))
end)


