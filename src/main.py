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

        """this will be the menu"""
        if level.state == True and level.game == True:
            pass

        
        
        if level.state == False and level.game == True:
            events(level)
            level.update()
            level.draw(screen)
            
            
        """this is if you win the level"""
        if level.state == False and level.game == False:
            events(level)
            end_text = Text("You win", I_Vec2(100, 100))
            screen.fill((0, 0, 0))
            end_text.draw(screen)
        
        """this is if you lose the game. it will need a quit option and a restart button"""
        if level.state == True and level.game == True:
            events(level)
            end_text = Text("You lose", I_Vec2(100, 100))
            screen.fill((0, 0, 0))
            end_text.draw(screen)
        
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Added FPS argument to limit framerate

    #END GAME LOOP
    
if __name__ == "__main__":
    main()
    