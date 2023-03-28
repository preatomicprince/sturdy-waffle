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
from resource import resources

building_type = {1:"House", 2:"Blood_Farm", 3:"Mine", 4:"Lumber_Mill", 5:"Stable", 6:"Lab"}
class Build_Comp:
    def __init__(self, b_type: int)->None:
        self.res = resources #how many milliseconds it takes to produce each resource per workers
        self.res_time = resources
        self.workers: list(Ent_Comp.ID) = []
        self.worker_cap = 3 #limit to number of workers 
        self.clock = pygame.time.Clock()

    def add_worker(self, ec_ID: int)->int:
        if len(self.workers) < self.worker_cap:
            self.workers.append(ec_ID)
            return 1
        return 0

    def rm_worker(self)->int:
        return self.workers.pop()

    def update_level_res(self, level_res: resources)-> resources:
        for i in self.res_time:
            self.res_time[i] += self.clock.tick()

            if self.res[i] <= self.res_time[i]:
                level_res[i] += 1
                self.res_time[i] = 0

        return level_res

class Building:
    def __init__(self, b_type: int, pos: I_Vec2 = I_Vec2(-1, -1))->None:
        self.bc = Build_Comp(b_type)

        if building_type[b_type] == "House":
            texture = "./res/house.png"
            self.bc.res["pop"] = 60000

        elif building_type[b_type] == "Blood_Farm":
            texture = "../res/bloodfarm.png"
            self.bc.res["blood"] = 5000 

        elif building_type[b_type] == "Mine":
            texture = "../res/mine.png"
            self.bc.res["stone"] = 5
            self.bc.res["coal"] = 15

        elif building_type[b_type] == "Lumber_Mill":
            texture = "../res/lumbermill.png"
            self.bc.res["wood"] = 5

        elif building_type[b_type] == "Stable":
            texture = "../res/stable.png"
            self.bc.res["horse"] = 30

        elif building_type[b_type] == "Lab":
            texture = "../res/lab.png"

        self.ec = Ent_Comp(texture, pos)

    