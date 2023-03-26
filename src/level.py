import pygame
from background import BG_Tile
from building import Building
from character import Character
from resource import Resources

class Level:
    """Struct to hold all level data and objects """
    def __init__(self)->None:
        self.background:list(list(BG_Tile)) #Multidimentional array of bg_tiles. bg_tile class yet to be added
        self.buildings:list(Building)
        self.chars:list(Character)
        self.res:Resources #count of player resources