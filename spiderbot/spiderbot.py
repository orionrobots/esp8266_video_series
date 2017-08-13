"""Control for the spider bot servo's.
Libraries:
    * micropython-adafruit-pca9685 - servo.py and pca9685.py.
    * https://bitbucket.org/thesheep/micropython-servo/src/f562a6abeaf0e83b752838df7cd31d88ea10b2c7/servo.py?at=default&fileviewer=file-view-default
        * as direct_servo.py with class DServo.
"""
from machine import Pin, I2C
import servo
from direct_servo import DServo

# Todo: Potentially flatten this with the other classes I have the source for.
class Servo9686():
    def __init__(self, adafruit_servos, index):
        self._servos = adafruit_servos
        self._index = index
        self.invert = False

    def position(self, angle):
        if self.invert:
            angle = 180 - angle
        self._servos.position(self._index, angle)
    
    def release(self):
        self._servos.release(self._index)


class ServoDirect():
    def __init__(self, pin):
        self._servo = DServo(pin)
        self.invert = False

    def position(self, angle):
        if self.invert:
            angle = 180 - angle
        self._servo.write_angle(angle)

    def release(self):
        self._servo.write_us(0)


class Robot:
    def __init__(self, i2c):
        s = servo.Servos(i2c)
        servo_list = []
        for n in range(16):
            servo_list.append(Servo9686(s, n))
        servo_list.append(ServoDirect(Pin(0)))
        servo_list.append(ServoDirect(Pin(2)))

        # Set them all to 90 degrees
        for n in range(18):
            servo_list[n].position(90)
        self.servo_list = servo_list


class Leg():
    def __init__(self, robot, hip, knee, foot, invert=False):
        """Hip, Knee and Foot are Servo classes.
        Invert will invert angles on hips and knees"""
        self.hip = robot.servo_list[hip]
        self.knee = robot.servo_list[knee]
        self.foot = robot.servo_list[foot]
        if invert:
            self.hip.invert = True
            self.knee.invert = True

def init():
    """From the front:
            00
    --0--0--0    0--0--0--
    1  0  2    4  3  5
    --0--0--0    0--0--0--
    11 10  9    6  7  8
    --0--0--0    0--0--0--
    14 12 13    17 15 16
    """
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    robot = Robot(i2c)

    left_side = [
        Leg(robot,  2,  0,  1),
        Leg(robot,  9, 10, 11),
        Leg(robot, 13, 12, 14)
    ]

    right_side = [
        Leg(robot, 4, 3, 5, invert=True),
        Leg(robot, 6, 7, 8, invert=True),
        Leg(robot, 17, 15, 16, invert=True)
    ]

    return left_side, right_side
