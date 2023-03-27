import pygame
from pathlib import Path
import sys
from definitions import *
from level import Level
from UI import Buttons, Text
from resource import resources

  
"""these are all the key events and clicks"""
def events(level: Level):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("pressed")
            if event.button == 3:
                print("right")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                level.keys_down.left = True
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                level.keys_down.right = True
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                level.keys_down.up = True
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                level.keys_down.down = True
   
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            
        if event.type == pygame.KEYUP:
        
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                level.keys_down.left = False
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                level.keys_down.right = False
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                level.keys_down.up = False
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                level.keys_down.down = False
            

def main()->None:
    """
    Initialise pygame

    main game loop:
        1.Handle events
        2.Update entities[TODO]
        3.Draw


    quit and exit
    """

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level()
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):                                                                                           
            level.add_bg_tile("./res/test.png", y)
    
    house_button = Buttons(100, 620, "button",Path("./res/house_button.png"), 1)
    level.button_list.append(house_button)
    
    blood_farm_button = Buttons(200, 650, "button",Path("./res/arrow_left.png"), 1)    
    level.button_list.append(blood_farm_button)

    mine_button = Buttons(300, 650, "button",Path("./res/arrow_left.png"), 1)  
    level.button_list.append(mine_button)  

    lumber_mill_button = Buttons(400, 650, "button",Path("./res/arrow_left.png"), 1)    
    level.button_list.append(lumber_mill_button)

    stable_button = Buttons(500, 650, "button",Path("./res/arrow_left.png"), 1)  
    level.button_list.append(stable_button)
      
    lab_button = Buttons(600, 650, "button",Path("./res/arrow_left.png"), 1)  
    level.button_list.append(lab_button)

    offset = (SCREEN_WIDTH/len(resources.items()))
    for i, (key, value) in enumerate(resources.items()):
            level.UI_text.append(Text(f"{key}: {value}", I_Vec2(i*offset + 25, 0)))

    
    running = True
    
    """
    *////////////////////////*
    *\\\\\\\\\\\\\\\\\\\\\\\\*
    *//                    //*
    *\\   MAIN GAME LOOP   \\*
    *//   ^^^^^^^^^^^^^^   //*
    *\\\\\\\\\\\\\\\\\\\\\\\\*
    *////////////////////////*
    """
    pygame.init()

    #BEGIN GAME LOOP
    while running:
        """this checks for clicks and keyevents"""
        events(level)
        level.draw(screen)
        
        """this draws the buttons onto the screen"""
        for i in level.button_list:
            i.draw(screen)            
        
        level.update()
        
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Can add FPS argument to limit framerate
        #END GAME LOOP
    
if __name__ == "__main__":
    main()
    