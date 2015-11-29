# encoding=utf-8

from System import Toolkit


__cache = {}


def load_bitmap(folder_name, filename):
    return normal_bitmap(folder_name + filename)


def normal_bitmap(path):
    if not include(path):
        __cache[path] = Toolkit.load_image(path)
    return __cache[path]


def include(key):
    return key in __cache.keys()


def clear():
    __cache.clear()


