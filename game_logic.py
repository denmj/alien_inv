import sys
import pygame
from time import sleep
from alien_inv.rocket import Rocket
from alien_inv.alien import Alien


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_rows(settings, player_ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - player_ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien_ship = Alien(settings, screen)
    alien_width = alien_ship.rect.width
    alien_ship.x = alien_width + 2 * alien_width * alien_number
    alien_ship.rect.x = alien_ship.x
    alien_ship.rect.y = alien_ship.rect.height + 2 * alien_ship.rect.height * row_number
    aliens.add(alien_ship)


def create_alien_fleet(settings, screen, player_ship, aliens):
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_aliens_rows(settings, player_ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for numb_of_alien in range(number_aliens_x):
            create_alien(settings, screen, aliens, numb_of_alien, row_number)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def check_aliens_reach_bottom(settings, stats, screen, player_ship, aliens, rockets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, player_ship, aliens, rockets)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.drop_speed
    settings.direction *= -1


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


def ship_hit(settings, stats, screen, player_ship, aliens, rockets):
    if stats.ship_lives_left > 0:
        stats.ship_lives_left -= 1

        aliens.empty()
        rockets.empty()

        create_alien_fleet(settings, screen, player_ship, aliens)
        player_ship.center_ship()

        sleep(1)
    else:
        settings.game_active = False

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


def check_alien_rocket_collisions(settings, screen, player_ship, aliens, rockets):
    collisions = pygame.sprite.groupcollide(rockets, aliens, True, True)

    if len(aliens) == 0:
        create_alien_fleet(settings, screen, player_ship, aliens)


def check_player_ship_alien_collision(settings, stats, screen, player_ship, aliens, rockets):
    if pygame.sprite.spritecollideany(player_ship, aliens):
        ship_hit(settings, stats, screen, player_ship, aliens, rockets)


def update_screen(screen, player_ship, rockets, aliens):
    bg_pic = pygame.image.load('background/starfield.png')
    bg_pic_rect = bg_pic.get_rect()

    screen.blit(bg_pic, bg_pic_rect)

    for rocket in rockets.sprites():
        rocket.draw_rocket()
    aliens.draw(screen)
    player_ship.blitme()
    pygame.display.flip()


def update_rockets(settings, screen, player_ship, rockets, aliens):
    rockets.update()
    for rocket in rockets.copy():
        if rocket.rect.bottom <= 0:
            rockets.remove(rocket)

    check_alien_rocket_collisions(settings, screen, player_ship, aliens, rockets)


def update_aliens(settings, stats, screen, player_ship, aliens, rockets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_player_ship_alien_collision(settings, stats, screen, player_ship, aliens, rockets)
    check_aliens_reach_bottom(settings, stats, screen, player_ship, aliens, rockets)
