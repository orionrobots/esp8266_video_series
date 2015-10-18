pin = 1
leds = 29

--Pulsate
current = 1
current_dir = 4

tmr.alarm(0, 20, 1, function() 
    current = current + current_dir
    if current_dir > 0 and current >= 250 then
      current_dir = -4
    elseif current_dir < 0 and current <= 1 then
      current_dir = 4
    end
    colour = string.char(current % 255, 0, 0)
    ws2812.writergb(1, colour:rep(leds))
end)


