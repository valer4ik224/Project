import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, screen, settings, character):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top

    def update(self):
        self.rect.y -= self.settings.bullet_speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)