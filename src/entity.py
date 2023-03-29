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
        self.visible: bool = True
        self.ID = Ent_Comp.ent_count
        Ent_Comp.ent_count += 1
        
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.texture, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey(colour)
        return image

"""GREEN = (11, 158, 3)   
animation_list = []
animation_steps = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0


spritesheet_image = pygame.image.load("./res/Pixilart Sprite Sheet.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(spritesheet_image)

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 100, 100, sprite_sheet.GREEN))
    

for x in range(animation_list):
    screen.blit(animation_list[x], (x * 100, 0))




frame_0 = sprite_sheet.get_image(spritesheet_image, 0, 100, 100, sprite_sheet.GREEN)
frame_1 = sprite_sheet.get_image(spritesheet_image, 1, 100, 100, sprite_sheet.GREEN)
screen.blit(frame_0, (0,0))
screen.blit(frame_1, (100,0))    
"""
