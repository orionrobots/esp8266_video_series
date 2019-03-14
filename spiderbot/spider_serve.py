from serve import respond_html, serve_file, start_server
from spiderbot import init
from leg_by_leg_gait import leg_by_leg
from crab_gait import crab
import gc


def wrap_action(action, name):
    def _wrap(conn):
        action()
        respond_html(conn, '%s ok' % name)
    return _wrap

class MotionController:
    def __init__(self, spider):
        self.current_motion = None
        self.spider = spider
    
    def start_motion(self, motion):
        def _wrap(conn):
            self.current_motion = motion(self.spider)
        return _wrap

    def stop_motion(self, conn):
        self.current_motion = None
        self.spider.neutral()
        gc.collect()

    def motion(self):
        if self.current_motion:
            next(self.current_motion)

def main():
    spider = init()
    spider.neutral()
    motion_controller = MotionController(spider)
    
    try:
        routes = {
            '/': lambda conn: serve_file(conn, 'spider_menu.html'),
            '/crouch': wrap_action(spider.crouch, 'crouch'),
            '/neutral': wrap_action(spider.neutral, 'neutral'),
            '/leg-by-leg': motion_controller.start_motion(leg_by_leg),
            '/crab': motion_controller.start_motion(crab),
            '/stop': motion_controller.stop_motion,
        }
        start_server(routes, async_function=motion_controller.motion)
    finally:
        motion_controller.stop_motion('')

if __name__ == "__main__":
    main()
