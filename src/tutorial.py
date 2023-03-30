import pygame
from UI import *

tute = True
left_text = Text("Press left or write to scroll", I_Vec2(100, 100))
build_text = Text("The buildings and their cost are at the bottom", I_Vec2(100, 100))
res_rext = Text("Your resource counter is underneath there", I_Vec2(100, 100))
icon_text = Text("Click the icon with the left button and place with the right", I_Vec2(100, 100))
vamp_text = Text("Left click vampires to select them, right click to move them", I_Vec2(100, 100))
build_text = Text("You can move vampires into buildings to produce resources", I_Vec2(100, 100))
house_text = Text("move vampires into houses to produce more vampires", I_Vec2(100, 100))
beware_text = Text("BEWARE: vampires still die during daylight even whilst in buildings", I_Vec2(100, 100))
sac_text = Text("Vampires can be sacrificed in the temple building", I_Vec2(100, 100))
ten_vamp = Text("Once ten vampires have been sacrificed in the temple the sun will be blocked out and you win the game", I_Vec2(100, 100))
ten_vamp = Text("You can see your progress in the bar above", I_Vec2(100, 100))

def Tutorial():
    if tute == True:
        pass