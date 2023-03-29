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
from resource import resources

building_type = {1:"House", 2:"Blood_Farm", 3:"Mine", 4:"Lumber_Mill", 5:"Stable", 6:"Lab"}
class Build_Comp:
    def __init__(self, b_type: int)->None:
        self.res = copy(resources) #how many milliseconds it takes to produce each resource per workers
        self.res_time = copy(resources)
        self.res_cost = copy(resources)
        self.b_type = b_type
        self.workers: list(Ent_Comp.ID) = []
        self.worker_cap = 3 #limit to number of workers 

    def add_worker(self, ec_ID: int)->int:
        if len(self.workers) < self.worker_cap:
            self.workers.append(ec_ID)
            return 1
        return 0

    def rm_worker(self)->int:
        return self.workers.pop()

    def update_level_res(self, level_res: resources)-> resources:
        for (key, value) in self.res_time.items():
            self.res_time[key] += (1000/FPS)*len(self.workers)
            if self.res[key] <= self.res_time[key] and self.res[key] > 0:
                level_res[key] += 1
                self.res_time[key] = 0

        return level_res

class Building:
    def __init__(self, b_type: int, pos: I_Vec2 = I_Vec2(-1, -1))->None:
        self.bc = Build_Comp(b_type)

        if building_type[b_type] == "House":
            texture = "./res/house.png"
            self.bc.res["Pop. "] = 10000
            self.bc.res_cost["Wood"] = 10

        elif building_type[b_type] == "Blood_Farm":
            texture = "../res/bloodfarm.png"
            self.bc.res["Blood"] = 5000 

        elif building_type[b_type] == "Mine":
            texture = "./res/house.png"
            self.bc.res["Stone"] = 5000
            self.bc.res["Coal"] = 15000
            self.bc.res_cost["Wood"] = 15 

        elif building_type[b_type] == "Lumber_Mill":
            texture = "./res/house.png"
            self.bc.res["Wood"] = 5
            self.bc.res_cost["Stone"] = 20

        elif building_type[b_type] == "Stable":
            texture = "../res/stable.png"
            self.bc.res["Horse"] = 30

        elif building_type[b_type] == "Lab":
            texture = "../res/lab.png"

        self.ec = Ent_Comp(texture, pos)

    