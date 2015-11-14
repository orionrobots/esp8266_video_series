-- Note - this is not intended to run as a complete program - these are snippets
-- for experimentation - blocks to run in Esplorer and demonstrate the panel.

white = string.char(255, 255, 255)
off = string.char(0,0,0)
blue=string.char(0, 0, 255)
pink=string.char(255, 0, 255)
purple=string.char(20, 0, 20)
red =string.char(100, 0, 0)
green =string.char(0, 100, 0)
yellow =string.char(100, 100, 0)
gold =string.char(180, 100, 0)
silver = string.char(60, 60, 100)
orange = string.char(255/4,127/4,0)
violet = string.char(138,43,226)
indigo = string.char(75,0,130)


rainbow_line = (red..orange..yellow..green..blue..indigo..violet..gold)
ws2812.writergb(1, rainbow_line:rep(8))

ws2812.writergb(1, white:rep(64))
ws2812.writergb(1, off:rep(64))
ws2812.writergb(1, blue:rep(64))
ws2812.writergb(1, purple:rep(64))
ws2812.writergb(1, red:rep(64))
ws2812.writergb(1, green:rep(64))
ws2812.writergb(1, gold:rep(64))
ws2812.writergb(1, silver:rep(64))

stripes = (red:rep(8)..blue:rep(8)
  ..red:rep(8)..green:rep(8)
  ..red:rep(8)..purple:rep(8)
  ..red:rep(8)..gold:rep(8))
  
ws2812.writergb(1, stripes)

-- Drawing a letter H
w = white
b = off
letter_h = (b..w..b..b..b..b..w..b
          ..b..w..b..b..b..b..w..b
          ..b..w..b..b..b..b..w..b
          ..b..w..b..b..b..b..w..b
          ..b..w..w..w..w..w..w..b
          ..b..w..b..b..b..b..w..b
          ..b..w..b..b..b..b..w..b
          ..b..w..b..b..b..b..w..b)
ws2812.writergb(1, letter_h)

-- Letter J

letter_j = (b..b..b..b..b..w..w..w          
          ..b..b..b..b..b..b..w..b
          ..b..b..b..b..b..b..w..b
          ..b..b..b..b..b..b..w..b
          ..b..b..b..b..b..b..w..b
          ..b..b..b..b..b..b..w..b
          ..b..b..b..w..b..w..b..b
          ..b..b..b..b..w..b..b..b)
ws2812.writergb(1, letter_j:gsub(w, blue))

-- Word Jo

word_jo =  (w..w..w..b..b..b..b..b         
          ..b..w..b..b..b..b..b..b
          ..b..w..b..b..b..b..b..b
          ..b..w..b..b..b..w..b..b
          ..b..w..b..b..w..b..w..b
          ..b..w..b..b..w..b..w..b
          ..w..b..b..b..b..w..b..b
          ..b..b..b..b..b..b..b..b
          )
ws2812.writergb(1, word_jo:gsub(b, green))