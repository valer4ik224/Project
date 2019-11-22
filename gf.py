import pygame
import sys

def check_events(screen, settings, char):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, char, screen, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, char)

def update_screen(screen, settings, char):
    screen.fill(settings.bg_color)
    char.blitme()
    pygame.display.flip()

def check_keydown_events(event, char, screen, settings):
    if event.key == pygame.K_d:
        char.moving_right = True
    if event.key == pygame.K_a:
        char.moving_left = True
    if event.key == pygame.K_w:
        char.moving_up = True
    if event.key == pygame.K_s:
        char.moving_down = True
    if event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, char):
    if event.key == pygame.K_d:
        char.moving_right = False
    if event.key == pygame.K_a:
        char.moving_left = False
    if event.key == pygame.K_w:
        char.moving_up = False
    if event.key == pygame.K_s:
        char.moving_down = False