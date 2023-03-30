import pygame
from pathlib import Path
import sys
from definitions import *
from level import Level, level_append
from UI import Buttons, Text, Bar, bar
from resource import resources
from event import events
from music import *



track.loading()


def main()->None:
    """
    create main variables

    Append objects to level

    Initialise pygame

    main game loop:
        1.Handle events
        2.Update entities
        3.Draw and update display, clock

    quit and exit
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level()
    running = True
    state = False
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
    track.play_music()
    #BEGIN GAME LOOP
    while running:
        
<<<<<<< HEAD
        events(level)
        level.update()
        level.draw(screen)
=======
        if state == True:
            pass
        
        
        elif state == False:
            events(level)
            level.update()
            level.draw(screen)
            
            bar.drawing(screen)
>>>>>>> 9998205fbdf6fa7a1109020348aea3808734311e
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Added FPS argument to limit framerate

    #END GAME LOOP
    
if __name__ == "__main__":
    main()
    