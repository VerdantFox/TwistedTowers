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

tower_list = []


for tower_location in tower_locations:  # See lists.py
    x_coord, y_coord = tower_locations[tower_locations.index(tower_location)]
    tower_list.append([
        towerClass.TowerButton(     # 0 = Button
            x_coord, y_coord, opt1_msg="basic", opt1_action="basic"),
        towerClass.BasicTower(      # 1 = Basic
            x_coord, y_coord, destroy=True),
        towerClass.IceTower(        # 2 = Ice
            x_coord, y_coord, destroy=True),
        towerClass.FireTower(       # 3 = Fire
            x_coord, y_coord, destroy=True),
        towerClass.PoisonTower(     # 4 = Poison
            x_coord, y_coord, destroy=True),
        towerClass.DarkTower(       # 5 = Dark
            x_coord, y_coord, destroy=True)])


def game_loop():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    helpers.pause_game()
            # print(event)

        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        for sub_list in tower_list:
            for tower in sub_list:
                if not tower.destroyed:
                    selected = tower.option_selected
                    tower_number = action_definitions.get(selected)
                    tower.draw()
                    if selected:
                        sub_list[tower_number].destroyed = False
                        tower.destroyed = True
                        tower.option_selected = None

        next(enemy1.move())
        pause_button.draw()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
