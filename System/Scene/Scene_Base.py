# encoding=utf-8


class SceneBase(object):
    def main(self, dt):
        self.start()
        self.post_start()
        self.update()
        self.pre_terminate()
        self.terminate()

    def start(self):
        pass

    def post_start(self):
        pass

    def scene_changing(self):
        return False

    def update(self):
        self.update_basic()

    def update_basic(self):
        pass

    def update_all_windows(self):
        pass

    def dispose_all_windows(self):
        pass

    def return_scene(self):
        pass

    def fadeout_all(self):
        pass

    def check_gameover(self):
        pass

    def pre_terminate(self):
        pass

    def terminate(self):
        self.dispose_all_windows()