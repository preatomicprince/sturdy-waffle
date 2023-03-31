import pygame
from UI import *
"pop cap determined by blood, for every blood one more vampire can be produced"
tute = True
left_text = Text("Press left or write to scroll", I_Vec2(10, 40))
build_text = Text("The buildings and their cost are at the bottom", I_Vec2(10, 80))
res_text = Text("Your resource counter is underneath there", I_Vec2(10, 120))
icon_text = Text("Click the icon with the left button and place with the right", I_Vec2(10, 160))
vamp_text = Text("Left click vampires to select them, right click to move them", I_Vec2(10, 200))
build_text = Text("You can move vampires into buildings to produce resources", I_Vec2(10, 240))
house_text = Text("move vampires into houses to produce more vampires", I_Vec2(10, 280))
beware_text = Text("BEWARE: vampires still die during daylight even whilst in buildings", I_Vec2(10, 320))
sac_text = Text("Vampires can be sacrificed in the temple building", I_Vec2(10, 360))
ten_vamp_text = Text("Once ten vampires have been sacrificed in the temple the sun will be blocked out and you win the game", I_Vec2(10, 400))
bar_vamp_text = Text("You can see your progress in the bar above", I_Vec2(10, 440))

def Tutorial(screen):
    if tute == True:
        screen.fill((0, 0, 0))
        left_text.draw(screen)
        build_text.draw(screen)
        res_text.draw(screen)
        icon_text.draw(screen)
        vamp_text.draw(screen)
        build_text.draw(screen)
        house_text.draw(screen)
        beware_text.draw(screen)
        sac_text.draw(screen)
        ten_vamp_text.draw(screen)
        bar_vamp_text.draw(screen)
        
    else:
        pass