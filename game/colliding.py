import pygame

#Tech with tim tutorial for collisions

def collide(player,enemy1):
    offsetx = enemy1.pos.x - player.pos.x
    offsety = enemy1.pos.y - player.pos.y
    return player.mask.overlap(enemy1.mask,(offsetx,offsety)) != None