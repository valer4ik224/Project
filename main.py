import pygame
import gf
from settings import Settings

def run_game():
    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("game_name")

while True:
    gf.update_screen(screen, settings)
    gf.check_events(screen, settings)



run_game()