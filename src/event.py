import pygame
from level import Level
import sys

def events(level: Level)->None:
    """this checks for clicks and keyevents"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                level.left_click()
                
            if event.button == 3:
                level.right_click()
                
        
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
            