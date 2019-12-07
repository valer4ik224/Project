import pygame
from pygame.sprite import Sprite

class Enemie(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 225 )
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height




    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.settings.enemie_speed * self.settings.fleet_direction
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True