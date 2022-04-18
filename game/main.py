import pygame
import random
from settings import *
from sprites import *



class Game:
    def __init__(self):
    #game window and other stuff
        pygame.init()
        
        self.WIN = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.running = True
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player =Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
    #game loop
        
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()


    def update(self):
    #update for game loop
        self.all_sprites.update()
    
    def events(self):
    #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        
    def draw(self):
    #game loop draw
        self.WIN.fill("black")  
        self.all_sprites.draw(self.WIN)
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