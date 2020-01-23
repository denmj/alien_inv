import pygame


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('background/player-spaceship-60x60.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom-30

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 7.5
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 7.5
