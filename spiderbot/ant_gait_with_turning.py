from time import sleep
import spiderbot
from machine import reset
from spiderbot_demo import neutral, left_side, right_side

knees_up = 30
knees_down = 90

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
        for n in len(self.legs):
            yield self.get_scale(n), self.legs[n]

    def move(self, knee=None, hip=None, foot=None, delay=None):
        for hip_scale, leg in self.iter():
            if foot:
                leg.foot.position(foot)
            if knee:
                leg.knee.position(knee)
            if hip:
                position = int(hip * hip_scale)
                leg.hip.position(position)
        if delay:
            sleep(delay)

# Turning ant pattern
def ant_pattern_with_turn(hips_range=20, position_delay=0.1, smooth_delay=0.01, smooth_speed=4, scale_left=1, scale_right=1):
    group1 = ScalingLegGroup(
        [left_side[0], right_side[1], left_side[2]],
        [0, 1, 0]
    )
    group2 = ScalingLegGroup(
        [right_side[0], left_side[1], right_side[2]],
        [1, 0, 1]
    )
    group1.set_scale(scale_left, scale_right)
    group2.set_scale(scale_left, scale_right)
    neutral(False)
    # Put group1 up first
    group1.move(knee=knees_up, delay=position_delay)
    # Starting from neutral (but knees up)
    while True:
        # Sweep group1 hips forward (in the air)
        # While sweeping group2 hips back
        for n in range(0, hips_range, smooth_speed):
            group1.move(hip=90+n)
            group2.move(hip=90-n)
            sleep(smooth_delay)
        # Now place group 1 down
        group1.move(knee=knees_down, delay=position_delay)
        # Pick group 2 up
        group2.move(knee=knees_up, delay=position_delay)
        # Now sweep the other way - group1 goes back, group1 forward, by 60
        for n in range(-hips_range, hips_range, smooth_speed):
            group1.move(hip=90-n)
            group2.move(hip=90+n)
            sleep(smooth_delay)
        # Place group 2 down and 1 up
        group2.move(knee=knees_down, delay=position_delay)
        group1.move(knee=knees_up, delay=position_delay)
        # Now half sweep group 1 forward, and 2 back (to neutral)
        for n in range(-hips_range, 0, smooth_speed):
            group1.move(hip=90+n)
            group2.move(hip=90-n)
            sleep(smooth_delay)
