import pygame


class Menu:
    def __init__(self, screen, text):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 400
        self.height = 600

        self.menu_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_menu(text)

    def prep_menu(self, text):
        self.text = self.font.render(text, True, self.text_color, self.menu_color)
        self.text_rect = self.text.get_rect(center=(self.height, self.width-250))
        # self.text_rect.midtop = self.rect.midtop

    def draw_menu(self):
        self.screen.fill(self.menu_color, self.rect)
        self.screen.blit(self.text, self.text_rect)
