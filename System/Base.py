# encoding=utf-8

import pyglet


class ActorImage(object):
    def __init__(self, actor_image):
        self.res = []
        sub_actor_image = pyglet.image.ImageGrid(actor_image, 2, 4)
        for i in range(0, 2):
            for j in range(0, 4):
                img = pyglet.image.ImageGrid(sub_actor_image[i, j], 4, 3)
                self.res.append(img)

    def get(self, idx):
        return self.res[idx]


class ActorSprite(pyglet.sprite.Sprite):
    COUNT  = 16
    FRAME = 3
    UP    = 0
    RIGHT = 1
    LEFT  = 2
    DOWN  = 3

    def __init__(self, *args, **kwargs):
        self.count = 0
        self.img_idx = 0
        self.direct = ActorSprite.DOWN
        self.actor_image = kwargs['img']
        kwargs['img'] = self.actor_image[3, 0]
        super(ActorSprite, self).__init__(*args, **kwargs)

    def update(self, dt):
        if self.count >= ActorSprite.COUNT:
            self.count = 0
            self.img_idx = (self.img_idx + 1) % ActorSprite.FRAME
            self.image = self.actor_image[self.direct, self.img_idx]
            print(self.img_idx)
        self.count += 1

    def set_direct(self, direct):
        self.direct = direct
