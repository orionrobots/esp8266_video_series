from spiderbot_demo import *

def leg_by_leg(position_delay=0.1, smooth_delay=0.01, smooth_speed=4):
    neutral(release=False)
    pattern = [left_side[0], right_side[0], left_side[1], right_side[1], left_side[2], right_side[2]]
    while True:
        #  All legs up and forward
        for leg in pattern:
            leg.knee.position(30)
            sleep(position_delay)
            leg.hip.position(110)
            sleep(position_delay)
            leg.knee.position(90)
            sleep(position_delay)
        # Now sweep back
        for n in range(110, 90, -smooth_speed):
            for leg in pattern:
                leg.hip.position(n)
                sleep(smooth_delay)
        sleep(position_delay)

