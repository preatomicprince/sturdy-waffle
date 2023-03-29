import pygame
from definitions import *
from entity import Ent_Comp

class Char_Comp:
    speed = 1
    def __init__(self):
        self.dir = I_Vec2(0, 0)
        self.vel = I_Vec2(Char_Comp.speed, Char_Comp.speed)
        self.aim = I_Vec2(-1, -1) #location to move to
        self.state:str = "Still"
        self.prev_state:str = "Still"
        self.frame_count: int = 0
        self.frames = range(10, 11)
        self.killed: bool = False

class Character:
    def __init__(self, texture: str, pos: F_Vec2)->None:
        self.ec = Ent_Comp(texture, pos)
        self.cc = Char_Comp()
        

    def kill(self):
        print("Ded")

    def update_frame(self):
        if self.cc.frame_count >= len(self.cc.frames) -1:
            self.cc.frame_count = 0
        else:
            self.cc.frame_count += 1
        print(f"{self.cc.state} {self.cc.frame_count} {self.cc.frames[self.cc.frame_count-1]}")
        self.ec.texture = self.ec.texture_list[self.cc.frames[self.cc.frame_count]]


    def update_state(self):
        if self.cc.dir.x > 0:
            self.cc.state = "Right"
            self.cc.frames = range(6, 9)
        elif self.cc.dir.x < 0:
            self.cc.state = "Left"
            self.cc.frames = range(0, 3)
        elif self.cc.dir.y > 0:
            self.cc.state = "Up"
            self.cc.frames = range(9, 12)
        elif self.cc.dir.y < 0:
            self.cc.state = "Down"
            self.cc.frames = range(3, 6)
        else:
            if not self.cc.killed:
                self.cc.state = "still"
                self.cc.frames = range(10, 11)
            else:
                self.cc.state = "killed"
                self.cc.frames = range(12, 16)

        if self.cc.state != self.cc.prev_state:
            self.frame_count = 0

        self.update_frame()
        self.cc.prev_state = self.cc.state

    

