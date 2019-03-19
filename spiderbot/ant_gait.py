from tweening_control import Tween, TweenPlayer

class ScaleServo:
    """Servo motor with scaling. Used for turning operations"""
    def __init__(self, servo, scale):
        self._servo = servo
        self._scale = scale

    def scale(self, scale):
        self._scale = scale

    def position(self, position):
        """Position the scaled servo.
        positions are relative to 90 degrees"""
        angle = 90 + int(self._scale * position)
        self._servo.position(angle)


def ant_gait(spider, left_scale=1, right_scale=1, hips_range=20):
    knees_up = 30
    knees_down = 90
    feet_in = 60
    feet_out = 90

    
    group_1 = [
        spider.left_side[0],
        spider.right_side[1],
        spider.left_side[2]
    ]
    group_1_hips = [
        ScaleServo(spider.left_side[0].hip, left_scale),
        ScaleServo(spider.right_side[1].hip, right_scale),
        ScaleServo(spider.left_side[2].hip, left_scale),
    ]
    group_2 = [
        spider.right_side[0],
        spider.left_side[1],
        spider.right_side[2]
    ]
    group_2_hips = [
        ScaleServo(spider.right_side[0].hip, right_scale),
        ScaleServo(spider.left_side[1].hip, left_scale),
        ScaleServo(spider.right_side[2].hip, right_scale),
    ]
    # lift up group 1
    for leg in group_1:
        leg.knee.position(knees_up)
        leg.foot.position(feet_in)

    def position_all_hips(position):
        for hip in group_1_hips:
            hip.position(position)
        for hip in group_2_hips:
            hip.position(-position)

    player = TweenPlayer()
    current_frame = 0
    # sweep group 1 back, group 2 forward
    player.add_tween(Tween(
        0, 20, position_all_hips, 0, hips_range
    ))
    # put down group 1
    for leg in group_1:
        # put down group 1
        player.add_tween(Tween(
            20, 25, leg.knee.position, knees_up, knees_down
        ))
        player.add_tween(Tween(
            20, 25, leg.foot.position, feet_in, feet_out
        ))
    # lift group 2
    for leg in group_2:
        # lift up group 2
        player.add_tween(Tween(
            25, 30, leg.knee.position, knees_down, knees_up
        ))
        player.add_tween(Tween(
            25, 30, leg.foot.position, feet_out, feet_in
        ))
    # sweep group 2 back, group 1 forward
    player.add_tween(Tween(
        30, 40, position_all_hips, hips_range, -hips_range
    ))
    # group 2 down
    for leg in group_2:
        # lift up group 2
        player.add_tween(Tween(
            40, 45, leg.knee.position, knees_up, knees_down
        ))
        player.add_tween(Tween(
            40, 45, leg.foot.position, feet_in, feet_out
        ))
    # group 1 up
    for leg in group_1:
        # lift up group 2
        player.add_tween(Tween(
            45, 50, leg.knee.position, knees_down, knees_up
        ))
        player.add_tween(Tween(
            45, 50, leg.foot.position, feet_out, feet_in
        ))
    # Now half sweep group 1 forward, and 2 back (to neutral)
    player.add_tween(Tween(
        50, 60, position_all_hips, -hips_range, 0
    ))
    player.loop = True
    player.set_end(60)

    return player.animate()