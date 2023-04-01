""""
housing: sets pop cap and spawn speed
human farm: produces blood
mine: produces coal and stone
lumber mill: produces wood
stable: holds horses that can drag buildings
laboratory: Used to develop more advanced versions of buidings   
"""
import pygame
from definitions import *
from entity import Ent_Comp
from copy import copy
from character import Character
from resource import resources, Win_State, winning


building_type = {1:"House", 2:"Blood_Farm", 3:"Mine", 4:"Lumber_Mill", 5:"Pyramid", 6:"Lab"}
class Build_Comp:
    def __init__(self, b_type: int)->None:
        self.res = copy(resources) #how many milliseconds it takes to produce each resource per workers
        self.res_time = copy(resources)
        self.res_cost = copy(resources)
        self.b_type = b_type
        self.workers: list(Ent_Comp.ID) = []
        self.worker_cap = 3 #limit to number of workers 

    def add_worker(self, ec_ID: int)->None:
        if len(self.workers) < self.worker_cap:
            self.workers.append(int(ec_ID))

    def rm_worker(self)->int:
        if self.b_type != 5:
            return self.workers.pop()
        
    def update_score(self):
        winning.sp = winning.sp + len(self.workers)
        
    

    
class Building:
    def __init__(self, b_type: int, pos: I_Vec2 = I_Vec2(-1, -1))->None:
        self.bc = Build_Comp(b_type)

        if building_type[b_type] == "House":
            texture = ["./res/house.png", "./res/house_day.png"]
            self.bc.res["Pop. "] = 10000
            self.bc.res_cost["Stone"] = 50

        elif building_type[b_type] == "Blood_Farm":
            texture = ["./res/blood.png", "./res/blood_day.png"]
            self.bc.res["Blood"] = 5000 
            self.bc.res_cost["Wood"] = 50
            
        elif building_type[b_type] == "Mine":
            texture = ["./res/mine.png", "./res/mine_day.png", "./res/mine_grey.png"]
            self.bc.res["Stone"] = 5000
            self.bc.res_cost["Wood"] = 20
             

        elif building_type[b_type] == "Lumber_Mill":
            texture = ["./res/lumber_mill.png", "./res/lumber_mill_day.png", "./res/lumber_mill_grey.png"]
            self.bc.res["Wood"] = 5
            self.bc.res_cost["Wood"] = 5
            

        elif building_type[b_type] == "Pyramid":
            texture = ["./res/pyramid.png", "./res/pyramid_day.png"]
            self.bc.res_cost["Wood"] = 1
            self.bc.worker_cap = 10
            
        elif building_type[b_type] == "Lab":
            texture = "../res/lab.png"

        self.ec = Ent_Comp(texture, pos)

    def update_level_res(self, level_res: resources, level_chars)-> resources:
        for (key, value) in self.bc.res_time.items():
            if key == "Pop. " and level_res["Pop. "] >= level_res["Blood"]:
                self.bc.res_time[key] = 0
            self.bc.res_time[key] += (1000/FPS)*len(self.bc.workers)
            if self.bc.res[key] <= self.bc.res_time[key] and self.bc.res[key] > 0:
                if key == "Pop. ":
                    if level_res["Pop. "] < level_res["Blood"]:
                        level_res[key] += 1
                        self.bc.res_time[key] = 0
                        level_chars.append(Character(None, I_Vec2(self.ec.rect.x - 100, self.ec.rect.y)))
                        continue
                   
                level_res[key] += 1
                self.bc.res_time[key] = 0
        
        return level_res, level_chars

    