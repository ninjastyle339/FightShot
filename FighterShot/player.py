import pygame, random
from bullet import Bullet
from enemy import Enemy

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,floor_sprites,enemy_sprites,player_group):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill("cyan")
        self.rect = self.image.get_rect(center=pos)
        self.display_surface = pygame.display.get_surface()

        self.enemy = enemy_sprites
        self.floor = floor_sprites
        self.player = player_group

        self.direction = pygame.Vector2(0,0)
        self.gravity = 1
        self.bullet = pygame.sprite.Group()

        self.start_time = 0
        self.speed = 8
        #red health bar underneath
        self.health_bar_red = pygame.Surface((200,30))
        #Length of health bar
        self.hp = 10
        self.health_x = 20 * self.hp
        self.health_bar = pygame.Surface((self.health_x,30))
        #Player HP
        # = 10

        self.font = pygame.font.Font("slkscrb.ttf",30)

        self.health_bar_red.fill("red")
        self.health_bar.fill("forestgreen")
        self.health_bar_red_rect = self.health_bar_red.get_rect(topleft=(0,30))
        self.health_bar_rect = self.health_bar.get_rect(topleft=(0,30))
    def health_bar_show(self):
        self.display_surface.blit(self.health_bar_red, self.health_bar_red_rect)
        self.display_surface.blit(self.health_bar,self.health_bar_rect)
        self.health_x = 20 * self.hp

        health_text = self.font.render("Player Health: ",False,"antiquewhite")
        health_text_rect = health_text.get_rect(topleft=(0,0))
        self.display_surface.blit(health_text, health_text_rect)
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    def shoot(self):
        #if I put shoot function in input then self.direction.x != 0 when space key is held
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            time = pygame.time.get_ticks() - self.start_time

            if time > 200:
                bullet = Bullet((self.rect.x,self.rect.y),self.rect.x,self.rect.y)
                self.bullet.add(bullet)

                self.start_time = pygame.time.get_ticks()
    def bullet_collision(self):
        for sprite in self.floor:
            if pygame.sprite.spritecollide(sprite,self.bullet,True):
                pass
        for sprite in self.enemy:
            if pygame.sprite.spritecollide(sprite,self.bullet,True):
                sprite.hp -= 1
        if pygame.sprite.spritecollide(self.player.sprite,self.enemy,True):
            self.hp -= 1
            self.health_bar = pygame.Surface((self.health_x, 30))
            self.health_bar.fill("forestgreen")



    def move(self):
        self.input()
        self.direction.y += self.gravity



    def update(self):

        self.bullet.draw(self.display_surface)

        self.bullet.update()

        self.shoot()
        self.bullet_collision()
        self.health_bar_show()
        self.move()

