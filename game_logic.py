import sys
import pygame


def check_keydown_events(event, player_ship):
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = True
    if event.key == pygame.K_LEFT:
        player_ship.moving_left = True


def check_keyup_events(event, player_ship):
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = False
    if event.key == pygame.K_LEFT:
        player_ship.moving_left = False


def check_events(player_ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player_ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player_ship)


def update_screen(screen, player_ship):
    bg_pic = pygame.image.load('background/bgrnd-2.jpg')
    bg_pic_rect = bg_pic.get_rect()

    screen.blit(bg_pic, bg_pic_rect, )
    player_ship.blitme()
    pygame.display.flip()