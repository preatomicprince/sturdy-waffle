import pygame
from definitions import F_Vec2, BG_TILE_SIZE, ROW_COUNT
from background import BG_Tile
from building import Build_Comp, Building
from character import Character
from resource import resources
from camera import Camera

class Level:
    """Struct to hold all level data and objects """
    def __init__(self)->None:
        self.background:list(list(BG_Tile)) = [[] for i in range(ROW_COUNT)] #NOTCURRENTLYMULTIDIMEN Multidimentional array of bg_tiles. bg_tile class yet to be added
        self.buildings:list(Building) = []
        self.chars:list(Character) = []
        self.res:dict = resources #count of player resources
        self.cam = Camera()
        self.button_list = []

    def add_bg_tile(self, texture: str,  y_pos: float, coal: int = 0, stone: int = 0, wood: int = 0)->None:
        """Adds tiles to background list, in the specified y_pos. 
        AUtomatically fills next blank square in X direction"""
        column: int = len(self.background[y_pos])*BG_TILE_SIZE
        pos = F_Vec2(column, y_pos*BG_TILE_SIZE)
        self.background[y_pos].append(BG_Tile(texture, pos))

    def draw(self, screen: pygame.display)->None:
        """Draw all entities:
            1. BG_Tiles
            TODO:
            2. Characters
            3. Buildings"""
        
        for y in range(len(self.background)): #draw tiles
            for x in self.background[y]:
                if self.cam.check_on_screen(x.ec):
                    screen.blit(x.ec.texture, 
                    (x.ec.rect.x - self.cam.offset.x, x.ec.rect.y - self.cam.offset.y))
                    #print(x.ec.rect.x)
                else:
                    print(f"{x.ec.ID} was not displayed\n")

    def _update_buiding(self, building: Building):
            level.res = self.buildings[i].bc.update_level_res()

    def update(self):
        for i in self.buildings:
            self._update_buidings(self.buildings[i])
