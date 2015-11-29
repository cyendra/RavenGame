# encoding=utf-8

from System.Module import DataManager

__scene = None
__stack = []
__background_bitmap = None


def init():
    DataManager.init()
    __set_scene(None)


def run(dt):
    if __scene is None:
        return False
    __scene.main
    return True


def get_scene():
    return __scene


def __set_scene(new_scene):
    global __scene
    __scene = new_scene


def scene_is(scene_class):
    if isinstance(__scene, scene_class):
        return True
    return False


def goto(scene_class):
    __set_scene(scene_class())


def call(scene_class):
    __stack.append(__scene)
    __set_scene(scene_class())


def back():
    __set_scene(__stack.pop())


def clear():
    __stack.clear()


def exit_game():
    __set_scene(None)


def get_background_bitmap():
    return __background_bitmap

