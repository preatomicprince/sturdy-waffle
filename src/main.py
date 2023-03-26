import pygame
from pathlib import Path
import sys
from definitions import F_Vec2, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, ROW_COUNT, COL_COUNT, TOOLBAR_HEIGHT
from level import Level
from UI import Buttons
from resource import resources

  
"""these are all the key events and clicks"""
def events():
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
                pass
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pass
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                pass
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pass
   
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            
        if event.type == pygame.KEYUP:
        
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pass
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pass
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                pass
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                pass
            

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
        events()
        level.draw(screen)
        
        """this draws the buttons onto the screen"""
        for i in level.button_list:
            i.draw(screen)
        
        offset = (SCREEN_WIDTH/len(resources.items()))/2
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0,0, SCREEN_WIDTH, TOOLBAR_HEIGHT))
        for i, (key, value) in enumerate(resources.items()):
            text = f"{key}: {value}"
            name_res = pygame.font.Font(Path("./res/themponewst.ttf"), 25)
            text_surface = name_res.render(text, False, (64, 64, 64))
            rect_surf = text_surface.get_rect()
            offset = i*(SCREEN_WIDTH/len(resources.items())) + 25
            rect_surf.x = offset
            screen.blit(text_surface, rect_surf)
            rect_surf.w = SCREEN_WIDTH
            rect_surf.x = 0
            print(f"{rect_surf.h}\n")
        
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Can add FPS argument to limit framerate
        #END GAME LOOP

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
    