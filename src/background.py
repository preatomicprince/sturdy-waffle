from definitions import F_Vec2
from entity import Ent_Comp
from resource import resources
from copy import copy
class BG_Tile:
    """Class to hold background tile image, position and whether they contain local resources"""
    def __init__(self, texture: str, pos: F_Vec2, coal: int , stone: int, wood: int):
        self.ec = Ent_Comp(texture, pos)
        self.res = copy(resources)
        self.res["Coal"] = coal
        self.res["Stone"] = stone
        self.res["Wood"] = wood
