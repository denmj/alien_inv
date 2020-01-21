from game_settings import Settings
from ship import Ship
import sys
import pygame


def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    player_ship = Ship(screen)

    bg_pic = pygame.image.load('C://Users/u325539/Desktop/ML/proj/Alien_inv/background/bgrnd-2.jpg')
    bg_pic_rect = bg_pic.get_rect()

    #loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # screen.fill((50, 50, 50))

        screen.blit(bg_pic, bg_pic_rect,)
        player_ship.blitme()
        pygame.display.flip()


run_game()

