import pygame
import generalClass
import towerClass
import enemies
import helpers
from colors import *
from lists import *
from gameParameters import backgroundImage, gameDisplay, display_height

# Initialize and set clock
pygame.init()
clock = pygame.time.Clock()

# Set static buttons
pause_button = generalClass.RectButton(
    (20, 50), message="Pause", inactive_color=gray, active_color=white,
    action=helpers.pause_game)

score_board = generalClass.GameScore((20, 20))

enemies_list = [enemies.Enemy(speed=1), enemies.Enemy(speed=2, points=5),
                enemies.Enemy(speed=2), enemies.Enemy(speed=1)]

game_score = 0
funds = generalClass.Money((20, display_height - 60))

tower_list = []
missile_list = []


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

    missile_list.append([towerClass.BasicMissile(location)])


def game_loop():
    global game_score
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

        for enemy in enemies_list:
            enemy.move()

        for sub_list in tower_list:
            for tower in sub_list:
                if not tower.destroy:
                    selected = tower.option_selected
                    # See lists.py
                    tower_number = action_definitions.get(selected)
                    tower.draw()
                    if selected:
                        new_tower = sub_list[tower_number]
                        if selected == "sell":
                            new_tower.destroy = False
                            tower.destroy = True
                            tower.option_selected = None
                            funds.adjust(tower.sell)
                        else:
                            if new_tower.buy <= funds.cash:
                                new_tower.destroy = False
                                tower.destroy = True
                                tower.option_selected = None
                                funds.adjust(-new_tower.buy)
                            else:
                                tower.option_selected = None
                                print("Not enough funds!")
                    if sub_list.index(tower) != 0:
                        missile = missile_list[tower_list.index(
                            sub_list)][0]
                        for enemy in enemies_list:
                            damage = missile.fire(tower, enemy)
                            if damage:
                                dead = enemy.take_damage(damage)
                                if dead:
                                    points, cash = dead
                                    if points:
                                        score_board.score += points
                                    if cash:
                                        funds.adjust(cash)


        funds.draw()
        score_board.draw()
        pause_button.draw()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
