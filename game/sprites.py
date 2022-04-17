import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/ 2)

        self.pos = vec(width/2, height/ 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    
    def update(self):
        self.acc = (0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x -= -0.5
        if keys[pygame.K_d]:
            self.acc.x += 0.5

        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        self.rect.center = self.pos


