-- Simple ESP Motor robot

-- Function to initialise a motor
-- motor: motor to initialise
function motor_init(motor)
    gpio.mode(motor.enable, gpio.OUTPUT)
    gpio.mode(motor.d0, gpio.OUTPUT)
    gpio.mode(motor.d1, gpio.OUTPUT)
    pwm.setup(motor.enable, 500, 1023)
end
 
-- Function to set motor forward, speed
--   motor - the motor struct (table)
--   speed - 0-1023 - duty cycle
function motor_forward(motor, speed) 
	gpio.write(motor.d0, 1)
	gpio.write(motor.d1, 0)
	pwm.setup(motor.enable, 500, speed)
	pwm.start(motor.enable)
end

-- Function to set motor back, speed
--   motor - the motor struct (table)
--   speed - 0-1023 - duty cycle
function motor_backward(motor, speed) 
	gpio.write(motor.d0, 0)
	gpio.write(motor.d1, 1)
	pwm.setup(motor.enable, 500, speed)
	pwm.start(motor.enable)
end

--Funciton motors off
function motor_stop(motor) 
	pwm.stop(motor.enable)
end

-- Main demo (remember to feed the watch dog!)
local motora = {enable=5, d0=4, d1=3}
local motorb = {enable=6, d0=1, d1=2}

motor_init(motora)
motor_init(motorb)

motor_forward(motora, 1023)
tmr.delay(500000)
motor_stop(motora)
tmr.wdclr()

motor_forward(motorb, 1023)
tmr.delay(500000)
motor_stop(motorb)
tmr.wdclr()

motor_backward(motora, 1023)
tmr.delay(500000)
motor_stop(motora)
tmr.wdclr()

motor_backward(motorb, 1023)
tmr.delay(500000)
motor_stop(motorb)
