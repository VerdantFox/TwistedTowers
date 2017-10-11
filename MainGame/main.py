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
empty_tower = []
basic_tower = []
ice_tower = []
fire_tower = []
poison_tower = []
dark_tower = []


for tower_location in tower_locations:  # See lists.py
    x_coord, y_coord = tower_locations[tower_locations.index(tower_location)]
    empty_tower.append(towerClass.TowerButton(
        x_coord, y_coord, opt1_msg="basic", opt1_action="basic"))
    basic_tower.append(towerClass.BasicTower(
        x_coord, y_coord, destroy=True))
    ice_tower.append(towerClass.IceTower(
        x_coord, y_coord, destroy=True))
    fire_tower.append(towerClass.FireTower(
        x_coord, y_coord, destroy=True))
    poison_tower.append(towerClass.PoisonTower(
        x_coord, y_coord, destroy=True))
    dark_tower.append(towerClass.DarkTower(
        x_coord, y_coord, destroy=True))

print(dark_tower)


basic1 = towerClass.BasicTower(100, 100)


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

        for tower in empty_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "basic":
                    basic_tower[empty_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        for tower in basic_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "sell":
                    print(selected)
                    empty_tower[basic_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None
                if selected == "ice":
                    print(selected)
                    ice_tower[basic_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None
                if selected == "fire":
                    print(selected)
                    fire_tower[basic_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None
                if selected == "poison":
                    print(selected)
                    poison_tower[basic_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None
                if selected == "dark":
                    print(selected)
                    dark_tower[basic_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        for tower in ice_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "sell":
                    empty_tower[ice_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        for tower in fire_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "sell":
                    empty_tower[fire_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        for tower in poison_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "sell":
                    empty_tower[poison_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        for tower in dark_tower:
            if not tower.destroyed:
                selected = tower.option_selected
                tower.draw()
                if selected == "sell":
                    empty_tower[dark_tower.index(tower)].destroyed = False
                    tower.destroyed = True
                    tower.option_selected = None

        basic1.draw()
        next(enemy1.move())
        pause_button.draw()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
