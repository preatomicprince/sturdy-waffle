from pathlib import Path
from definitions import *
import pygame

class Text:
    font_path:str = "./res/themponewst.ttf"
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


class Buttons:
    """ this class creates a button, it collets the width/height of the button, selects its location"""
    
    def __init__(self, x, y, image, file, scale):        
        self.x = x
        self.y = y
        self.file = file
        self.image = pygame.image.load(self.file)
        """self.image = pygame.transform.scale(image, (int(width * scale)), (int(height * scale))) """
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        width = self.image.get_width()
        height = self.image.get_height() #I NEED TO FIGURE OUT HOW TO MAKE THIS SCALE
        
        """here we can see if the buttons been clicked"""
        self.clicked = False
        
    def draw(self, screen):    
        """this gets the mouse possition"""
        pos = pygame.mouse.get_pos()
        
        """this checks if the mouse possition is over a button"""
        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                
                
        """this turns the clicked off after its clicked"""
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
            
        screen.blit(self.image, (self.x, self.y))    
        

