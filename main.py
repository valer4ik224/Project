import pygame
import game_functions as gf

from settings import Settings
from character import Character
from map import Soil
from map import Water
from map import Stone
from map import Chest
from map import Heart
from map import Door


from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("GAME")
    soils = Group()
    stones = Group()
    waters = Group()
    bullets = Group()
    chests = Group()
    hearts = Group()
    doors = Group()
    character = Character(screen, settings)

    map = [ ['H', 'H', 'H', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'D', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'W', 'W'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'W'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y'],
            ['X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'Y', 'X', 'Q', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'Y', 'Y', 'Y', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'Y', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'Y', 'X', 'X', 'X', 'X', 'X', 'X','X', 'X', 'X', 'X'],
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
            elif col == 'Q':
                soil = Soil(screen, settings)
                chest = Chest(screen, settings)
                soil.rect.x += x * soil.rect.width
                soil.rect.y += y * soil.rect.height
                chest.rect.x += x * chest.rect.width
                chest.rect.y += y * chest.rect.height
                soils.add(soil)
                chests.add(chest)
                x += 1
            elif col == 'H':
                soil = Soil(screen, settings)
                heart = Heart(screen, settings)
                soil.rect.x += x * soil.rect.width
                soil.rect.y += y * soil.rect.height
                heart.rect.x += x * heart.rect.width
                heart.rect.y += y * heart.rect.height
                soils.add(soil)
                chests.add(heart)
                x += 1
            elif col == 'D':
                soil = Soil(screen, settings)
                door = Door(screen, settings)
                soil.rect.x += x * soil.rect.width
                soil.rect.y += y * soil.rect.height
                door.rect.x += x * door.rect.width
                door.rect.y += y * door.rect.height
                door.image = pygame.transform.scale(door.image, (54, 64))
                soils.add(soil)
                doors.add(door)
                x += 1
            elif col == 'Y':
                stone_obj = Stone(screen , settings)
                stone_obj.rect.x += x * stone_obj.rect.width
                stone_obj.rect.y += y * stone_obj.rect.height
                stones.add(stone_obj)
                x += 1
            elif col == 'W':
                water = Water(screen , settings)
                water.rect.x += x * water.rect.width
                water.rect.y += y * water.rect.height
                waters.add(water)
                x += 1
        x = 0
        y += 1







    while True:

        gf.update_screen(screen, settings, soils, stones, waters, chests, hearts, doors, character, bullets)
        gf.check_events(settings, screen, character, bullets)
        character.update(character, stones)
        bullets.update()
        gf.update_bullets(bullets)

run_game()








