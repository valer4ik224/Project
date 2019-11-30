import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, settings, character):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.character = character
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = character.rect.centerx
        self.rect.top = character.rect.top
        self.move_x = 0
        self.move_y = 0

    def update(self):
        self.rect.y += self.move_y
        self.rect.x += self.move_x

        # if self.character.last_move == 'top':
        #     self.rect.y -= self.settings.bullet_speed
        # if self.character.last_move == 'bottom':
        #     self.rect.y += self.settings.bullet_speed
        # if self.character.last_move == 'right':
        #     self.rect.x += self.settings.bullet_speed
        # if self.character.last_move == 'left':
        #     self.rect.x -= self.settings.bullet_speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)