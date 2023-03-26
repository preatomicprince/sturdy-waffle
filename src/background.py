from definitions import F_Vec2
from entity import Ent_Comp
from resource import resources

class BG_Tile:
    """Class to hold background tile image, position and whether they contain local resources"""
    def __init__(self, texture: str, pos: F_Vec2, coal: int = 0, stone: int = 0, wood: int = 0):
        self.ec = Ent_Comp(texture, pos)
        self.res = resources