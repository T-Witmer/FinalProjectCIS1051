import pygame
import random
import time
import os

pygame.font.init()
#window size
width ,  height = 750, 750
WIN = pygame.display.set_mode(size= (width, height))
vec = pygame.math.Vector2

#loading assets
#ships
redShip = pygame.image.load(os.path.join("assets", "Player_Red.png"))
blueShip = pygame.image.load(os.path.join("assets", "Player_Blue.png"))
#projectiles
laser = pygame.image.load(os.path.join("assets", "laser.png"))
#backround
space = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space.png")), (width,height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = redShip
        
        self.pos = vec(width/2, height /2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = vec(0, 0)
        if keys[pygame.K_a]:
           self.acc.x = -0.5

        if keys[pygame.K_d]:    
            self.acc.x = 0.5

        if keys[pygame.K_w]:
            self.acc.y = -.5

        if keys[pygame.K_s]:
            self.acc.y =  .5
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
def main():
    run =  True
    fps = 60
    level = 1
    lives = 3
    font = pygame.font.Font("assets/8514fix.fon", 35)
    player = Player()
    player.__init__()
    clock = pygame.time.Clock() #clock speed to regulate fps on all computers

    def redraw_window():  #Good practice to seperate different type of events in functions
        WIN.blit(space, (0,0))

        #text
        lives_counter = font.render(f"lives: {lives}", 1, (255,255,255))
        level_counter = font.render(f"level: {level}", 1, (255,255,255))
        
        WIN.blit(level_counter, (10, 10))
        WIN.blit(lives_counter, (10, 30))
        player.update()
        pygame.display.update()
    
    while run:
        clock.tick(fps)
        redraw_window()
        for frame in pygame.event.get():
            if frame.type == pygame.QUIT:
                run = False
                
            if frame.type == pygame.KEYDOWN:
                pass
    
        player.update()



main()












