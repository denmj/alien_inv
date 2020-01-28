from alien_inv.game_settings import Settings
from alien_inv.ship import Ship
from alien_inv.alien import Alien
from alien_inv.game_stat import GameStats
from alien_inv.game_logic import *
import sys
import os

import pygame
from pygame.sprite import Group

FPS = 60


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(game_settings)
    player_ship = Ship(screen)
    rockets = Group()
    aliens = Group()

    create_alien_fleet(game_settings, screen, player_ship, aliens)

    # loop
    while True:
        clock.tick(60)
        check_events(game_settings, screen, player_ship, rockets)
        if game_settings.game_active:
            player_ship.update_position()
            update_rockets(game_settings, screen, player_ship, rockets, aliens)
            update_aliens(game_settings, stats, screen, player_ship, aliens, rockets)
        update_screen(screen, player_ship, rockets, aliens)


run_game()

