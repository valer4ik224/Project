import pygame
from pygame.sprite import Sprite


class Character(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/char1.png').convert_alpha()
        self.size = self.image.get_size()
        self.transform_value = 0.7
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*self.transform_value), int(self.size[1]*self.transform_value)))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.horizontalD = [self.load_image('images/char1.png'), self.load_image('images/char2.png'),
                            self.load_image('images/char3.png'), self.load_image('images/char4.png'),
                            self.load_image('images/char5.png')]
        self.topD = [self.load_image('images/chart1.png'), self.load_image('images/chart2.png'),
                     self.load_image('images/chart3.png'), self.load_image('images/chart4.png'),
                     self.load_image('images/chart5.png')]
        self.bottomD = [self.load_image('images/chard1.png'), self.load_image('images/chard2.png'),
                        self.load_image('images/chard3.png'), self.load_image('images/chard4.png'),
                        self.load_image('images/chard5.png')]
        self.fightR = [self.load_image('images/fr1.png'), self.load_image('images/fr2.png'),
                       self.load_image('images/fr3.png')]
        self.fightT = [self.load_image('images/fu1.png'), self.load_image('images/fu2.png'),
                       self.load_image('images/fu3.png')]
        self.fightD = [self.load_image('images/fd1.png'), self.load_image('images/fd2.png'),
                       self.load_image('images/fd3.png')]
        self.animation = 1
        self.animation2 = 0
        self.last_move = 'top'
        self.last_hit = 'zeroH'
        self.fps = 5
        self.fps2 = 3


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.attack = False
    def load_image(self, img):
        return pygame.image.load(img).convert_alpha()




    def update(self):
        if self.animation > len(self.horizontalD) * self.fps:
            self.animation = 1
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.character_speed
            self.animation += 1
            self.last_move = 'right'

        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.animation += 1
            self.last_move = 'left'

            self.rect.centerx -= self.settings.character_speed
        if self.moving_up == True and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.settings.character_speed
            self.animation += 1
            self.last_move = 'top'
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.character_speed
            self.animation += 1
            self.last_move = 'bottom'
        if self.attack == True:
            self.animation2 += 1


    def blitme(self):
        #Reset attack animation
        if len(self.fightR) <= self.animation2 // self.fps2:
            self.animation2 = 0
            self.attack = False
        #Reset move animation
        if len(self.horizontalD) <= self.animation // self.fps:
            self.animation = self.fps
        if len(self.topD) <= self.animation // self.fps:
            self.animation = self.fps
        if len(self.bottomD) <= self.animation // self.fps:
            self.animation = self.fps
        #Attack animation
        if self.attack == True:
            if self.last_move == 'right':
                self.image = self.fightR[self.animation2 // self.fps2]
            elif self.last_move == 'left':
                self.image = pygame.transform.flip(self.fightR[self.animation2 // self.fps2], True, False)
            elif self.last_move == 'top':
                self.image = (self.fightT[self.animation2 // self.fps2])
            elif self.last_move == 'bottom':
                self.image = (self.fightD[self.animation2 // self.fps2])


        elif self.last_move == 'right':
            self.image = self.horizontalD[self.animation // self.fps]
        elif self.last_move == 'bottom':
            self.image = self.bottomD[self.animation // self.fps]
        elif self.last_move == 'top':
            self.image = self.topD[self.animation // self.fps]
        elif self.last_move == 'left':
            self.image = pygame.transform.flip(self.horizontalD[self.animation // self.fps], True, False)

        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*self.transform_value), int(self.size[1]*self.transform_value)))
        self.screen.blit(self.image, self.rect)


