import pygame


class GameStats:
    def __init__(self, settings):

        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_lives_left = self.settings.ship_lives