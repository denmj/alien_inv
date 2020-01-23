import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    def __init__(self, settings, screen, player_ship):
        super().__init__()
        self.screen = screen

