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
    location = tower_locations[tower_locations.index(tower_location)]
    tower_list.append([
        towerClass.TowerButton(     # 0 = Button
            location, opt1_msg="basic", opt1_action="basic"),
        towerClass.BasicTower(location),
        towerClass.IceTower(location),
        towerClass.FireTower(location),
        towerClass.PoisonTower(location),
        towerClass.DarkTower(location)])

basic1 = towerClass.BasicTower((269, 477))


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
                    if pygame.sprite.collide_circle(tower, enemy1):
                        print("collision at tower {}"
                              .format(tower_list.index(sub_list)))
        basic1.draw()

        # next(enemy1.move())
        enemy1.move()
        pause_button.draw()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
