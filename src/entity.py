import pygame
from pathlib import Path
from definitions import F_Vec2

class Ent_Comp:
    ent_count: int = 0
    colour = (11, 158, 3)
    """Component containing variables found in all entities"""
    def __init__(self, texture: str, pos: F_Vec2)->None:
        self.texture_list = []
        if type(texture) == str:
            self.texture = pygame.image.load(Path(texture))
        else:
            for i in texture:
                image = pygame.image.load(Path(i))
                image.convert_alpha()
                image.set_colorkey(Ent_Comp.colour)
                self.texture_list.append(image)
                self.texture = self.texture_list[0]


        self.rect = self.texture.get_rect()
        self.rect.x = pos.x
        self.rect.y = pos.y
        self.visible: bool = True
        self.ID = Ent_Comp.ent_count
        Ent_Comp.ent_count += 1
        
        """GREEN = (11, 158, 3) 
        animation_list = []
        animation_steps = 2
        spritesheet_image = pygame.image.load().convert_alpha()
        sprite_sheet = spritesheet.SpriteSheet(spritesheet_image)"""

    
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.texture, (0, 0), ((frame * width), 0, width, height))
        image.set_colorkey(colour)
        return image
        
"""for x in range(animation_steps):
    animation_list.append(Ent_Comp.get_image(x, 100, 100, Ent_Comp.GREEN))
grass = Ent_Comp("./res/grass_sprite_sheet.png", )
"""
"""  

last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0




for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 100, 100, 
    

for x in range(animation_list):
    screen.blit(animation_list[x], (x * 100, 0))




frame_0 = sprite_sheet.get_image(spritesheet_image, 0, 100, 100, sprite_sheet.GREEN)
frame_1 = sprite_sheet.get_image(spritesheet_image, 1, 100, 100, sprite_sheet.GREEN)
screen.blit(frame_0, (0,0))
screen.blit(frame_1, (100,0))    
"""
