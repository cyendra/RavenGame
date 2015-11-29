# encoding=utf-8
import System.Global as Global
from System import Toolkit

last_savefile_index = 0


def init():
    global last_savefile_index
    last_savefile_index = 0
    load_database()
    create_game_objects()


def load_database():
    load_normal_database()
    check_player_location()


def load_normal_database():
    Global.data_actors = Toolkit.load_data("Data/Actors.ravdata")


def check_player_location():
    return True


def create_game_objects():
    pass