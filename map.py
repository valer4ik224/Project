import pygame
from pygame.sprite import Sprite


class Soil(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/soil.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)