import pygame
from definitions import *
from background import BG_Tile
from building import Build_Comp, Building
from character import Character, Char_Comp
from resource import resources
from entity import Ent_Comp, Interact_Comp
from camera import Camera

class Keys_Down:
    def __init__(self):
        self.left: bool = 0
        self.right: bool = 0
        self.up: bool = 0
        self.down: bool = 0

class Mouse:
    def __init__(self):
        self.pos = I_Vec2(0,0)
        self.ent_ID: int = None
        self.ent_type: type = None
        # self.buiding: Building
    
    def update_pos(self)->I_Vec2:
        self.pos.x, self.pos.y = pygame.mouse.get_pos()
        return self.pos

    def deselect(self)->None:
        self.selected = False
        self.ent_ID = None
        self.ent_type = None

class Level:
    """Struct to hold all level data and objects """
    def __init__(self)->None:
        self.background:list(list(BG_Tile)) = [[] for i in range(ROW_COUNT)] #NOTCURRENTLYMULTIDIMEN Multidimentional array of bg_tiles. bg_tile class yet to be added
        self.buildings:list(Building) = []
        self.chars:list(Character) = []
        self.res:dict = resources #count of player resources
        self.cam = Camera()
        self.mouse = Mouse()
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
            3. Characters
            TODO
            4. Buildings"""

        screen.fill((0,0,0))
        
        for y in range(len(self.background)): #draw tiles
            for x in self.background[y]:
                if x.ec.rect.x > 0 or x.ec.rect.y > 0:
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
        if char.cc.aim == char.ec.rect:
            char.cc.aim = I_Vec2(-1, -1)
        if char.cc.aim.x >= 0 or char.cc.aim.x >= 0:
            if char.cc.aim.x > char.ec.rect.x:
                char.ec.rect.x += char.cc.vel.x
            elif char.cc.aim.x < char.ec.rect.x:
                char.ec.rect.x -= char.cc.vel.x

            if char.cc.aim.y > char.ec.rect.y:
                char.ec.rect.y += char.cc.vel.y
            elif char.cc.aim.y < char.ec.rect.y:
                char.ec.rect.y -= char.cc.vel.y

        

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

    def left_click(self):
        self.mouse.update_pos()

        self.mouse.deselect()

        for ent in self.chars:
            if ent.ec.rect.x - self.cam.offset.x < self.mouse.pos.x < ent.ec.rect.x + ent.ec.rect.w - self.cam.offset.x:
                if ent.ec.rect.y - self.cam.offset.y < self.mouse.pos.y < ent.ec.rect.y + ent.ec.rect.h - self.cam.offset.y:
                    ent.ic.selected = True
                    self.mouse.ent_ID = ent.ec.ID
                    self.mouse.ent_type = type(ent)
                    print("selected")

    def right_click(self):
        self.mouse.update_pos()
        if self.mouse.ent_type is Character:
            for char in self.chars:
                if char.ec.ID == self.mouse.ent_ID:
                    char.cc.aim = self.mouse.pos
                    self.mouse.deselect()


        

        


