import pygame
from settings import *

blueShip = pygame.image.load("assets/Player_Blue.png")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(30,40)
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/ 2)
    
    def update(self):
        self.vel = (0,0)



