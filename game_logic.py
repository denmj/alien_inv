import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, player_ship):
    bg_pic = pygame.image.load('background/bgrnd-2.jpg')
    bg_pic_rect = bg_pic.get_rect()

    screen.blit(bg_pic, bg_pic_rect, )
    player_ship.blitme()
    pygame.display.flip()