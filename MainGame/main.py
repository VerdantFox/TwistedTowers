import pygame
import general_classes
import enemies
from colors import *
from lists import *


# Initialize and set clock
pygame.init()
clock = pygame.time.Clock()

# Set constants for game dimensions, background, title and icon
backgroundImage = general_classes.Background('TowerpathCastle3.png')
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tower Defense')
pygame.display.set_icon(pygame.image.load('TowerpathCastle3.png'))

# Define first enemy
enemy1 = enemies.Enemy(image_file='runner1.png',
                       location=(path_nodes[0][0], path_nodes[0][1]),
                       speed=3)

# Set up towers
towers = []
for tower_location in tower_locations:
    x_coord, y_coord = tower_locations[tower_locations.index(tower_location)]
    towers.append(general_classes.TowerButton(
            x_coord, y_coord, action=quit, message="blah"))


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

        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        for tower in towers:
            tower.draw()
        next(enemy1.move())

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
