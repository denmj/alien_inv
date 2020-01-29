from game_settings import Settings
from button import Button
from menu import Menu
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from game_stat import GameStats
from game_logic import *
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
    game_menu = Menu(screen, "Game Menu")
    play_button = Button(game_settings, screen, "Play", 500, 250)
    option_button = Button(game_settings, screen, "Options", 500, 350)
    reset_button = Button(game_settings, screen, "Reset game", 500, 450)
    exit_button = Button(game_settings, screen, "Exit", 500, 550)
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(game_settings)
    score_board = Scoreboard(game_settings, screen, stats)
    player_ship = Ship(screen)
    rockets = Group()
    aliens = Group()

    create_alien_fleet(game_settings, screen, player_ship, aliens)

    # game loop
    while True:
        clock.tick(60)
        check_events(score_board, stats, game_settings, screen, player_ship, aliens, rockets, play_button, reset_button)
        if game_settings.game_active:
            player_ship.update_position()
            update_rockets(game_settings, stats, screen, player_ship, rockets, aliens, score_board)
            update_aliens(game_settings, stats, screen, player_ship, aliens, rockets)
        update_screen(game_settings, screen, player_ship, rockets, aliens, play_button,
                      option_button, exit_button, reset_button, game_menu, score_board)


run_game()

