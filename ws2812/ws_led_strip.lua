
white = string.char(255, 255, 255)
red = string.char(255, 0, 0)
green = string.char(0, 255, 0)
blue = string.char(0, 0, 255)
off = string.char (0, 0, 0)
purple = string.char(60, 0, 60)
yellow = string.char(60, 60, 0)

ws2812.writergb(1, red..green..blue..purple..white..off:rep(29))
tmr.delay(10000)
ws2812.writergb(1, off:rep(29))
tmr.delay(10000)

pin = 1
leds = 64


current = 1
current_dir = 1
current_seq = red..blue..green..purple
yellow_cur = leds
yellow_dir = -1
tmr.alarm(0, 100, 1, function() 
    current = current + current_dir
    if current_dir == 1 and current >= leds-3 then
      current_dir = -1
    elseif current_dir == -1 and current <= 1 then
      current_dir = 1
    end
    yellow_cur = leds - current
    if yellow_cur > current then
        dist = yellow_cur - current - 4
        ws2812.writergb(1, off:rep(current-1)..current_seq..off:rep(dist)..yellow..off:rep(leds))
    elseif yellow_cur < current then
        dist = current - yellow_cur
        ws2812.writergb(1, off:rep(yellow_cur-1)..yellow..off:rep(dist)..current_seq..off:rep(leds))
    else 
        ws2812.writergb(1, off:rep(current-1)..current_seq..off:rep(leds))
    end
end)


