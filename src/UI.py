from pathlib import Path
from definitions import *
from entity import Ent_Comp
import pygame
from building import Building, building_type  

class Text:
    font_path:str = "./res/themponewst.ttf" #https://www.1001freefonts.com/thempo-new-st.font
    colour = (64, 64, 64)
    size = 25
    def __init__(self, text:str, pos: I_Vec2):
        self.text = text
        self.pos = pos

    def draw(self, screen: pygame.display):
        name_res = pygame.font.Font(Path(Text.font_path), Text.size)
        surface = name_res.render(self.text, False, Text.colour)
        rect = surface.get_rect()
        rect.x = self.pos.x
        rect.y = self.pos.y        
        screen.blit(surface, rect)

class Button_Comp:
    def __init__(self):
        self.selected: bool = False

class Buttons:
    """ this class creates a button, it collets the width/height of the button, selects its location"""
    def __init__(self, pos: F_Vec2, texture: str, b_type: int): 
        self.ec = Ent_Comp(texture, pos)       
        self.btc = Button_Comp()
        self.building = Building(b_type)
        
    def draw(self, screen):                
        """this turns the clicked off after its clicked"""            
        screen.blit(self.ec.texture, (self.ec.rect.x, self.ec.rect.y))    
        

