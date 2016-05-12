pin = 2
gpio.mode(pin, gpio.OUTPUT)
-- The second parameter here is the frequency
-- most hobby motors use 50. Check your model for specifics.
-- 500 is the duty cycle - 512 is the middle (ish).
pwm.setup(pin, 50,  512)
pwm.start(pin)

tmr.delay(300)
pwm.setduty(pin, 100)
tmr.delay(300)
pwm.setduty(pin, 800)

