def leg_by_leg(spider, smooth_speed=4):
    spider.neutral(release=False)
    pattern = [spider.left_side[0], spider.right_side[0], spider.left_side[1], 
            spider.right_side[1], spider.left_side[2], spider.right_side[2]]
    # Timebase - assume 0.01
    key_frames = {}
    current_key_frame = 0 
    # add legs
    for leg in pattern:
        key_frames[current_key_frame] =    lambda: pattern[0].knee.position(30)
        key_frames[current_key_frame+10] = lambda: pattern[0].hip.position(110)
        key_frames[current_key_frame+20] = lambda: pattern[0].knee.position(90)
        current_key_frame += 30
    # add sweep
    for n in range(110, 90, -smooth_speed):
        def all_legs():
            for leg in pattern:
                leg.hip.position(n)
        key_frames[current_key_frame] = all_legs
        current_key_frame += 1
    reset_frame = current_key_frame + 10
    timebase = 0
    while True:
        timebase += 1
        current_key_frame = timebase % reset_frame
        if key_frames.get(current_key_frame):
            key_frames[current_key_frame]()
        yield