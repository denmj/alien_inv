
import sys
import pygame


def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Inv")

    bg_pic = pygame.image.load('C://Users/u325539/Desktop/ML/proj/Alien_inv/background/bgrnd.jpg')


    #loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # screen.fill((255, 255, 255))
        screen.blit(bg_pic, (0, 0))
        pygame.display.flip()


run_game()

