import pygame

#Tech with tim tutorial for collisions

def collide(player,enemy):
    offsetx = enemy.x - player.x
    offsety = enemy.y - player.y
    return player.mask.overlap(enemy.mask,(offsetx,offsety)) != None