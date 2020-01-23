import sys
import pygame
from rocket import Rocket


def check_keydown_events(event, settings, screen, player_ship, rockets):
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        player_ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_rocket(settings, screen, player_ship, rockets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_rocket(settings, screen, player_ship, rockets):
    if len(rockets) < settings.rocket_qnty:
        new_rocket = Rocket(settings, screen, player_ship)
        rockets.add(new_rocket)


def check_keyup_events(event, player_ship):
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = False
    if event.key == pygame.K_LEFT:
        player_ship.moving_left = False


def check_events(settings, screen, player_ship, rockets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, player_ship, rockets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player_ship)


def update_screen(screen, player_ship, rockets, alien):
    bg_pic = pygame.image.load('background/bgrnd-2.jpg')
    bg_pic_rect = bg_pic.get_rect()

    screen.blit(bg_pic, bg_pic_rect)

    for rocket in rockets.sprites():
        rocket.draw_rocket()
    alien.blitme()
    player_ship.blitme()
    pygame.display.flip()


def update_rockets(rockets):
    rockets.update()
    for rocket in rockets.copy():
        if rocket.rect.bottom <= 0:
            rockets.remove(rocket)
