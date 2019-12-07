import pygame
from pygame.sprite import Sprite


class Soil(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/soil.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Stone(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/stone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
class Water(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/water.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)
class Chest(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/chest.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Heart(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/Heart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Door(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/door.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)

