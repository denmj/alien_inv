from game_settings import Settings
from ship import Ship
from alien import Alien
from game_logic import *
import sys
import os
import pygame
from pygame.sprite import Group


def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    player_ship = Ship(screen)
    rockets = Group()
    aliens = Group()

    create_alien_fleet(game_settings, screen, aliens)

    # loop
    while True:
        check_events(game_settings, screen, player_ship, rockets)
        player_ship.update_position()
        update_rockets(rockets)
        update_screen(screen, player_ship, rockets, aliens)


run_game()

