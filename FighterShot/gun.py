import pygame
import math

class Gun(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.og_image = pygame.image.load("gun.png").convert_alpha()
        self.image = pygame.image.load("gun.png").convert_alpha()
        self.rect = self.image.get_rect(midleft = pos)
    def rotate(self):
         mouse_x, mouse_y = pygame.mouse.get_pos()
         res_x, res_y = mouse_x - self.rect.x, mouse_y - self.rect.y
         angle = (180/math.pi)* -math.atan2(res_y, res_x) + 180
         self.image = pygame.transform.rotate(self.og_image,int(angle))
         self.rect = self.image.get_rect(center=(self.rect.x,self.rect.y))





