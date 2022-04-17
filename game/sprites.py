import pygame
from settings import *

blueShip = pygame.image.load("assets/Player_Blue.png")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blueShip
    
    def update(self):
        self.vel = (0,0)



