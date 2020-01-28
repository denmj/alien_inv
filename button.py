import pygame


class Button:
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
