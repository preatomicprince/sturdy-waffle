import pygame
from pathlib import Path
import sys
from definitions import *
from level import Level, level_append
from UI import Buttons, Text
from resource import resources

def events(level: Level)->None:
    """this checks for clicks and keyevents"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                level.left_click()
                print("left\n")
            if event.button == 3:
                level.right_click()
                print("Right\n")
        
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
    Append objects to level

    Initialise pygame

    main game loop:
        1.Handle events
        2.Update entities
        3.Draw

    quit and exit
    """

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level()
    running = True

    level_append(level)
    
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
        
        events(level)
        level.update()
        level.draw(screen)

        pygame.display.update()
        #print(clock.get_fps())
        clock.tick(FPS) #Can add FPS argument to limit framerate
        #END GAME LOOP
    
if __name__ == "__main__":
    main()
    