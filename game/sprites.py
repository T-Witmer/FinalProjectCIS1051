from turtle import color
import pygame
import random
from settings import *
vec = pygame.math.Vector2

#followed a tutorial on vectors for this code
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/Player_Blue.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/ 2)
        self.orig_img = self.image
        self.pos = vec(width/2, height/ 2) #spawns in the center of the screen
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 1

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.health -= 1

    def update(self):
  

        self.acc = vec(0,0)
        keys = pygame.key.get_pressed() #dictionary of keys being pressed
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

        self.rect.center = self.pos
        
        _ , angle = (pygame.mouse.get_pos()-self.pos).as_polar()
        self.image = pygame.transform.rotozoom(self.orig_img, -angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        #got this bit from stack overflow, I could not figure out these vectors myself
        #https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d

redship = pygame.image.load("assets/Redenemy.png")
blueship = pygame.image.load("assets/Blueenemy.png")

'''
class enemy2(pygame.sprite.Sprite):
     def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = redship
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,width), random.randint(0,height))
        self.vel = 2
        self.orig_img = self.image
        self.pos = vec(self.rect.center)

'''
class enemy1(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = redship
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,width), random.randint(0,height))
        self.vel = 5
        self.orig_img = self.image
        self.pos = vec(self.rect.center)
        self.health = 1
        
    def look(self,player):

        _ , angle = (player.pos -self.pos).as_polar()
        
        return angle
        #got this bit from stack overflow, I could not figure out these vectors myself changed it so it follows player
        #https://gamedev.stackexchange.com/questions/132163/how-can-i-make-the-player-look-to-the-mouse-direction-pygame-2d


    def follow(self,player):
        # Find direction vector (dx, dy) between enemy and player.
        if self.vel > 5:
            self.vel = 5
        dirvect = vec(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        
        dirvect.normalize()
        dirvect.scale_to_length(5)
        
        self.rect.move_ip(dirvect)
    
    #got this code from https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame 

    def update(self,player):
        self.look(player)
        self.follow(player)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,width), random.randint(0,height))
        self.vel = 5
        self.orig_img = self.image
        self.pos = vec(self.rect.center)
        self.health = 1