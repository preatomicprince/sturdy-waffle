import pygame
from definitions import *
from background import BG_Tile
from building import Build_Comp, Building
from character import Character, Char_Comp
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

    def add_char(self, texture: str, pos: F_Vec2):
        self.chars.append(Character(texture, pos))

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
                if x.ec.rect.x > 0 or y > 0:
                    screen.blit(x.ec.texture, 
                    (x.ec.rect.x - self.cam.offset.x, x.ec.rect.y - self.cam.offset.y))
                    if self.cam.offset.x > (COL_COUNT*BG_TILE_SIZE - SCREEN_WIDTH):
                        screen.blit(x.ec.texture, 
                        (x.ec.rect.x - self.cam.offset.x + COL_COUNT*BG_TILE_SIZE, x.ec.rect.y - self.cam.offset.y))

            
        for character in self.chars:
            screen.blit(character.ec.texture, (character.ec.rect.x - self.cam.offset.x, 
                                                character.ec.rect.y - self.cam.offset.y))
            if self.cam.offset.x > (COL_COUNT*BG_TILE_SIZE - SCREEN_WIDTH):
                        screen.blit(character.ec.texture, 
                        (character.ec.rect.x - self.cam.offset.x + COL_COUNT*BG_TILE_SIZE, character.ec.rect.y - self.cam.offset.y))
        
        pygame.draw.rect(screen, (255, 255, 255),pygame.Rect(0,0, SCREEN_WIDTH, TOOLBAR_HEIGHT+2)) #draw white toolbar

        for i in self.button_list:
            i.draw(screen)

        for i in self.UI_text:
            i.draw(screen)
        
    def _update_char(self, char: Character):
        if char.cc.aim.x >= 0 and char.cc.aim.y >= 0:
            char.ec.rect.x += char.cc.vel.x
            char.ec.rect.y += char.cc.vel.y

        if char.cc.aim == char.ec.rect:
            char.cc.aim = I_Vec2(-1, -1)

    def _update_buiding(self, building: Building):
            level.res = self.buildings[i].bc.update_level_res()

    def _update_camera(self):
        if self.keys_down.right:
            self.cam.offset.x += self.cam.speed

        if self.keys_down.left:
            self.cam.offset.x -= self.cam.speed

        if self.cam.offset.y < ROW_COUNT*BG_TILE_SIZE - SCREEN_HEIGHT: #+ TOOLBAR_HEIGHT
            if self.keys_down.down:
                self.cam.offset.y += self.cam.speed
        else: self.cam.offset.y = ROW_COUNT*BG_TILE_SIZE - SCREEN_HEIGHT

        if self.cam.offset.y > 0:
            if self.keys_down.up:
                self.cam.offset.y -= self.cam.speed
        else: self.cam.offset.y = 0

        if  self.cam.offset.x >= COL_COUNT*BG_TILE_SIZE:
            self.cam.offset.x = 0
        if self.cam.offset.x < 0:
            self.cam.offset.x = COL_COUNT*BG_TILE_SIZE

    def update(self):
        self._update_camera()
        for building in self.buildings:
            self._update_buidings(building)
        for character in self.chars:
            self._update_char(character)
        


