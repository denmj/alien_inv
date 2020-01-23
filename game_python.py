from alien_inv.game_settings import Settings
from alien_inv.ship import Ship
from alien_inv.game_logic import *
import sys
import os
import pygame


def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    player_ship = Ship(screen)

    # loop
    while True:
        check_events(player_ship)
        player_ship.update_position()
        update_screen(screen, player_ship)



run_game()

