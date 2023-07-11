import pygame, random
from settings import *
from floor import Floor
from player import Player
from gun import Gun
from enemy import Enemy
#gun recoil

class Level():
    def __init__(self):
        self.player = pygame.sprite.GroupSingle()
        self.gun = pygame.sprite.GroupSingle()

        self.enemy = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.display_surface = pygame.display.get_surface()
        self.create()
        self.currentLevel = 0
        #gun recoil
        self.start_time = 0
        #text
        self.font = pygame.font.Font("slkscrb.ttf",30)
        #timer for enemy shot
        self.enemy_shoot = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_shoot, 1000)

    def create(self):
        for row_index,row in enumerate(MAP):
            for col_index,col in enumerate(row):
                x = col_index * FLOORSIZE + 300
                y = row_index * FLOORSIZE + 300
                if col == "x":
                    floor = Floor((x,y))
                    self.floor.add(floor)
                if col == "p":
                    player = Player((x,y),self.floor,self.enemy,self.player)
                    self.player.add(player)
                if col == "e":
                    enemy = Enemy((x,y), self.player,1,(25,25),10)
                    self.enemy.add(enemy)

    def move(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        self.collision("horizontal")
        player.rect.y += player.direction.y
        self.collision("vertical")

    def collision(self,direction):
        player = self.player.sprite
        if direction == "horizontal":
            for sprite in self.floor:
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    if player.direction.x > 0:
                        player.rect.right = sprite.rect.left
        if direction == "vertical":
            for sprite in self.floor:
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0

    def load_level(self, level):
        Fast_enemy = Enemy((random.randint(0,1280),random.randint(20,400)),self.player, 2, (25,25),10)
        normal_enemy = Enemy((random.randint(0,1280),random.randint(20,400)),self.player, 1, (25,25),10)
        normal_enemy1 = Enemy((random.randint(0,1280),random.randint(20,400)), self.player, 1, (25,25),10)
        if level == 1:

            self.enemy.add(normal_enemy)
            self.enemy.add(normal_enemy1)
        if level == 2:

            self.enemy.add(Fast_enemy)
        if level == 3:
            self.enemy.add(Fast_enemy)
            self.enemy.add(normal_enemy)
        if level == 4:
            pass
        if level == 5:
            pass
    def shoot_player(self):

        if self.enemy.sprites():
            random_enemy = random.choice(self.enemy.sprites())
            bullet = Enemy(random_enemy.rect.center,self.player,6,(10,10),1)
            self.enemy.add(bullet)
    def User_interface(self):
        level_count_text = self.font.render(f"Level:{self.currentLevel}",False,"antiquewhite")
        level_count_text_rect = level_count_text.get_rect(center=(1100,20))
        self.display_surface.blit(level_count_text,level_count_text_rect)
    def add_level(self):
        if not self.enemy:
            self.currentLevel += 1
            self.load_level(self.currentLevel)
    def enemy_shoot(self):
        if self.enemy:
            pass




    def update_gun(self):
        self.start_time
        mouse_x, mouse_y = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        gun = Gun((self.player.sprite.rect.x,self.player.sprite.rect.y))
        self.gun.add(gun)
        self.gun.sprite.rect.x = self.player.sprite.rect.x
        self.gun.sprite.rect.y = self.player.sprite.rect.y

        #Move gun back every shot
        if keys[pygame.K_SPACE]:
            time = pygame.time.get_ticks() - self.start_time
            if time > 200:
                if mouse_x > 0 and mouse_y > 0:
                    self.gun.sprite.rect.x -= 10
                self.start_time = pygame.time.get_ticks()


        gun.rotate()
        self.gun.draw(self.display_surface)


    def run(self):
        self.floor.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.enemy.draw(self.display_surface)

        self.player.update()
        self.enemy.update()

        self.update_gun()

        self.add_level()
        #text
        self.User_interface()

        self.move()
        #Enemy shot
        for event in pygame.event.get():
            if event.type == self.enemy_shoot:
                self.shoot_player()