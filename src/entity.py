import pygame
from pathlib import Path
from definitions import F_Vec2

class Ent_Comp:
    ent_count: int = 0
    """Component containing variables found in all entities"""
    def __init__(self, texture: str, pos: F_Vec2)->None:
        self.texture = pygame.image.load(Path(texture))
        self.rect = self.texture.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y
        self.visible: bool = 1
        
        self.ID = Ent_Comp.ent_count
        Ent_Comp.ent_count += 1