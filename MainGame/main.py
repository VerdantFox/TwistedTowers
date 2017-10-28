import pygame
import generalClass
import towerClass
import enemies
import helpers
import random
from definitions import *
from lists import *

from gameParameters import backgroundImage, gameDisplay, display_height, clock


# Start game loop
def game_loop(start_cash=1000, enemy_spawn_rate=5*seconds):
    # Set static buttons
    pause_button = generalClass.Button(
        (20, 50), message="Pause", color1=gray, color2=white,
        action=helpers.pause_game)

    # Set up game rules
    score_board = generalClass.GameScore((20, 20))
    funds = generalClass.Money((20, display_height - 90), start_cash=start_cash)
    castle = generalClass.Castle((20, display_height - 60))
    end_screen = generalClass.EndScreen()
    frames = 0

    # Blank list
    enemies_list = []

    # # Single lizard
    # enemies_list = [enemies.Lizard(), enemies.Lizard(), enemies.Lizard()]

    # # Single orc
    # enemies_list = [enemies.Orc()]

    # # Single spider
    # enemies_list = [enemies.Spider(), enemies.Spider(), enemies.Spider(),
    #                 enemies.Spider(), enemies.Spider()]

    # # single turtle
    # enemies_list = [enemies.Turtle()]

    # # Single wolf
    # enemies_list = [enemies.Wolf()]

    # # Single Dragon
    # enemies_list = [enemies.Dragon()]

    # # all enemies
    # enemies_list = [enemies.Wolf(), enemies.Spider(), enemies.Orc(),
    #                 enemies.Turtle(), enemies.Lizard(), enemies.Dragon()]

    # Set towers and missiles
    bot_tower_list = []
    bot_missile_list = []
    top_tower_list = []
    top_missile_list = []

    set_towers(bot_tower_locations, bot_tower_list, bot_missile_list)
    set_towers(top_tower_locations, top_tower_list, top_missile_list)

    # Actual game loop
    while True:
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    helpers.pause_game()
            # print(event)

        # add new enemies
        add_enemies(frames, enemies_list, enemy_spawn_rate)

        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        # Draw top towers
        draw_towers(top_tower_list, top_missile_list, funds,
                    score_board, enemies_list)
        # Draw enemies
        draw_enemies(enemies_list, castle)
        # Draw bot towers
        draw_towers(bot_tower_list, bot_missile_list, funds,
                    score_board, enemies_list)

        funds.draw()
        castle.draw()
        score_board.draw()
        pause_button.draw()
        pygame.display.update()
        clock.tick(60)
        if castle.game_over:
            end_screen.score = score_board.score
            end_screen.time_elapsed = frames
            end = end_screen.draw()
            if end == "play":
                game_loop()
        if frames % (1 * seconds) == 0:
            funds.adjust(1)


def set_towers(tower_locations, tower_list, missile_list):
    for tower_location in tower_locations:  # See lists.py
        tower_list.append([
            towerClass.TowerButton(  # 0 = Button
                tower_location, ),
            towerClass.BasicTower(tower_location),
            towerClass.IceTower1(tower_location),
            towerClass.FireTower1(tower_location),
            towerClass.PoisonTower1(tower_location),
            towerClass.DarkTower1(tower_location),
            towerClass.IceTower2(tower_location),
            towerClass.FireTower2(tower_location),
            towerClass.PoisonTower2(tower_location),
            towerClass.DarkTower2(tower_location)])
        missile_list.append([
            None,
            towerClass.BasicMissile(tower_location),
            towerClass.IceMissile1(tower_location),
            towerClass.FireMissile1(tower_location),
            towerClass.PoisonMissile1(tower_location),
            towerClass.DarkMissile1(tower_location),
            towerClass.IceMissile2(tower_location),
            towerClass.FireMissile2(tower_location),
            towerClass.PoisonMissile2(tower_location),
            towerClass.DarkMissile2(tower_location)])


def add_enemies(frames, enemies_list, enemy_spawn_rate):
    picker = 0
    if frames % enemy_spawn_rate == 0:
        # Setting the picker
        if frames <= 0.33 * minutes:
            picker = 0
        if 0.33 * minutes < frames <= .66 * minutes:
            picker = 1
        if 0.66 * minutes < frames <= 1 * minutes:
            picker = random.randint(2, 4)
        if 1 * minutes < frames <= 2 * minutes:
            picker = random.randint(3, 7)
        if 2 * minutes < frames <= 2.8 * minutes:
            picker = random.randint(8, 12)
        if 2.8 * minutes < frames <= 3.5 * minutes:
            picker = -1
        if frames == 3 * minutes:
            picker = 13
        if 3.5 * minutes < frames <= 5 * minutes:
            picker = random.randint(14, 18)
        if frames == 4 * minutes:
            picker = 13
        if 5 * minutes < frames <= 7 * minutes:
            picker = random.randint(13, 19)
        if frames > 7 * minutes:
            picker = random.randint(14, 20)
        if frames == 7 * minutes:
            picker = 20

        # The picks
        if picker == -1:
            pass
        if picker == 0:
            enemies_list.append(enemies.Spider())
        elif picker == 1:
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider()])
        elif picker == 2:
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider(), enemies.Spider()])
        elif picker == 3:
            enemies_list.append(enemies.Lizard())
        elif picker == 4:
            enemies_list.append(enemies.Wolf())
        elif picker == 5:
            enemies_list.append(enemies.Orc())
        elif picker == 6:
            enemies_list.append(enemies.Turtle())
        elif picker == 7:
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider()])
        elif picker == 8:
            enemies_list.extend([enemies.Lizard(), enemies.Lizard()])
        elif picker == 9:
            enemies_list.extend([enemies.Wolf(), enemies.Wolf()])
        elif picker == 10:
            enemies_list.extend([enemies.Orc(), enemies.Orc()])
        elif picker == 11:
            enemies_list.extend([enemies.Turtle(), enemies.Turtle()])
        elif picker == 12:
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider()])
        elif picker == 13:
            enemies_list.append(enemies.Dragon())
        elif picker == 14:
            enemies_list.extend([enemies.Lizard(), enemies.Lizard(),
                                 enemies.Lizard()])
        elif picker == 15:
            enemies_list.extend([enemies.Wolf(), enemies.Wolf(),
                                 enemies.Wolf()])
        elif picker == 16:
            enemies_list.extend([enemies.Orc(), enemies.Orc(), enemies.Orc()])
        elif picker == 17:
            enemies_list.extend([enemies.Turtle(), enemies.Turtle(),
                                 enemies.Turtle()])
        elif picker == 18:
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider()])
        elif picker == 19:
            enemies_list.extend(
                [enemies.Lizard(), enemies.Wolf(), enemies.Orc,
                 enemies.Turtle, enemies.Spider(), enemies.Spider(),
                 enemies.Spider()])
        elif picker == 20:
            enemies_list.extend([enemies.Dragon(), enemies.Dragon()])


def draw_towers(tower_list, missile_list, funds, score_board, enemies_list):
    # Go through list of towers, drawing towers if not destroyed
    # Then drawing missiles to match appropriate tower
    for tower_location in tower_list:
        for current_tower in tower_location:
            if not current_tower.destroy:
                if current_tower.tier == 0:
                    if funds.cash < 100:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                if current_tower.tier == 1:
                    if funds.cash < 125:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                if current_tower.tier == 2:
                    if funds.cash < 150:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                selected = current_tower.option_selected
                new_tower_index = actions.get(selected)  # See lists.py
                current_tower_index = tower_location.index(current_tower)
                if selected:
                    new_tower = tower_location[new_tower_index]
                    if selected == "sell":
                        new_tower.destroy = False
                        current_tower.destroy = True
                        current_tower.option_selected = None
                        funds.adjust(current_tower.sell)
                    else:
                        if new_tower.buy <= funds.cash:
                            new_tower.destroy = False
                            current_tower.destroy = True
                            current_tower.option_selected = None
                            funds.adjust(-new_tower.buy)
                        else:
                            current_tower.option_selected = None
                current_tower.draw()

                if current_tower_index != 0:
                    tower_position = tower_list.index(tower_location)
                    missile = \
                        missile_list[tower_position][current_tower_index]
                    for enemy in enemies_list:
                        hit = missile.lock_enemy(
                            current_tower, enemy)
                        if hit:
                            damage, specialty = hit
                            enemy.hit(damage, specialty)
                        try:    # Crashed once here 7 mins in ("no self given")
                            kill = enemy.check_death()
                            if kill:
                                points, cash = kill
                                score_board.adjust(points)
                                funds.adjust(cash)
                        except TypeError:
                            print("kill error")
                    missile.adjust_counters()


def draw_enemies(enemies_list, castle):
    # Draw and move enemies
    # If enemies reach castle, damage castle
    for enemy in enemies_list:
        if enemy.lives == 0:
            enemies_list.pop(enemies_list.index(enemy))
        castle_damage = enemy.move()

        # Fire stuff
        if enemy.fireball2:
            for adjacent in enemies_list:
                if adjacent != enemy:
                    if helpers.collision(enemy, adjacent):
                        adjacent.fire2 = enemy.fire2
                        adjacent.burned_counter = 3
        if enemy.fireball1 and not enemy.fireball2:
            for adjacent in enemies_list:
                if adjacent != enemy:
                    if helpers.collision(enemy, adjacent):
                        adjacent.fire1 = enemy.fire1
                        adjacent.burned_counter = 3

        if castle_damage:
            if castle.hp > 0:
                castle.adjust(-castle_damage)


if __name__ == "__main__":
    game_loop()
    pygame.quit()
    quit()
