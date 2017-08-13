from time import sleep
import spiderbot
from machine import reset
from spiderbot_demo import neutral, left_side, right_side

def move_group(group, knee=None, hip=None, foot=None, delay=None):
    """Group is a list of legs. Change all the positions
    as defined"""
    for leg in group:
        if foot:
            leg.foot.position(foot)
        if knee:
            leg.knee.position(knee)
        if hip:
            leg.hip.position(hip)
    if delay:
        sleep(delay)

knees_up = 30
knees_down = 90

def ant_pattern(hips_range=20, position_delay=0.1, smooth_delay=0.01, smooth_speed=4):
    group1 = [left_side[0], right_side[1], left_side[2]]
    group2 = [right_side[0], left_side[1], right_side[2]]
    neutral(False)
    # Put group1 up first
    move_group(group1, knee=knees_up, delay=position_delay)
    # Starting from neutral (but knees up)
    while True:
        # Sweep group1 hips forward (in the air)
        # While sweeping group2 hips back
        for n in range(0, hips_range, smooth_speed):
            move_group(group1, hip=90+n)
            move_group(group2, hip=90-n)
            sleep(smooth_delay)
        # Now place group 1 down
        move_group(group1, knee=knees_down, delay=position_delay)
        # Pick group 2 up
        move_group(group2, knee=knees_up, delay=position_delay)
        # Now sweep the other way - group1 goes back, group1 forward, by 60
        for n in range(-hips_range, hips_range, smooth_speed):
            move_group(group1, hip=90-n)
            move_group(group2, hip=90+n)
            sleep(smooth_delay)
        # Place group 2 down and 1 up
        move_group(group2, knee=knees_down, delay=position_delay)
        move_group(group1, knee=knees_up, delay=position_delay)
        # Now half sweep group 1 forward, and 2 back (to neutral)
        for n in range(-hips_range, 0, smooth_speed):
            move_group(group1, hip=90+n)
            move_group(group2, hip=90-n)
            sleep(smooth_delay)

