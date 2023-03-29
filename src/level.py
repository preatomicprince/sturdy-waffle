import pygame
import random
from itertools import chain
from copy import copy
from definitions import *
from background import BG_Tile
from building import Build_Comp, Building, building_type
from character import Character, Char_Comp
from pathlib import Path
from resource import resources
from entity import Ent_Comp
from camera import Camera
from UI import Buttons, Text, Tooltip

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
        self.tip = Tooltip()
        self.building: Building = None
    
    def update_pos(self)->None:
        self.pos.x, self.pos.y = pygame.mouse.get_pos()

    def deselect(self)->None:
        self.ent_ID = None
        self.ent_type = None
        self.building = None

class sunlight:
    def __init__(self):
        self.rect = pygame.Rect(-2500, 0, (COL_COUNT/2)*BG_TILE_SIZE, ROW_COUNT*BG_TILE_SIZE)
        self.sl_pos = I_Vec2(self.rect.x, self.rect.y)
        self.timer = 0
        self.update_time = 5000

class Level:
    """Struct to hold all level data and objects """
    def __init__(self)->None:
        self.background:list(list(BG_Tile)) = [[] for i in range(ROW_COUNT)] #NOTCURRENTLYMULTIDIMEN Multidimentional array of bg_tiles. bg_tile class yet to be added
        self.buildings:list(Building) = []
        self.chars:list(Character) = []
        self.res:dict = copy(resources) #count of player resources
        self.res["Wood"] += 100
        self.sunlight = sunlight()
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
        self.res["Pop. "] += 1

    def draw(self, screen: pygame.display)->None:
        """Draw all entities:
            1. BG_Tiles
            2. Characters
            3. Buildings
            4.UI"""

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
            if character.ec.visible:
                screen.blit(character.ec.texture, (character.ec.rect.x - self.cam.offset.x, 
                                                    character.ec.rect.y - self.cam.offset.y))
                if self.cam.offset.x > (COL_COUNT*BG_TILE_SIZE - SCREEN_WIDTH):
                            screen.blit(character.ec.texture, 
                            (character.ec.rect.x - self.cam.offset.x + COL_COUNT*BG_TILE_SIZE, character.ec.rect.y - self.cam.offset.y))
        
        for building in self.buildings:
            screen.blit(building.ec.texture, ((building.ec.rect.x - self.cam.offset.x), 
                                                building.ec.rect.y - self.cam.offset.y))

        
        if self.mouse.building != None:
            screen.blit(self.mouse.building.ec.texture, ((self.mouse.building.ec.rect.x - self.cam.offset.x), 
                                                self.mouse.building.ec.rect.y - self.cam.offset.y))
        pygame.draw.rect(screen, (64, 64, 64),pygame.Rect(0,SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100)) #draw white toolbar
        pygame.draw.rect(screen, (128, 128, 180),pygame.Rect(0,SCREEN_HEIGHT - TOOLBAR_HEIGHT, SCREEN_WIDTH, TOOLBAR_HEIGHT)) #draw white toolbar

        for i in self.button_list:
            i.draw(screen)

        for i in self.UI_text:
            Text.colour = (64, 64, 64)
            i.draw(screen)

        if self.mouse.tip.visible:
            pygame.draw.rect(screen, Tooltip.colour, self.mouse.tip.rect)
 
            for i in self.mouse.tip.texts:
                Text.colour = (128, 128, 180)
                for ent in self.button_list:
                    if ent.ec.rect.collidepoint(self.mouse.pos.tup()):
                        for key, value in ent.building.bc.res_cost.items():
                                if ent.building.bc.res_cost[key] > self.res[key]:
                                    Text.colour = (255, 64, 64)
                i.draw(screen)

        #draw sun. Note 2 calcs for edge cases
        if self.cam.offset.x > (COL_COUNT*BG_TILE_SIZE)/2 - SCREEN_WIDTH:
            print("dfjjd")
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.sunlight.rect.x +5000 , self.sunlight.rect.y, self.sunlight.rect.w, self.sunlight.rect.h))
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.sunlight.rect)

        
    def _update_char(self, char: Character):
        if char.cc.aim == char.ec.rect:
            for building in self.buildings:
                if pygame.Rect.colliderect(char.ec.rect, building.ec.rect):
                    if len(building.bc.workers) < building.bc.worker_cap:
                        building.bc.add_worker(char.ec.ID)
                        char.ec.visible = False
                        break
            char.cc.aim = I_Vec2(-1, -1)

        if char.ec.rect.x >= COL_COUNT*BG_TILE_SIZE:
            char.ec.rect.x = 1
        if char.ec.rect.x < 0:
            char.ec.rect.x = COL_COUNT*BG_TILE_SIZE - 1

        if char.cc.aim.x >= 0 or char.cc.aim.y >= 0:
            
            if (char.cc.aim.x > 4000 and char.ec.rect.x < 1000):
                char.ec.rect.x -= char.cc.vel.x
            elif char.ec.rect.x > 4000 and char.cc.aim.x < 1000:
                char.ec.rect.x += char.cc.vel.x
            elif char.cc.aim.x > char.ec.rect.x:
                char.ec.rect.x += char.cc.vel.x
            elif char.cc.aim.x < char.ec.rect.x:
                char.ec.rect.x -= char.cc.vel.x

            if char.cc.aim.y > char.ec.rect.y:
                char.ec.rect.y += char.cc.vel.y
            elif char.cc.aim.y < char.ec.rect.y:
                char.ec.rect.y -= char.cc.vel.y


    def _update_buiding(self, building: Building):
        self.res = building.bc.update_level_res(self.res)
        

    def _update_mouse(self):
        self.mouse.update_pos()
        if self.mouse.building != None:
            self.mouse.building.ec.rect.x, self.mouse.building.ec.rect.y = self.mouse.pos.x - self.mouse.pos.x%BG_TILE_SIZE, self.mouse.pos.y - self.mouse.pos.y%BG_TILE_SIZE
        self.mouse.tip.visible = False
        for ent in chain(self.buildings, self.button_list):
            if ent.ec.rect.collidepoint(self.mouse.pos.tup()):
                self.mouse.tip.visible = True
                self.mouse.tip.rect.x, self.mouse.tip.rect.y = ent.ec.rect.x + ent.ec.rect.w, ent.ec.rect.y
                if type(ent) == Building:
                    self.mouse.tip.texts = []
                    self.mouse.tip.rect.w = 180
                    self.mouse.tip.rect.h = 80
                    self.mouse.tip.texts.append(Text(building_type[ent.bc.b_type], 
                                                I_Vec2(self.mouse.tip.rect.x + 10, self.mouse.tip.rect.y)))
                    self.mouse.tip.texts.append(Text(f"Workers: {len(ent.bc.workers)}/{ent.bc.worker_cap}",
                                                I_Vec2(self.mouse.tip.rect.x + 10, self.mouse.tip.rect.y + 40)))
                    for key, value in ent.bc.res.items():
                        if ent.bc.res[key] != 0:
                            self.mouse.tip.rect.h += 40
                            timer = int(100*ent.bc.res_time[key]/ent.bc.res[key])
                            self.mouse.tip.texts.append(Text(f"{key.strip()}+1: {timer}%",
                                I_Vec2(self.mouse.tip.rect.x + 10, self.mouse.tip.rect.y + 80)))
                    
                elif type(ent) == Buttons:
                    self.mouse.tip.texts = []
                    self.mouse.tip.rect.w = 180
                    self.mouse.tip.rect.h = 80
                    self.mouse.tip.texts.append(Text(building_type[ent.building.bc.b_type], 
                                                I_Vec2(self.mouse.tip.rect.x + 10, self.mouse.tip.rect.y)))
                    for key, value in ent.building.bc.res_cost.items():
                        if ent.building.bc.res_cost[key] != 0:
                            self.mouse.tip.texts.append(Text(f"cost: {value} {key}", 
                                                        I_Vec2(self.mouse.tip.rect.x + 10, self.mouse.tip.rect.y + 40)))
                            
                break

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

    def _update_text(self):
        self.UI_text = []
        offset = (SCREEN_WIDTH/len(resources.items()))
        for i, (key, value) in enumerate(self.res.items()):
            if key != "Pop. ":
                self.UI_text.append(Text(f"{key}: {value}", I_Vec2(i*offset + 40, SCREEN_HEIGHT - TOOLBAR_HEIGHT+4)))
            else:
                blood_str = "Blood"
                self.UI_text.append(Text(f"{key}: {value}/{self.res[blood_str]}", I_Vec2(i*offset + 25, SCREEN_HEIGHT - TOOLBAR_HEIGHT)))

    def _update_sunlight(self):
        self.sunlight.timer += (1000/FPS)
        if self.sunlight.timer >= self.sunlight.update_time:
            self.sunlight.timer = 0
            self.sunlight.sl_pos.x += BG_TILE_SIZE
        self.sunlight.rect.x = self.sunlight.sl_pos.x - self.cam.offset.x
        if self.sunlight.rect.x >= COL_COUNT*BG_TILE_SIZE:
            self.sunlight.rect.x = 0
        for char in self.chars:
            if self.sunlight.rect.colliderect(pygame.Rect(char.ec.rect.x - self.cam.offset.x, char.ec.rect.y, char.ec.rect.w, char.ec.rect.h)):
                char.kill()
        for  ent in chain(self.background, self.buildings):
            pass
            #update spritesheet frame
            #if building: kill workers
    def update(self):
        self._update_camera()
        self._update_mouse()
        self._update_text()
        for building in self.buildings:
            self._update_buiding(building)
        for character in self.chars:
            self._update_char(character)
        self._update_sunlight()

    def left_click(self):
        self.mouse.update_pos()

        self.mouse.deselect()

        for button in self.button_list:
            for key, value in resources.items():
                if self.res[key] >= button.building.bc.res_cost[key]: 
                    if button.ec.rect.collidepoint(self.mouse.pos.tup()):
                            button.btc.selected = True
                            self.mouse.building = button.building
                            self.mouse.ent_type = type(self.mouse.building)

        for ent in self.chars:
            wrap_offset = 0
            if ent.ec.rect.x < self.mouse.pos.x + self.cam.offset.x < ent.ec.rect.x + ent.ec.rect.w:
                if ent.ec.rect.y < self.mouse.pos.y + self.cam.offset.y < ent.ec.rect.y + ent.ec.rect.h:
                    self.mouse.ent_ID = ent.ec.ID
                    self.mouse.ent_type = type(ent)

            if self.cam.offset.x > (COL_COUNT*BG_TILE_SIZE - SCREEN_WIDTH):
                if ent.ec.rect.x < self.mouse.pos.x + self.cam.offset.x - COL_COUNT*BG_TILE_SIZE< ent.ec.rect.x + ent.ec.rect.w:
                    if ent.ec.rect.y < self.mouse.pos.y + self.cam.offset.y < ent.ec.rect.y + ent.ec.rect.h:
                        self.mouse.ent_ID = ent.ec.ID
                        self.mouse.ent_type = type(ent) 

    def right_click(self):
        self.mouse.update_pos()

        for button in self.button_list:
            button.btc.selected = False
            
        if self.mouse.ent_type is Character:
            for char in self.chars:
                if char.ec.ID == self.mouse.ent_ID:
                    char.cc.aim = I_Vec2(self.mouse.pos.x + self.cam.offset.x, self.mouse.pos.y + self.cam.offset.y)
        
        if self.mouse.ent_type is Building:
            can_place: bool = True
            for building in self.buildings: #Check no building already on square
                if building.ec.rect.x == self.mouse.building.ec.rect.x and building.ec.rect.y == self.mouse.building.ec.rect.y:
                    can_place = False
            if can_place:
                for key, value in resources.items():
                    self.res[key] -= button.building.bc.res_cost[key]
                self.buildings.append(Building(3, I_Vec2(self.mouse.pos.x - self.mouse.pos.x%BG_TILE_SIZE, self.mouse.pos.y - self.mouse.pos.y%BG_TILE_SIZE)))

        for building in self.buildings:
            if len(building.bc.workers) > 0 and self.mouse.ent_ID == None:
                if building.ec.rect.collidepoint(self.mouse.pos.tup()):
                    rm_id = building.bc.rm_worker()
                    for char in self.chars:
                        if char.ec.ID == rm_id:
                            char.ec.visible = True
                            char.ec.rect.x = building.ec.rect.x - BG_TILE_SIZE
                            char.ec.rect.y = building.ec.rect.y
                            break

        self.mouse.deselect()




def level_append(level: Level):

    tile_list = ["./res/trees_1.png", "./res/grass_1.png"]
    
    
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):                                                                                           
            level.add_bg_tile(random.choice(tile_list), y)
    
    level.add_char("./res/testchar.png", I_Vec2(200, 100))

    level.add_char("./res/testchar.png", I_Vec2(200, 200))
    level.add_char("./res/testchar.png", I_Vec2(300, 200))
    level.add_char("./res/testchar.png", I_Vec2(300, 300))



    level.button_list.append(Buttons(I_Vec2(100, 605), "./res/house_button.png", 1))
    
    level.button_list.append(Buttons(I_Vec2(200, 605), "./res/blood_button.png", 1))
  
    level.button_list.append(Buttons(I_Vec2(300, 605), "./res/mine_button.png", 3))  
    
    level.button_list.append(Buttons(I_Vec2(400, 605), "./res/lumber_mill_button.png", 4))
 
    level.button_list.append(Buttons(I_Vec2(500, 620), "./res/arrow_left.png", 1))
      
    level.button_list.append(Buttons(I_Vec2(600, 620), "./res/arrow_left.png", 1))

    offset = (SCREEN_WIDTH/len(resources.items()))

    for i, (key, value) in enumerate(level.res.items()):
        if key != "Pop. ":
            level.UI_text.append(Text(f"{key}: {value}", I_Vec2(i*offset + 40, SCREEN_HEIGHT - TOOLBAR_HEIGHT+4)))
        else:
            blood_str = "Blood"
            level.UI_text.append(Text(f"{key}: {value}/{level.res[blood_str]}", I_Vec2(i*offset + 25, SCREEN_HEIGHT - TOOLBAR_HEIGHT)))


        

        


