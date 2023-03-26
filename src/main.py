import pygame
import sys
from definitions import SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level
from building import Enum_Build

def main()->None:
    """
    Initialise pygame

    main game loop:
        1.Handle events
        2.


    quit and exit
    """

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #level = Level()
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick() #Can add FPS argument to limit framerate
        #END GAME LOOP

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    #main()
    print(Enum_Build.Blood_Farm == 1)
    