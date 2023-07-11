import pygame
class Floor(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill("black")
        self.rect = self.image.get_rect(center=pos)
        self.hp = 5
