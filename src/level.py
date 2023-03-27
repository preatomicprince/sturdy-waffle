import pygame
from definitions import *
from background import BG_Tile
from building import Build_Comp, Building
from character import Character
from resource import resources
from camera import Camera

class Keys_Down:
    def __init__(self):
        self.left: bool = 0
        self.right: bool = 0
        self.up: bool = 0
        self.down: bool = 0

class Level:
    """Struct to hold all level data and objects """
    def __init__(self)->None:
        self.background:list(list(BG_Tile)) = [[] for i in range(ROW_COUNT)] #NOTCURRENTLYMULTIDIMEN Multidimentional array of bg_tiles. bg_tile class yet to be added
        self.buildings:list(Building) = []
        self.chars:list(Character) = []
        self.res:dict = resources #count of player resources
        self.cam = Camera()
        self.keys_down = Keys_Down()
        self.button_list = []
        self.UI_text = []

    def add_bg_tile(self, texture: str,  y_pos: float, coal: int = 0, stone: int = 0, wood: int = 0)->None:
        """Adds tiles to background list, in the specified y_pos. 
        AUtomatically fills next blank square in X direction"""
        column: int = len(self.background[y_pos])*BG_TILE_SIZE
        pos = F_Vec2(column, y_pos*BG_TILE_SIZE)
        self.background[y_pos].append(BG_Tile(texture, pos))

    def draw(self, screen: pygame.display)->None:
        """Draw all entities:
            1. BG_Tiles
            2.UI
            TODO:
            3. Characters
            4. Buildings"""

        screen.fill((0,0,0))
        
        for y in range(len(self.background)): #draw tiles
            for x in self.background[y]:
                if self.cam.check_on_screen(x.ec):
                    screen.blit(x.ec.texture, 
                    (x.ec.rect.x - self.cam.offset.x, x.ec.rect.y - self.cam.offset.y + TOOLBAR_HEIGHT))

        pygame.draw.rect(screen, (255, 255, 255), 
        pygame.Rect(0,0, SCREEN_WIDTH, TOOLBAR_HEIGHT+2)) #draw top toolbar

        for i in self.button_list:
            i.draw(screen)

        for i in self.UI_text:
            i.draw(screen)
        


    def _update_buiding(self, building: Building):
            level.res = self.buildings[i].bc.update_level_res()

    def _update_camera(self):
        if self.keys_down.right:
            self.cam.offset.x += self.cam.speed

        if self.keys_down.left:
            self.cam.offset.x -= self.cam.speed

        if self.cam.offset.y <= ROW_COUNT*BG_TILE_SIZE - SCREEN_HEIGHT + TOOLBAR_HEIGHT:
            if self.keys_down.down:
                self.cam.offset.y += self.cam.speed

        if self.cam.offset.y >= 0:
            if self.keys_down.up:
                self.cam.offset.y -= self.cam.speed

        if  self.cam.offset.x >= ROW_COUNT*BG_TILE_SIZE:
            self.cam.offset.x = 0
        if self.cam.offset.x < 0:
            self.cam.offset.x = ROW_COUNT*BG_TILE_SIZE

    def update(self):
        self._update_camera()
        for i in self.buildings:
            self._update_buidings(self.buildings[i])
        


