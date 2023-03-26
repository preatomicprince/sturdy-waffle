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
from resource import Resources

build_type = {1:"House", 2:"Blood_Farm", 3:"Mine", 4:"Lumber_Mill", 5:"Stable", 6:"Lab"}
class Build_Comp:
    def __init__(self, type: int)->None:
        self.res = Resources()
        self.workers: list(Ent_Comp.ID) = []

    def add_worker(ec_ID: int)->None:
        self.workers.append(ec_ID)

    def rm_worker()->int:
        return self.workers.pop()
    
    def get_img_str(type: int)->str:
        """Return location of building png"""

        if build_type[type] == "House":
            return "../res/house.png"
        elif build_type[type] == "Blood_Farm":
            return "../res/bloodfarm.png"
        elif build_type[type] == "Mine":
            return "../res/mine.png"
        elif build_type[type] == "Lumber_Mill":
            return "../res/lumbermill.png"
        elif build_type[type] == "Stable":
            return "../res/stable.png"
        elif build_type[type] == "Lab":
            return "../res/lab.png"
        else: 
            return None
                
class Building:
    def __init__(selfpos: F_Vec2, type: int)->None:
        self.bc = Build_Comp()
        self.ec = ent_comp(self.bc.get_img_str(), pos)
        self.ic = Interact_Comp()
        
        