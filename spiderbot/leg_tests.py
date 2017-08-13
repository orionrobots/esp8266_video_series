from time import sleep
import spiderbot

left_side, right_side = spiderbot.init()

# feet test
def feet_test(side):
    """Pass in left side or right side"""
    for leg in side:
        leg.foot.position(150)
        sleep(0.3)
        leg.foot.position(90)
        sleep(0.3)

# # knee test down
def knee_test(side):
    for leg in side:
        leg.knee.position(150)
        sleep(0.3)
        leg.knee.position(90)
        sleep(0.3)
        leg.knee.position(30)
        sleep(0.3)
        leg.knee.position(90)
        sleep(0.3)

def hip_test(side):
    for leg in side:
        leg.hip.position(150)
        sleep(0.3)
        leg.hip.position(90)
        sleep(0.3)
        leg.hip.position(30)
        sleep(0.3)
        leg.hip.position(90)
        sleep(0.3)
