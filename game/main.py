import pygame
import random
from settings import *
from sprites import *
from colliding import *

#Followed tutorial for structure of files
#https://www.youtube.com/watch?v=Q-__8Xw9KTM&t=4995s
#https://www.youtube.com/watch?v=pN9pBx5ln40
# These tutorials helped make this game
pygame.font.init()

class Game:
    def __init__(self):
    #game window and other stuff
        pygame.init()
        self.font = pygame.font.SysFont("",50)
        self.WIN = pygame.display.set_mode((width,height))
        self.bg = pygame.image.load("assets/space.png")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def new(self):
        self.score = 0
        self.level = 0
        self.all_sprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
    #game loop
        
        
        self.enemies = []      

        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

            

            if len(self.enemies) == 0:
                self.score += 100
                self.level += 1

                for i in range(self.level):
                    self.enemy1 = enemy1()
                    self.enemies.append(self.enemy1)
                    self.enemySprites.add(self.enemy1)

            


    def update(self):
    #update for game loop
       
        self.all_sprites.update()
        self.enemySprites.update(self.player)
        

    def events(self):
    #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        if self.player.collide(self.enemySprites) == True:
            self.player.health -= 1
            self.enemies.remove(self.enemy1)
        if self.player.health == 0:
            self.playing = False
            self.running = False

        
           
            
    def draw(self):
    #game loop draw
        enemies = []
        self.WIN.blit(pygame.transform.scale(self.bg, (width,height)), (0,0))
        self.all_sprites.draw(self.WIN)
        self.enemySprites.draw(self.WIN)
        healthLabel = self.font.render(f"health: {self.player.health}", 1, (255,255,255))
        levelLabel = self.font.render(f"Level: {self.level}",1,(255,255,255))
        self.WIN.blit(healthLabel, (10,10))
        self.WIN.blit(levelLabel,(10,40))
        pygame.display.flip()
        
    def menuScreen(self):
        pass

    def overScreen(self):
        pass

#loop for playing the game

g = Game()

while g.running:
    g.new()
    g.overScreen()

pygame.quit()

