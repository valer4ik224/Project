import pygame
import sys

def check_events(screen, setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,)

def update_screen(screen, settings):
    screen.fill(settings.bg_color)
    pygame.display.flip()
