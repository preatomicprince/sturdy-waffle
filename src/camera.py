import pygame
from definitions import SCREEN_HEIGHT, SCREEN_WIDTH, I_Vec2
from entity import Ent_Comp

class Camera:
    def __init__(self):
        self.size = I_Vec2(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.offset = I_Vec2(0, 0)
        self.speed = 2 

    def check_on_screen(self,ec: Ent_Comp)-> int:
        return 1
        if (ec.rect.x - self.offset.x) >= 0 and (ec.rect.x - self.offset.x) < SCREEN_WIDTH:
            if (ec.rect.y - self.offset.y) >= 0 and (ec.rect.y - self.offset.y) < SCREEN_WIDTH:
                return 1

        return 0
