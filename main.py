import pygame
import gf
from settings import Settings
from char import Char

def run_game():
    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.FULLSCREEN)
    char = Char(screen, settings)
    pygame.display.set_caption("game_name")

while True:
    gf.update_screen(screen, settings, char)
    gf.check_events(screen, settings, char)
    char.update()



run_game()