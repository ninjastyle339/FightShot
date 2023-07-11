import pygame
import math
import random
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,player,speed,size,hp):
        super().__init__()
        self.image = pygame.Surface((size))
        self.image.fill("green")
        self.rect = self.image.get_rect(center=pos)
        self.player = player

        self.speed = speed
        self.max_hp = hp
        self.hp = hp

        #glow
        self.glow = pygame.Surface((size[0] + 5,size[1] + 5))
        self.glow.fill("green")
        self.glow_rect = self.glow.get_rect(center=pos)
        self.display = pygame.display.get_surface()

    def move_to_player(self):

        player = self.player.sprite
        dx,dy = player.rect.x - self.rect.x,player.rect.y - self.rect.y
        distance = math.hypot(dx,dy)
        #Float division by 0 fix
        if distance < 0.5:
            distance = 0.5
        dx,dy = dx/distance, dy/distance
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    def death(self):
        if self.hp == self.max_hp / 2:
            self.image.fill("yellow")
        if self.hp <= self.max_hp / 3:
            self.image.fill("red")
        if self.hp <= 0:
            self.kill()





    def update(self):
        #glow
        self.glow_rect.x = self.rect.x - 3
        self.glow_rect.y = self.rect.y - 2.5
        self.display.blit(self.glow,self.glow_rect,special_flags=pygame.BLEND_RGB_ADD)
        self.death()
        self.move_to_player()

