"""Concept:
* Create tweens with:
    * start frame
    * end frame
    * callable
    * start value
    * end end value
* Add tweens to the tween player.
* Set the frame loop point in the tween player.
* Start the tween player, get a generator.
* Each time the generator is called, a frame is advanced
    * All tweens are checked, and activated if it's their frame.
        * This will mean their callable is called with a value in the range.
    * Reset made if needed (mod operator)
"""

class Tween:
    __slots__ = ['_start_frame', '_end_frame', '_callback', '_start_value', '_end_value',
                '_const']
    def __init__(self, start_frame, end_frame, callback, start_value, end_value):
        self._start_frame = start_frame
        self._end_frame = end_frame
        self._callback = callback
        self._start_value = start_value
        self._end_value = end_value

        self._const = (end_value - start_value) / (end_frame - start_frame)

    def activate(self, frame_number):
        if frame_number < self._start_frame or frame_number > self._end_frame:
            return
        # in a frame that matters to this tween
        position = self._start_value + self._const * (frame_number - self._start_frame)
        # print('Tween frame:', frame_number, 'callback:', 
        #     self._callback, 'position:', position, )
        self._callback(int(position))


class TweenPlayer:
    def __init__(self):
        self.tweens = []
        self.end_frame = 0
        self.loop = False

    def add_tween(self, tween):
        self.tweens.append(tween)

    def set_end(self, end_frame):
        self.end_frame = end_frame

    def animate(self):
        while True:
            for frame in range(self.end_frame):
                for tween in self.tweens:
                    tween.activate(frame)
                yield
            if not self.loop:
                return

def crouch(spider):
    player = TweenPlayer()
    spider.neutral()
    for leg in spider.left_side:
        player.add_tween(Tween(
            0, 20, leg.knee.position, 90, 30
        ))
    for leg in spider.right_side:
        player.add_tween(Tween(
            0, 20, leg.knee.position, 90, 30
        ))
    player.set_end(20)
    for frame in player.animate():
        yield
    for leg in spider.left_side:
        leg.knee.release()
    for leg in spider.right_side:
        leg.knee.release()

def stand(spider):
    player = TweenPlayer()
    for leg in spider.left_side:
        player.add_tween(Tween(
            0, 20, leg.knee.position, 30, 90
        ))
    for leg in spider.right_side:
        player.add_tween(Tween(
            0, 20, leg.knee.position, 30, 90
        ))
    player.set_end(20)
    return player.animate()

