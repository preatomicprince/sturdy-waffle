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
    game = True
    
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
    pygame.display.set_caption("In the Dark")
    track.play_music()
    #BEGIN GAME LOOP
    while running:
<<<<<<< HEAD
        """this will be the menu"""
        if state == True and game == True:
=======
        
<<<<<<< HEAD
        events(level)
        level.update()
        level.draw(screen)
=======
        if state == True:
>>>>>>> 0c1c5f7155c2efbd814f01d90c8664a45c67d8aa
            pass
        
        
        if state == False and game == True:
            events(level)
            level.update()
            level.draw(screen)
            
            bar.drawing(screen)
<<<<<<< HEAD
        
        """this is if you win the level"""
        if state == False and game == False:
            pass
        
        """this is if you lose the game. it will need a quit option and a restart button"""
        if state == True and game == True:
            pass
        
=======
>>>>>>> 9998205fbdf6fa7a1109020348aea3808734311e
>>>>>>> 0c1c5f7155c2efbd814f01d90c8664a45c67d8aa
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Added FPS argument to limit framerate

    #END GAME LOOP
    
if __name__ == "__main__":
    main()
    