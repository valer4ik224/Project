import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, settings, character):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.character = character
        self.image = pygame.image.load('images/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.bullet_width, settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top
        self.move_x = 0
        self.move_y = 0

    def update(self):
        self.rect.y += self.move_y
        self.rect.x += self.move_x

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)