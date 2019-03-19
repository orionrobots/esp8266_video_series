import gc

from serve import respond_html, serve_file, start_server
from spiderbot import init
from leg_by_leg_gait import leg_by_leg_tween
from crab_gait import crab
from ant_gait import ant_gait

from tweening_control import crouch, stand

def wrap_action(action, name):
    def _wrap(conn):
        action()
        respond_html(conn, '%s ok' % name)
    return _wrap

class MotionController:
    def __init__(self, spider):
        self.current_motion = None
        self.spider = spider
    
    def start_motion(self, motion, **kwargs):
        def _wrap(conn):
            self.current_motion = motion(self.spider, **kwargs)
        return _wrap

    def stop_motion(self, conn):
        self.current_motion = None
        self.spider.neutral()
        gc.collect()

    def motion(self):
        if self.current_motion:
            try:
                next(self.current_motion)
            except StopIteration:
                self.current_motion = None
                gc.collect()


def main():
    spider = init()
    spider.neutral()
    motion_controller = MotionController(spider)
    
    try:
        routes = {
            '/': lambda conn: serve_file(conn, 'spider_menu.html'),
            '/crouch': motion_controller.start_motion(crouch),
            '/stand': motion_controller.start_motion(stand),
            '/neutral': wrap_action(spider.neutral, 'neutral'),
            '/leg-by-leg': motion_controller.start_motion(leg_by_leg_tween),
            '/crab': motion_controller.start_motion(crab),
            '/ant': motion_controller.start_motion(ant_gait),
            '/ant-left': motion_controller.start_motion(ant_gait, left_scale=0.5),
            '/ant-right': motion_controller.start_motion(ant_gait, right_scale=0.5),
            '/stop': motion_controller.stop_motion,
        }
        start_server(routes, async_function=motion_controller.motion)
    finally:
        motion_controller.stop_motion('')

if __name__ == "__main__":
    main()
