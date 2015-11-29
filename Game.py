# encoding=utf-8

import pyglet
from System.Module import SceneManager

game_window = pyglet.window.Window(800, 600)


@game_window.event
def on_draw():
    game_window.clear()


def update(dt):
    if not SceneManager.run(dt):
        pyglet.app.exit()


if __name__ == '__main__':
    SceneManager.init()
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
