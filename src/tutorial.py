import pygame
from UI import *
"pop cap determined by blood, for every blood one more vampire can be produced"
tute = True
left_text = Text("Press left, right or a and d keys to scroll", I_Vec2(10, 40))
build1_text = Text("Left click to select units on the map, or buildings from the menu", I_Vec2(10, 80))
res_text = Text("Right click to move a unit to a location, or place a unit in a building", I_Vec2(10, 120))
icon_text = Text("Right click to place buildings selected from the menu, and to empty occupied ", I_Vec2(10, 160))
vamp_text = Text("buildings.", I_Vec2(10, 200))
build_text = Text("You can move vampires into buildings to produce resources. Move vampires into", I_Vec2(10, 240))
house_text = Text("houses to produce more vampires. BEWARE: vampires die in sunlight, even whilst in", I_Vec2(10, 280))
house_text1 = Text("buildings", I_Vec2(10, 320))
beware_text = Text("", I_Vec2(10, 360))
sac_text = Text("Vampires can be sacrificed in the pyramid building", I_Vec2(10, 400))
ten_vamp_text = Text("Once a certain amount of vampires have been sacrificed in the temple the ", I_Vec2(10, 440))
bar_vamp_text = Text("sun will be blocked out and you win the game. You can see your progress in the bar", I_Vec2(10, 480))
bar_vamp_text1 = Text("above the map", I_Vec2(10, 520))
bar_vamp_text3 = Text("", I_Vec2(10, 560))
bar_vamp_text2 = Text("Your population cap is determined by the amount of blood you have", I_Vec2(10, 600))

def Tutorial(screen):
    if tute == True:
        screen.fill((0, 0, 0))
        left_text.draw(screen)
        build1_text.draw(screen)
        res_text.draw(screen)
        icon_text.draw(screen)
        vamp_text.draw(screen)
        build_text.draw(screen)
        house_text.draw(screen)
        house_text1.draw(screen)
        beware_text.draw(screen)
        sac_text.draw(screen)
        ten_vamp_text.draw(screen)
        bar_vamp_text.draw(screen)
        bar_vamp_text1.draw(screen)
        bar_vamp_text3.draw(screen)
        bar_vamp_text2.draw(screen)
        
    else:
        pass