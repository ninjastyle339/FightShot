import pygame, math
from settings import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos,x_start,y_start):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill("chocolate")
        self.rect = self.image.get_rect(center = pos)


        self.rect.x = x_start
        self.rect.y = y_start
        self.float_x = x_start
        self.float_y = y_start
        mouse_x, mouse_y = pygame.mouse.get_pos()
        res_x, res_y = mouse_x - self.rect.x, mouse_y - self.rect.y
        angle = math.atan2(res_y, res_x)
        velocity = 5
        self.dx = math.cos(angle) * velocity
        self.dy = math.sin(angle) * velocity

    def update(self):
        self.float_y += self.dy
        self.float_x += self.dx
        self.rect.x = (self.float_x)
        self.rect.y = (self.float_y)

        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.kill()
        if self.rect.y > HEIGHT or self.rect.y < 0:
            self.kill()
