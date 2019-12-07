import pygame
import game_functions as gf

from settings import Settings
from character import Character
from map import Soil
from pygame.sprite import Group
from enemie import Enemie


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("GAME")
    soils = Group()
    bullets = Group()
    enemies = Group()
    character = Character(screen, settings)
    gf.create_fleet(settings, screen, enemies)
    map = [ ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ]

    x = 0
    y = 0
    for row in map:
        for col in row:
            if col == 'X':
                soil = Soil(screen, settings)
                soil.rect.x += x * soil.rect.width
                soil.rect.y += y * soil.rect.height
                soils.add(soil)
                x += 1
        x = 0
        y += 1







    while True:

        gf.update_screen(screen, settings, soils, character, bullets, enemies)
        gf.check_events(settings, screen, character, bullets, enemies)
        character.update()
        bullets.update()

run_game()








