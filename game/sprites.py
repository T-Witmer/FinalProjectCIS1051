import pygame
import math
from settings import *
vec = pygame.math.Vector2

#followed a tutorial on vectors for this code
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/Player_Blue.png")
        self.image = pygame.transform.scale(self.image,(width/15,height/15))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/ 2)
        self.orig_img = self.image
        self.pos = vec(width/2, height/ 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:

            self.acc.x = -acceleration
            if self.vel.x < -maxvelocity:
                self.acc.x = 0
            if self.pos.x < 0 + width/15/2:
                self.vel.x = 0
                self.acc.x = 0

        if keys[pygame.K_d]:
            self.acc.x = acceleration
            if self.vel.x > maxvelocity:
                self.acc.x = 0  
            if self.pos.x > width - width/15/2:
                self.vel.x = 0
                self.acc.x = 0

        if keys[pygame.K_w]:
            self.acc.y = -acceleration
            if self.vel.y < -maxvelocity:
                self.acc.y = 0
            if self.pos.y < 0 + height /15/2:
                self.vel.y = 0
                self.acc.y = 0

        if keys[pygame.K_s]:
            self.acc.y = acceleration
            if self.vel.y > maxvelocity:
                self.acc.y = 0
            if self.pos.y > height - height/15/2:
                self.vel.y = 0
                self.acc.y = 0


        self.acc += self.vel * deacceleration
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        #following mouse for turning
        pos1, pos2 = pygame.mouse.get_pos()

        self.rect.center = self.pos
        
        _ , angle = (pygame.mouse.get_pos()-self.pos).as_polar()
        self.image = pygame.transform.rotozoom(self.orig_img, -angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        #got this bit from stack overflow, I could not figure uot these vectors myself
        
  