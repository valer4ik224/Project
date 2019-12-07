import pygame
import sys
from bullet import Bullet
from character import Character
import character
from settings import Settings
from enemie import Enemie

def check_events(settings, screen, character, bullets, enemies):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            key_checkdown_events(event, character, screen, settings, bullets, enemies)

        if event.type == pygame.KEYUP:
            key_checkup_events(event, character)



def update_screen(screen, settings, soils, character, bullets, enemies):
    pygame.sprite.groupcollide(bullets, enemies, True, True)
    screen.fill(settings.bg_color)
    for i in soils:
        i.blitme()
    enemies.draw(screen)
    update_enemies(enemies,settings)
    character.blitme()
    for bullet in bullets.sprites():
        if bullet.rect.right > settings.screen_width:
            bullets.remove(bullet)
        if bullet.rect.top > settings.screen_height:
            bullets.remove(bullet)
        if bullet.rect.left < 0:
            bullets.remove(bullet)
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

        bullet.draw_bullet()

    pygame.display.flip()





def key_checkdown_events(event, character, screen, settings, bullets, enemies):

    if event.key == pygame.K_d:
        character.moving_right = True
    if event.key == pygame.K_a:
        character.moving_left = True
    if event.key == pygame.K_w:
        character.moving_up = True
    if event.key == pygame.K_s:
        character.moving_down = True
    if event.key == pygame.K_e:
        fireBullets(bullets, screen, settings, character, enemies)
    if event.key == pygame.K_SPACE:
       character.attack = True
       pygame.sprite.spritecollide(character, enemies, True)
    if event.key == pygame.K_ESCAPE:
        sys.exit()


def key_checkup_events(event, character):
        character.animation = 0
        if event.key == pygame.K_d:
            character.moving_right = False
        if event.key == pygame.K_a:
            character.moving_left = False
        if event.key == pygame.K_w:
            character.moving_up = False
        if event.key == pygame.K_s:
            character.moving_down = False




def fireBullets(bullets, screen, settings, character, enemies):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(screen, settings, character)
        if character.last_move == 'right':
            new_bullet.move_x = settings.bullet_speed
        elif character.last_move == 'left':
            new_bullet.move_x = -settings.bullet_speed
        if character.last_move == 'top':
            new_bullet.move_y = -settings.bullet_speed
        elif character.last_move == 'bottom':
            new_bullet.move_y = settings.bullet_speed

        bullets.add(new_bullet)


def create_fleet(settings, screen, enemies):
    enemie = Enemie(screen, settings)

    for row_num in range(1):
        for enemie_num in range(3):
            create_enemie(screen, settings, enemies, enemie_num, row_num)



def create_enemie(screen, settings, enemies, enemie_num, row_num):
    enemie = Enemie(screen, settings)
    enemie.rect.x = enemie.rect.width + enemie.rect.width * 2 * enemie_num
    enemie.rect.y = enemie.rect.height + enemie.rect.height * 2 * row_num
    enemies.add(enemie)

def update_enemies(enemies,settings):
    enemies.update()
    check_fleet_edges(enemies, settings)
def check_fleet_edges(enemies, settings):
    for enemie in enemies:
        if enemie.check_edges() == True:

            change_fleet_direction(enemies, settings)
            break

def change_fleet_direction(enemies, settings):
    for enemie in enemies:
        settings.fleet_direction *= -1






