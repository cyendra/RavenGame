# encoding=utf-8

import pyglet
from System.Base import ActorImage, ActorSprite

game_window = pyglet.window.Window(800, 600)

explosion = pyglet.image.load('Graphics/Actor1.png')
explosion_seq = ActorImage(explosion).get(0)
main_batch = pyglet.graphics.Batch()
show = ActorSprite(img=explosion_seq, x=400, y=300, batch=main_batch)


def update(dt):
    show.update(dt)


@game_window.event
def on_draw():
    game_window.clear()
    show.draw()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()

