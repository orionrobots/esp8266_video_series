from math import sin, radians

def crab(spider, direction=1):
    # Wobbling knees
    theta = 0
    spider.neutral(release=False)
    while True:
        group1_knees = 90 + int(sin(radians(theta)) * 30)
        group1_feet = 90 + int(sin(radians(theta+90)) * 30)
        group2_knees = 90 + int(sin(radians(theta + 180)) * 30)
        group2_feet = 90 + int(sin(radians(theta + 270)) * 30)

        for leg in (spider.left_side[0], spider.right_side[1], spider.eft_side[2]):
            leg.foot.position(group1_feet)
            leg.knee.position(group1_knees)

        for leg in (spider.ight_side[0], spider.left_side[1], spider.right_side[2]):
            leg.foot.position(group2_feet)
            leg.knee.position(group2_knees)

        yield
        theta += direction
        if theta > 360:
            theta = 0
