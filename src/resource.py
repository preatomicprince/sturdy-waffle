"""
Coal: Used to run lumber mill, labs, human farms
blood: Used to feed population. Perhaps sets cap and housing just sets spawn rate
wood: Used to buidl buildings
stone: Used to build roads and perhaps some buidlings
"""
from enum import Enum

class Resources:
    def __init__(self, blood: int = 0, coal: int = 0, stone: int = 0, wood: int = 0)->None:
        self.blood = blood
        self.coal = coal
        self.stone = stone
        self.wood = wood