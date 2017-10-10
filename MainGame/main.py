import pygame
import generalClass
import towerClass
import enemies
import helpers
from colors import *
from lists import *
from gameParameters import backgroundImage, gameDisplay

# Initialize and set clock
pygame.init()
clock = pygame.time.Clock()

# Set static buttons
pause_button = generalClass.RectButton(
    20, 20, message="Pause", inactive_color=gray, active_color=white,
    action=helpers.pause_game)

# Define first enemy
enemy1 = enemies.Enemy()

# Set up towers
towers = []
for tower_location in tower_locations:  # See lists.py
    x_coord, y_coord = tower_locations[tower_locations.index(tower_location)]
    towers.append(towerClass.TowerButton(x_coord, y_coord, opt1_msg="basic"))

# basic1 = towerClass.BasicTower(100, 100)


def game_loop():

    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    helpers.pause_game()
            # print(event)

        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        for tower in towers:
            tower.draw()
        # basic1.draw()
        next(enemy1.move())
        pause_button.draw()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
