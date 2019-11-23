import pygame
import sys


def check_events(settings, screen, character, bullets):
    for event in pygame.event.get():
        #Check events
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            key_checkdown_events(event, character, screen, settings, bullets)

        if event.type == pygame.KEYUP:
            key_checkup_events(event, character)



def update_screen(screen, settings, soils, character, bullets):
    screen.fill(settings.bg_color)
    for i in soils:
        i.blitme()
    character.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()


def key_checkdown_events(event, character, screen, settings, bullets):

    if event.key == pygame.K_d:
        character.moving_right = True
    if event.key == pygame.K_a:
        character.moving_left = True
    if event.key == pygame.K_w:
        character.moving_up = True
    if event.key == pygame.K_s:
        character.moving_down = True
    if event.key == pygame.K_SPACE:
        fireBullets(bullets, screen, settings, ship)
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def key_checkup_events(event, character):

        if event.key == pygame.K_d:
            character.moving_right = False
        if event.key == pygame.K_a:
            character.moving_left = False
        if event.key == pygame.K_w:
            character.moving_up = False
        if event.key == pygame.K_s:
            character.moving_down = False

def update_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        bullets.update()


def fireBullets(bullets, screen, settings, ship):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(screen, settings, ship)
        bullets.add(new_bullet)



