import pygame
import os


win_width = 700
win_height = 500
def create_path (filename):
    path = os.path.join(os.path.abspath(__file__ + "/.."), filename)
    return path

class Settings:
    def __init__(self, filename, x, y, w, h, speed):
        self.width = w
        self.height = h
        self.image = pygame.transform.scale(pygame.image.load(create_path(filename)), (self.width,self.height))
        self.rect = self.image.get_rect()
