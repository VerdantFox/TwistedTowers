import pygame
import random
from colors import *

pygame.init()

display_width = 850
display_height = 650

gameDisplay = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('TowerPathFinal1.png')
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('TowerIcon32transparaent.png')
pygame.display.set_icon(gameIcon)


def game_loop():

    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        gameDisplay.fill(white)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
