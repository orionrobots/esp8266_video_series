from tweening_control import Tween, TweenPlayer

def leg_by_leg_tween(spider):
    spider.neutral(release=False)
    pattern = [spider.left_side[0], spider.right_side[0], spider.left_side[1], 
            spider.right_side[1], spider.left_side[2], spider.right_side[2]]
    player = TweenPlayer()
    # add legs
    current_start = 0
    for leg in pattern:
        player.add_tween(Tween(
            current_start, current_start + 20, leg.knee.position, 90, 30
        ))
        player.add_tween(Tween(
            current_start + 20, current_start + 40, leg.hip.position, 90, 110
        ))
        player.add_tween(Tween(
            current_start + 40, current_start + 60, leg.knee.position, 30, 90
        ))
        current_start += 60
    # add sweep
    for leg in pattern:
        player.add_tween(Tween(
            current_start, current_start + 20, leg.hip.position, 110, 90
        ))
    player.set_end(current_start + 20)
    player.loop = True
    return player.animate()