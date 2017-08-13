from time import sleep
import spiderbot
from machine import reset

left_side, right_side = spiderbot.init()

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

