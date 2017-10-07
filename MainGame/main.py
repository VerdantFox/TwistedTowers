import pygame
import general_classes
import enemies
import mainLoop
from colors import *
from enemyPath import *


# Initialize and set clock
pygame.init()
clock = pygame.time.Clock()

# Set constants for game dimensions, background, title and icon
backgroundImage = general_classes.Background('TowerpathCastle1.PNG', [0, 0])
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tower Defense')
pygame.display.set_icon(pygame.image.load('TowerIcon32transparaent.png'))

# Define first enemy
enemy1 = enemies.Enemy(image_file='runner1.png',
                       location=(path_nodes[0][0], path_nodes[0][1]),
                       speed=3)

button1 = general_classes.Button("Continue", 150, 450, 100, 50, action=quit,
                                 inactive_color=red, active_color=green)


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
            # print(event)

        gameDisplay.fill(white)
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        next(enemy1.move())

        button1.draw()
        button1.set_text()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
