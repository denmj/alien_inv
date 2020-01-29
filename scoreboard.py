import pygame


class Scoreboard:
    def __init__(self, settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settnigs = settings
        self.stats = stats

        self.text_color = (212,175,55)
        self.font = pygame.font.SysFont(None, 38)

        self.prep_board()

    def prep_board(self):
        score = "Aliens killed: " + str(self.stats.score)

        self.board_image = self.font.render(score, True, self.text_color)

        self.board_image_rect = self.board_image.get_rect()
        self.board_image_rect.right = self.screen_rect.right - 20
        self.board_image_rect.top = 20

    def draw_board(self):
        self.screen.blit(self.board_image, self.board_image_rect)