import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()

        self.settings = settings
        self.screen = screen

        self.alien_igm = pygame.image.load('background/alien-transp.png')
        self.rect = self.alien_igm.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.alien_igm, self.rect)
