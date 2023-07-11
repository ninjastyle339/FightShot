import pygame,sys
from settings import *
from level import Level
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Fighter Shot")
        self.level = Level()
        self.sky = pygame.image.load("sky.jpg").convert_alpha()
        #Crosshair
        self.crosshair = pygame.image.load("crosshair.png").convert_alpha()
        pygame.mouse.set_visible(False)
        """
        self.surf = pygame.Surface((40, 40))
        self.surf.fill("blue")
        
        self.surf_rect = self.surf.get_rect(center=(400,200))

        self.glow = pygame.Surface((50, 50))
        self.glow.fill("blue")
        self.glow_rect = self.glow.get_rect(center=(400,200))
        """
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((30,30,30))
            self.screen.blit(self.sky,(0,0))
            #For crosshair
            pos = pygame.mouse.get_pos()
            self.screen.blit(self.crosshair,pos)

            #self.screen.blit(self.surf,self.surf_rect)
            #self.screen.blit(self.glow,self.glow_rect,special_flags=pygame.BLEND_RGB_ADD)
            self.level.run()
            pygame.display.flip()
            self.clock.tick(FPS)
if __name__ == "__main__":
    game = Game()
    game.run()
