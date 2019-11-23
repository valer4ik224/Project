import pygame


class Character():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 45)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()



        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.character_speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.settings.character_speed
        if self.moving_up == True and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.settings.character_speed
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.character_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)


