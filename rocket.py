import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    def __init__(self, settings, screen, player_ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.rocket_width, settings.rocket_height)
        self.rect.centerx = player_ship.rect.centerx
        self.rect.top = player_ship.rect.top

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = settings.rocket_color
        self.speed_factor = settings.rocket_speed_factor

    # Overrides Scripts update
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_rocket(self):
        pygame.draw.rect(self.screen, self.color, self.rect)