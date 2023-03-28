import pygame
from definitions import *
from entity import Ent_Comp, Interact_Comp

class Char_Comp:
    speed = 1
    def __init__(self):
        self.dir = I_Vec2(0, 0)
        self.vel = I_Vec2(Char_Comp.speed, Char_Comp.speed)
        self.aim = I_Vec2(-1, -1) #location to move to

class Character:
    def __init__(self, texture: str, pos: F_Vec2)->None:
        self.ec = Ent_Comp(texture, pos)
        self.cc = Char_Comp()
