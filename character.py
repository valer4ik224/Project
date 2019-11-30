import pygame


class Character():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/char1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
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
        self.animation = 0
        self.last_move = 'zero'
        self.fps = 5


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def load_image(self, img):
        return pygame.image.load(img).convert_alpha()




    def update(self):
        if self.animation > len(self.horizontalD) * self.fps:
            self.animation = 0
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


    def blitme(self):

        if len(self.horizontalD) <= self.animation // self.fps:
            self.animation = 0
        if len(self.topD) <= self.animation // self.fps:
            self.animation = 0
        if len(self.bottomD) <= self.animation // self.fps:
            self.animation = 0
        if self.last_move == 'right':
            self.image = self.horizontalD[self.animation // self.fps]
        if self.last_move == 'bottom':
            self.image = self.bottomD[self.animation // self.fps]
        if self.last_move == 'top':
            self.image = self.topD[self.animation // self.fps]
        if self.last_move == 'left':
            self.image = pygame.transform.flip(self.horizontalD[self.animation // self.fps], True, False)



        self.screen.blit(self.image, self.rect)


