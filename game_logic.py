import sys
import pygame
from rocket import Rocket
from alien import Alien


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_rows(settings, player_ship_height, alien_height):
    available_space_y = settings.screen_height - 3 * alien_height - player_ship_height
    number_rows = available_space_y / (2 * alien_height)
    return number_rows


def create_alien(settnigs, screen, aliens, alien_number):
    alien_ship = Alien(settnigs, screen)
    alien_width = alien_ship.rect.width
    alien_ship.x = alien_width + 2 * alien_width * alien_number
    alien_ship.rect.x = alien_ship.x
    aliens.add(alien_ship)


def create_alien_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)

    for numb_of_alien in range(number_aliens_x):
        create_alien(settings, screen, aliens, numb_of_alien)


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


def update_screen(screen, player_ship, rockets, aliens):
    bg_pic = pygame.image.load('background/bgrnd-2.jpg')
    bg_pic_rect = bg_pic.get_rect()

    screen.blit(bg_pic, bg_pic_rect)

    for rocket in rockets.sprites():
        rocket.draw_rocket()
    aliens.draw(screen)
    player_ship.blitme()
    pygame.display.flip()


def update_rockets(rockets):
    rockets.update()
    for rocket in rockets.copy():
        if rocket.rect.bottom <= 0:
            rockets.remove(rocket)
