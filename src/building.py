""""
housing: sets pop cap and spawn speed
human farm: produces blood
mine: produces coal and stone
lumber mill: produces wood
stable: holds horses that can drag buildings
laboratory: Used to develop more advanced versions of buidings   
"""
import pygame
from definitions import F_Vec2
from entity import Ent_Comp, Interact_Comp
from resource import resources

build_type = {1:"House", 2:"Blood_Farm", 3:"Mine", 4:"Lumber_Mill", 5:"Stable", 6:"Lab"}
class Build_Comp:
    def __init__(self, type: int)->None:
        self.res = resources() #how many milliseconds it takes to produce each resource per workers
        self.res_time = resources()
        self.workers: list(Ent_Comp.ID) = []
        self.worker_cap = 3 #limit to number of workers 
        self.clock = pygame.time.clock()

    def add_worker(ec_ID: int)->int:
        if len(self.workers) < self.worker_cap:
            self.workers.append(ec_ID)
            return 1
        return 0

    def rm_worker()->int:
        return self.workers.pop()

    def update_level_res(level_res: resources)-> resources:
        for i in self.res_time:
            self.res_time[i] += self.clock.tick()

            if self.res[i] <= self.res_time[i]:
                level_res[i] += 1
                self.res_time[i] = 0

        return level_res

class Building:
    def __init__(selfpos: F_Vec2, type: int)->None:
        self.bc = Build_Comp()

        if build_type[type] == "House":
            texture = "../res/house.png"
            self.bc.res["pop"] = 60000

        elif build_type[type] == "Blood_Farm":
            texture = "../res/bloodfarm.png"
            self.bc.res["blood"] = 5000 

        elif build_type[type] == "Mine":
            texture = "../res/mine.png"
            self.bc.res["stone"] = 5
            self.bc.res["coal"] = 15

        elif build_type[type] == "Lumber_Mill":
            texture = "../res/lumbermill.png"
            self.bc.res["wood"] = 5

        elif build_type[type] == "Stable":
            texture = "../res/stable.png"
            self.bc.res["horse"] = 30

        elif build_type[type] == "Lab":
            texture = "../res/lab.png"

        
        self.ic = Interact_Comp()
        self.ec = ent_comp(texture, pos)

    