"""Control for the spider bot servo's."""
from machine import Pin, I2C
import servo # adafruit serves
from direct_servo import DServo
from time import sleep


class Servo9686:
    __slots__ = ['_servo', '_index', 'invert']
    def __init__(self, adafruit_servo, index):
        self._servo = adafruit_servo
        self._index = index
        self.invert = False

    def position(self, angle):
        if self.invert:
            angle = 180 - angle
        self._servo.position(self._index, angle)

    def release(self):
        self._servo.release(self._index)


class ServoDirect:
    __slots__ = ['_servo', 'invert']
    def __init__(self, pin):
        self._servo = DServo(pin)
        self.invert = False

    def position(self, angle):
        if self.invert:
            angle = 180 - angle
        self._servo.write_angle(angle)

    def release(self):
        self._servo.write_us(0)


class Leg():
    __slots__ = ['hip', 'knee', 'foot']

    def __init__(self, robot, hip, knee, foot, invert=False):
        """Hip, Knee and Foot are Servo classes.
        Invert will invert angles on hips and knees"""
        self.hip = robot.servo_list[hip]
        self.knee = robot.servo_list[knee]
        self.foot = robot.servo_list[foot]
        if invert:
            self.hip.invert = True
            self.knee.invert = True
            self.foot.invert = True


class ScalingLegGroup:
    def __init__(self, legs, scale_indexes):
        self.legs = legs
        self.scale_indexes = scale_indexes
        self.scales = (1.0, 1.0)

    def set_scale(self, left, right):
        self.scales = (left, right)

    def get_scale(self, index):
        return self.scales[self.scale_indexes[index]]

    def iter(self):
        return ((self.get_scale(n), leg) for n, leg in enumerate(self.legs))

    def move(self, knee=None, hip=None, foot=None, delay=None):
        for hip_scale, leg in self.iter():
            if foot is not None:
                leg.foot.position(90 + foot)
            if knee is not None:
                leg.knee.position(90 + knee)
            if hip is not None:
                position = 90 + int(hip * hip_scale)
                leg.hip.position(position)
        if delay:
            sleep(delay)


class Robot:
    def __init__(self, i2c):
        """From the front:
                   00
           --0--0--0    0--0--0--
             1  0  2    4  3  5
           --0--0--0    0--0--0--
            11 10  9    6  7  8
           --0--0--0    0--0--0--
            14 12 13    17 15 16
           """
        s = servo.Servos(i2c)
        servo_list = [Servo9686(s, n) for n in range(16)]
        servo_list.append(ServoDirect(Pin(0)))
        servo_list.append(ServoDirect(Pin(2)))

        # Set them all to 90 degrees
        [servo_list[n].position(90) for n in range(18)]
        self.servo_list = servo_list

        self.left_side = [
            Leg(self, 2, 0, 1),
            Leg(self, 9, 10, 11),
            Leg(self, 13, 12, 14)
        ]

        self.right_side = [
            Leg(self, 4, 3, 5, invert=True),
            Leg(self, 6, 7, 8, invert=True),
            Leg(self, 17, 15, 16, invert=True)
        ]

        self.group1 = ScalingLegGroup(
            [self.left_side[0], self.right_side[1], self.left_side[2]],
            [0, 1, 0]
        )
        self.group2 = ScalingLegGroup(
            [self.right_side[0], self.left_side[1], self.right_side[2]],
            [0, 1, 0]
        )

    def neutral(self, release=True):
        for leg in self.left_side:
            leg.knee.position(90)
            leg.foot.position(90)
            leg.hip.position(90)
        for leg in self.right_side:
            leg.knee.position(90)
            leg.foot.position(90)
            leg.hip.position(90)
        if release:
            sleep(0.1)
            for leg in self.left_side:
                leg.knee.release()
                leg.foot.release()
                leg.hip.release()
            for leg in self.right_side:
                leg.knee.release()
                leg.foot.release()
                leg.hip.release()

    def crouch(self):
        self.neutral()
        for leg in self.left_side:
            leg.knee.position(30)
        for leg in self.right_side:
            leg.knee.position(30)
        sleep(0.1)
        for leg in self.left_side:
            leg.knee.release()
        for leg in self.right_side:
            leg.knee.release()



def init():
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    return Robot(i2c)
