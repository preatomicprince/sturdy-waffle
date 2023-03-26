import pygame
import sys
from definitions import F_Vec2, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, ROW_COUNT, COL_COUNT
from level import Level
from UI import Buttons, button_list

  
"""these are all the key events and clicks"""
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
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
            level.add_bg_tile("../res/factory.png", y)
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
        """this draws the buttons onto the screen"""
        """for i in button_list:
            i.draw(screen)"""
            
        level.draw(screen)
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Can add FPS argument to limit framerate
        #END GAME LOOP

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
    