import pygame
import random
from settings import *
from sprites import *

#Followed tutorial for structure of files

class Game:
    def __init__(self):
    #game window and other stuff
        pygame.init()
        
        self.WIN = pygame.display.set_mode((width,height))
        self.bg = pygame.image.load("assets/space.png")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def new(self):
        self.score = 0
        self.level = 3
        self.all_sprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
    #game loop
        
        enemies = []

        if len(enemies) == 0:
            self.score += 100
            self.level += 1

            for i in range(self.level):
                self.enemy1 = enemy1()
                enemies.append(self.enemy1)
                self.enemySprites.add(self.enemy1)
                

        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
            
            


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
        
    def draw(self):
    #game loop draw
        enemies = []
        self.WIN.blit(pygame.transform.scale(self.bg, (width,height)), (0,0))
        self.all_sprites.draw(self.WIN)
        self.enemySprites.draw(self.WIN)

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

