import pygame
import sys
from definitions import F_Vec2, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, ROW_COUNT, COL_COUNT
from level import Level

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        level.draw(screen)
        pygame.display.update()
        #print(clock.get_fps())
        clock.tick() #Can add FPS argument to limit framerate
        #END GAME LOOP

    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
    