import pygame
import generalClass
import towerClass
import enemies
import helpers
from definitions import *
from lists import *
from gameParameters import backgroundImage, gameDisplay, display_height, clock


# Start game loop
def game_loop():
    # Set static buttons
    pause_button = generalClass.Button(
        (20, 50), message="Pause", color1=gray, color2=white,
        action=helpers.pause_game)

    # Set up game rules
    score_board = generalClass.GameScore((20, 20))
    funds = generalClass.Money((20, display_height - 90))
    castle = generalClass.Castle((20, display_height - 60))
    end_screen = generalClass.EndScreen()
    frames = 0

    # # Single enemy
    # enemies_list = [enemies.Enemy(speed=1)]

    # Set enemies
    enemies_list = [enemies.Enemy(speed=1), enemies.Enemy(speed=1),
                    enemies.Enemy(speed=1), enemies.Enemy(speed=1)]

    # # fast tester enemies
    # enemies_list = [enemies.Enemy(speed=10), enemies.Enemy(speed=10),
    #                 enemies.Enemy(speed=10), enemies.Enemy(speed=10),
    #                 enemies.Enemy(speed=10), enemies.Enemy(speed=10),
    #                 enemies.Enemy(speed=10), enemies.Enemy(speed=10),
    #                 enemies.Enemy(speed=10), enemies.Enemy(speed=10)]

    # Set towers and missiles
    tower_list = []
    missile_list = []
    for tower_location in tower_locations:  # See lists.py
        tower_list.append([
            towerClass.TowerButton(  # 0 = Button
                tower_location, opt1_msg="basic", opt1_action="basic"),
            towerClass.BasicTower(tower_location),
            towerClass.IceTower(tower_location),
            towerClass.FireTower(tower_location),
            towerClass.PoisonTower(tower_location),
            towerClass.DarkTower(tower_location)])
        missile_list.append([
            None,
            towerClass.BasicMissile(tower_location),
            towerClass.IceMissile(tower_location),
            towerClass.FireMissile(tower_location),
            towerClass.PoisonMissile(tower_location),
            towerClass.DarkMissile(tower_location)])

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

        # show background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        # Draw and move enemies
        # If enemies reach castle, damage castle
        for enemy in enemies_list:
            castle_damage = enemy.move()
            if enemy.fireball:
                for adjacent in enemies_list:
                    if adjacent != enemy:
                        if helpers.collision(enemy, adjacent):
                            if adjacent.fire_lockout == 0:
                                adjacent.fire = 3
                                adjacent.burned_counter = 3
                                adjacent.fire_lockout = 3 * seconds

            if castle_damage:
                if castle.hp > 0:
                    castle.adjust(-castle_damage)

        # Go through list of towers, drawing towers if not destroyed
        # Then drawing missiles to match appropriate tower
        for tower_location in tower_list:
            for current_tower in tower_location:
                if not current_tower.destroy:
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
                                print("Not enough funds!")
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
                                if specialty == "ice":
                                    enemy.ice = 30
                                if specialty == "poison":
                                    enemy.poison = 5
                                if specialty == "fire":
                                    enemy.fireball = True
                                    enemy.fire = 3
                                    enemy.burned_counter = 3
                                    enemy.fire_lockout = 3 * seconds
                                if specialty == "dark":
                                    enemy.dark = damage * 2
                                enemy.take_damage(damage)
                            kill = enemy.check_death()
                            if kill:
                                points, cash = kill
                                score_board.score += points
                                funds.adjust(cash)

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


game_loop()
pygame.quit()
quit()
