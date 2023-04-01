from pathlib import Path
import pygame
from pygame import mixer

"""this starts pygames music stuff"""
mixer.init()

class Music:
    def __init__(self, name, file_loc):
        self.file_loc = file_loc
        
    def play_music(self):
        self.name = pygame.mixer.Sound(self.file_loc)
        self.name.play(-1)
    def loading(self):
        pygame.mixer.music.load(self.file_loc)
        
track = Music("intro_music", "./res/tracklist_1.wav")



"""this is for effects"""
class Sounds:
    def __init__(self, name, file_loc):
        self.name = name
        self.file_loc = file_loc
        
    def doit(self):
        self.name = pygame.mixer.Sound(self.file_loc)
        self.name.play()
        
click_s = Sounds("skiingsound", "./res/click_sound.wav")
death_s = Sounds("skiingsound", "./res/possible death sound.wav")
