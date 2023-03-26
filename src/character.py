import pygame
from definitions import F_Vec2
from entity import Ent_Comp, Interact_Comp

class Char_Comp:
    pass
class Character:
    def __init__(self)->None:
        self.ec = Ent_Comp(texture, pos)
        self.ic = Interact_Comp()
