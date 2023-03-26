""""
housing: sets pop cap and spawn speed
human farm: produces blood
mine: produces coal and stone
lumber mill: produces wood
stable: holds horses that can drag buildings
laboratory: Used to develop more advanced versions of buidings   
"""
import pygame
from definitions import F_Vec2
from entity import Ent_Comp
from enum import Enum

class Enum_Build(Enum):
    Blood_Farm = 1
    Mine = 2
    Lumber_Mill = 3
    Stable = 4
    Lab = 5
    House = 6

class Building:
    def __init__(selfpos: F_Vec2, type: Enum_Build):
        self.ec = ent_comp(texture, pos)
        self.res = resource
        """match type:
            case Enum_Build.Blood_Farm:
                texture = "../res/bloodfarm.png"
            case Enum_Build.Mine:
                texture = "../res/mine.png"
            case Enum_Build.Lumber_Mill:
                texture = "../res/lumbermill.png"
            case Stab"""