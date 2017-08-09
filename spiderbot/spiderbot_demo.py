from math import sin, radians
from time import sleep
from spiderbot import Robot, Leg
from machine import Pin, I2C

"""From the front:
           00
 --0--0--0    0--0--0--
   2  1  0    4  3  5
 --0--0--0    0--0--0--
  11 10  9    6  7  8
 --0--0--0    0--0--0--
  14 12 13    17 15 16
"""
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
robot = Robot(i2c)

left_side = [
    Leg(robot,  0,  1,  2),
    Leg(robot,  9, 10, 11),
    Leg(robot, 13, 12, 14)
]

right_side = [
    Leg(robot, 4, 3, 5, invert=True),
    Leg(robot, 6, 7, 8, invert=True),
    Leg(robot, 17, 15, 16, invert=True)
]

# # feet test
# for n in range(3):
#     left_side[n].foot.position(150)
#     sleep(0.3)
#     left_side[n].foot.position(90)
#     sleep(0.3)

# for n in range(3):
#     right_side[n].foot.position(30)
#     sleep(0.3)
#     right_side[n].foot.position(90)
#     sleep(0.3)


# # knee test down
# for n in range(3):
#     left_side[n].knee.position(150)
#     sleep(0.3)
#     left_side[n].knee.position(90)
#     sleep(0.3)
#     left_side[n].knee.position(30)
#     sleep(0.3)
#     left_side[n].knee.position(90)
#     sleep(0.3)

# for n in range(3):
#     right_side[n].knee.position(30)
#     sleep(0.3)
#     right_side[n].knee.position(90)
#     sleep(0.3)
#     right_side[n].knee.position(150)
#     sleep(0.3)
#     right_side[n].knee.position(90)
#     sleep(0.3)

# # Hip Test
# for n in range(3):
#     left_side[n].hip.position(150)
#     sleep(0.3)
#     left_side[n].hip.position(90)
#     sleep(0.3)
#     left_side[n].hip.position(30)
#     sleep(0.3)
#     left_side[n].hip.position(90)
#     sleep(0.3)

# for n in range(3):
#     right_side[n].hip.position(30)
#     sleep(0.3)
#     right_side[n].hip.position(90)
#     sleep(0.3)
#     right_side[n].hip.position(150)
#     sleep(0.3)
#     right_side[n].hip.position(90)
#     sleep(0.3)

def neutral(release=True):
    for leg in left_side:
        leg.knee.position(90)
        leg.foot.position(90)
        leg.hip.position(90)
    for leg in right_side:
        leg.knee.position(90)
        leg.foot.position(90)
        leg.hip.position(90)
    if release:
        sleep(0.1)
        for leg in left_side:
            leg.knee.release()
            leg.foot.release()
            leg.hip.release()
        for leg in right_side:
            leg.knee.release()
            leg.foot.release()
            leg.hip.release()

def crouch():
    neutral()
    for leg in left_side:
        leg.knee.position(30)
    for leg in right_side:
        leg.knee.position(30)
    sleep(0.1)
    for leg in left_side:
        leg.knee.release()
    for leg in right_side:
        leg.knee.release()


def crab(delay=0.02, direction=1):
    # Wobbling knees
    theta = 0
    neutral(release=False)
    while True:
        group1_knees = 90 + int(sin(radians(theta)) * 30)
        group1_feet = 90 + int(sin(radians(theta+90)) * 30)
        group2_knees = 90 + int(sin(radians(theta + 180)) * 30)
        group2_feet = 90 + int(sin(radians(theta + 270)) * 30)

        for leg in (left_side[0], right_side[1], left_side[2]):
            leg.foot.position(group1_feet)
            leg.knee.position(group1_knees)

        for leg in (right_side[0], left_side[1], right_side[2]):
            leg.foot.position(group2_feet)
            leg.knee.position(group2_knees)

        sleep(delay)
        theta += direction
        if theta > 360:
            theta = 0

def leg_by_leg(delay=0.02):
    neutral(release=False)
    pattern = [left_side[0], right_side[0], left_side[1], right_side[1], left_side[2], right_side[2]]
    while True:
        #  All legs up and forward
        for leg in pattern:
            leg.knee.position(30)
            sleep(delay)
            leg.hip.position(110)
            sleep(delay)
            leg.knee.position(90)
            sleep(delay)
        # Now sweep back
        for leg in pattern:
            leg.hip.position(30)
        sleep(delay)


"""
for n in range(3):
    left_side[n].foot.position(150)
    sleep(0.3)
    left_side[n].foot.position(90)
    sleep(0.3)
"""