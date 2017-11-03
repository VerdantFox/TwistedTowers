import random

import pygame

import enemies
import generalClass
import helpers
import towerClass
from definitions import *
from gameParameters import backgroundImage, gameDisplay, display_height, clock
from gameText import *
from lists import *
from sounds import build_tower_sound, sell_tower_sound, castle_hit


def load_intro_music():
    pygame.mixer.music.load('music/Anamalie.mp3')
    pygame.mixer.music.play(-1)
    intro_loop()


def intro_loop():
    play_button = generalClass.Button(
        (450, display_height - 250),
        message="Play", action=game_loop, font_size=40, width=300, height=60)
    quit_button = generalClass.Button(
        (450, display_height - 180),
        message="Quit", action=quit, font_size=40, width=300, height=60,
        color1=red, color2=bright_red)
    tower_info_button = generalClass.Button(
        (100, display_height - 320),
        message="Tower Types", action=tower_info_loop, font_size=40,
        width=300, height=60, color1=teal, color2=bright_teal)
    enemy_info_button = generalClass.Button(
        (100, display_height - 250),
        message="Enemy Types", action=enemy_info_loop, font_size=40,
        width=300, height=60, color1=yellow, color2=bright_yellow)
    settings_button = generalClass.Button(
        (100, display_height - 180),
        message="Settings", action=settings_loop, font_size=40,
        width=300, height=60, color1=orange, color2=bright_orange)

    font = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
    title_font = pygame.font.SysFont('Comic Sans MS', 72, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        # Draw title and intro text
        helpers.blit_text(gameDisplay, title, (100, 25),
                          title_font, margin=50)
        helpers.blit_text(gameDisplay, intro_text, (100, 150), font, margin=100)
        # Draw buttons
        play_button.draw()
        quit_button.draw()
        enemy_info_button.draw()
        tower_info_button.draw()
        settings_button.draw()
        # Update game display
        pygame.display.update()
        clock.tick(60)


def tower_info_loop():
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    previous_button = generalClass.Button(
        (50, display_height - 100), message="Previous", action="backward",
        font_size=40, width=200, height=60, color1=red, color2=bright_red)
    next_button = generalClass.Button(
        (600, display_height - 100), message="Next", action="forward",
        font_size=40, width=200, height=60, color1=green, color2=bright_green)
    # Texts
    font = pygame.font.SysFont('Comic Sans MS', 18, bold=True)

    basic = towerClass.BasicTower((160, 400), destroy=False)
    ice1 = towerClass.IceTower1((155, 250), destroy=False)
    ice2 = towerClass.IceTower2((155, 530), destroy=False)
    fire1 = towerClass.FireTower1((155, 250), destroy=False)
    fire2 = towerClass.FireTower2((155, 530), destroy=False)
    poison1 = towerClass.PoisonTower1((155, 250), destroy=False)
    poison2 = towerClass.PoisonTower2((155, 530), destroy=False)
    dark1 = towerClass.DarkTower1((155, 250), destroy=False)
    dark2 = towerClass.DarkTower2((155, 530), destroy=False)

    info_index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        pygame.draw.rect(gameDisplay, white,
                         (100, 125, 650, 525))
        # Draw buttons
        return_button.draw()
        next_tower = next_button.draw()
        previous_tower = previous_button.draw()
        if next_tower:
            info_index += 1
        if previous_tower:
            info_index -= 1
        if info_index > 4:
            info_index = 0
        if info_index < 0:
            info_index = 4
        # Draw Tower and info
        if info_index == 0:
            basic.draw()
            helpers.blit_text(gameDisplay, basic_tower_text, (225, 300),
                              font, margin=125)
        if info_index == 1:
            ice1.draw()
            ice2.draw()
            helpers.blit_text(gameDisplay, ice1_text, (225, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, ice2_text, (225, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 2:
            fire1.draw()
            fire2.draw()
            helpers.blit_text(gameDisplay, fire1_text, (225, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, fire2_text, (225, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 3:
            poison1.draw()
            poison2.draw()
            helpers.blit_text(gameDisplay, poison1_text, (225, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, poison2_text, (225, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 4:
            dark1.draw()
            dark2.draw()
            helpers.blit_text(gameDisplay, dark1_text, (225, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, dark2_text, (225, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        # Update game display
        pygame.display.update()
        clock.tick(60)


def enemy_info_loop():
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    previous_button = generalClass.Button(
        (50, display_height - 100), message="Previous", action="backward",
        font_size=40, width=200, height=60, color1=red, color2=bright_red)
    next_button = generalClass.Button(
        (600, display_height - 100), message="Next", action="forward",
        font_size=40, width=200, height=60, color1=green, color2=bright_green)
    # Texts
    font = pygame.font.SysFont('Comic Sans MS', 18, bold=True)

    spider = enemies.Spider((180, 250), (190, 250), True, False)
    lizard = enemies.Lizard((180, 530), (190, 530), True, False)
    wolf = enemies.Wolf((180, 250), (190, 250), True, False)
    turtle = enemies.Turtle((180, 530), (190, 530), True, False)
    orc = enemies.Orc((180, 250), (190, 250), True, False)
    dragon = enemies.Dragon((180, 530), (190, 530), True, False)

    info_index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        pygame.draw.rect(gameDisplay, white,
                         (100, 125, 650, 525))
        # Draw buttons
        return_button.draw()
        next_enemy = next_button.draw()
        previous_enemy = previous_button.draw()
        if next_enemy:
            info_index += 1
        if previous_enemy:
            info_index -= 1
        if info_index > 2:
            info_index = 0
        if info_index < 0:
            info_index = 2
        # Draw Tower and info
        if info_index == 0:
            spider.draw()
            lizard.draw()
            helpers.blit_text(gameDisplay, spider_text, (275, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, lizard_text, (275, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 1:
            wolf.draw()
            turtle.draw()
            helpers.blit_text(gameDisplay, wolf_text, (275, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, turtle_text, (275, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 2:
            orc.draw()
            dragon.draw()
            helpers.blit_text(gameDisplay, orc_text, (275, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, dragon_text, (275, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        # Update game display
        pygame.display.update()
        clock.tick(60)


def settings_loop():
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    easy_button = generalClass.Button(
        (50, 200), message="Easy", action=easy_settings, font_size=40,
        width=200, height=60, color1=green, color2=bright_green, permanent=True)
    medium_button = generalClass.Button(
        (50, 285), message="Medium", action=medium_settings, font_size=40,
        width=200, height=60, color1=yellow, color2=bright_yellow,
        permanent=True)
    hard_button = generalClass.Button(
        (50, 370), message="Hard", action=hard_settings, font_size=40,
        width=200, height=60, color1=red, color2=bright_red, permanent=True)
    font = pygame.font.SysFont('Comic Sans MS', 24, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        # Draw setting descriptions
        helpers.blit_text(gameDisplay, easy_text, (275, 190),
                          font, margin=-50)
        helpers.blit_text(gameDisplay, medium_text, (275, 275),
                          font, margin=50)
        helpers.blit_text(gameDisplay, hard_text, (275, 360),
                          font, margin=50)
        # Draw buttons
        return_button.draw()
        easy_button.draw(medium_button, hard_button)
        medium_button.draw(easy_button, hard_button)
        hard_button.draw(easy_button, medium_button)
        # Update game display
        pygame.display.update()
        clock.tick(60)


def easy_settings():
    settings.spawn_rate = 9 * seconds
    settings.starting_gold = 1600
    settings.gold_generation = 0.5 * seconds
    settings.difficulty = 2


def medium_settings():
    settings.spawn_rate = 6 * seconds
    settings.starting_gold = 1200
    settings.gold_generation = 1 * seconds
    settings.difficulty = 1


def hard_settings():
    settings.spawn_rate = 3 * seconds
    settings.starting_gold = 800
    settings.gold_generation = 2 * seconds
    settings.difficulty = 0.5


pause = False


def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()


def pause_game():

    pygame.mixer.music.pause()
    resume_button = generalClass.Button(
        (20, 80), message="Resume", width=120, color1=green,
        color2=bright_green, action=unpause)

    reset_button = generalClass.Button(
        (20, 110), message="Reset", width=120, color1=red,
        color2=bright_red, action=game_loop)

    main_button = generalClass.Button(
        (20, 140), message="Main Menu", width=120, color1=yellow,
        color2=bright_yellow, action=load_intro_music)

    global pause
    pause = True
    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    unpause()
        resume_button.draw()
        reset_button.draw()
        main_button.draw()
        pygame.display.update()


# Start game loop
def game_loop():
    # Start main game music
    pygame.mixer.music.fadeout(100)
    pygame.mixer.music.load('music/main_music_mesh2.wav')
    pygame.mixer.music.play(0)

    # Set static buttons
    pause_button = generalClass.Button(
        (20, 50), message="Pause", width=120,  color1=gray, color2=white,
        action=pause_game)

    # Set game settings
    start_cash = settings.starting_gold
    enemy_spawn_rate = settings.spawn_rate
    passive_money_rate = settings.gold_generation
    difficulty = settings.difficulty

    # Set up game rules
    score_board = generalClass.GameScore((140, 20))
    game_clock = generalClass.GameClock((20, 20))
    funds = generalClass.Money((20, display_height - 90), start_cash=start_cash)
    castle = generalClass.Castle((20, display_height - 60))
    end_screen = generalClass.EndScreen()

    # Set blank enemies list
    enemies_list = []

    # Set towers' and missiles' lists
    bot_tower_list = []
    bot_missile_list = []
    top_tower_list = []
    top_missile_list = []

    # Call function to set up towers and missiles
    set_towers(bot_tower_locations, bot_tower_list, bot_missile_list)
    set_towers(top_tower_locations, top_tower_list, top_missile_list)

    # Set mage
    mage = enemies.Mage()

    # Actual game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game()

        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        # Periodically add money
        if game_clock.frames % passive_money_rate == 0:
            funds.adjust(1)

        # add new enemies
        if not mage.stop_spawn:
            add_enemies(game_clock.frames, enemies_list, enemy_spawn_rate,
                        difficulty)

        # Draw top towers
        draw_towers(top_tower_list, top_missile_list, funds,
                    score_board, enemies_list)

        # Draw enemies
        draw_enemies(enemies_list, castle)

        # Draw bottom towers
        draw_towers(bot_tower_list, bot_missile_list, funds,
                    score_board, enemies_list)

        # Draw in mage
        draw_mage(mage, game_clock, score_board, funds, enemies_list)

        # Draw game info panels
        tower_costs_display()
        funds.draw()
        castle.draw()
        score_board.draw()
        game_clock.draw()
        pause_button.draw()

        # Update game
        pygame.display.update()
        clock.tick(60)

        # Set win/loss conditions
        if mage.win:
            end_screen.score = score_board.score
            end_screen.time_elapsed = game_clock.frames
            end = end_screen.draw("win")
            if end == "play":
                game_loop()
            if end == "main":
                load_intro_music()
        if castle.game_over:
            end_screen.score = score_board.score
            end_screen.time_elapsed = game_clock.frames
            end = end_screen.draw("lose")
            if end == "play":
                game_loop()
            if end == "main":
                load_intro_music()


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


def add_enemies(frames, enemies_list, enemy_spawn_rate, difficulty):
    picker = 0
    if frames % enemy_spawn_rate == 0:
        min_rate = minutes * difficulty
        # Setting the picker
        if frames <= 0.33 * min_rate:
            picker = 0
        if 0.33 * min_rate < frames <= .66 * min_rate:
            picker = 1
        if 0.66 * min_rate < frames <= 1 * min_rate:
            picker = random.randint(2, 3)
        if 1 * min_rate < frames <= 2 * min_rate:
            picker = random.randint(3, 7)
        if 2 * min_rate < frames <= 2.8 * min_rate:
            picker = random.randint(8, 12)
        if 2.8 * min_rate < frames <= 3.5 * min_rate:
            picker = -1
        if frames == int(3 * min_rate):
            picker = 13
        if 3.5 * min_rate < frames <= 5 * min_rate:
            picker = random.randint(14, 18)
        if frames == 4 * min_rate:
            picker = 13
        if 5 * min_rate < frames <= 7 * min_rate:
            picker = random.randint(13, 19)
        if frames > 7 * min_rate:
            picker = random.randint(14, 20)
        if frames == int(7 * min_rate):
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
                [enemies.Lizard(), enemies.Lizard(), enemies.Wolf(),
                 enemies.Wolf(), enemies.Orc(), enemies.Orc(),
                 enemies.Turtle(), enemies.Turtle(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider()])
        elif picker == 20:
            enemies_list.extend([enemies.Dragon(), enemies.Dragon()])


def draw_towers(tower_list, missile_list, funds, score_board, enemies_list):
    # Go through list of towers, drawing towers if not destroyed
    # Then drawing missiles to match appropriate tower
    for tower_location in tower_list:
        for current_tower in tower_location:
            if current_tower.constructing:
                current_tower.construct()
            if current_tower.selling:
                current_tower.sell()
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
                        new_tower.option_selected = None
                        new_tower.selling = True
                        new_tower.previous_sell_value = current_tower.sell
                        new_tower.sell_countdown = new_tower.sell_timer
                        current_tower.destroy = True
                        current_tower.option_selected = None
                        funds.adjust(current_tower.sell)
                        sell_tower_sound.play()
                    else:
                        if new_tower.buy <= funds.cash:
                            new_tower.constructing = True
                            new_tower.construct_countdown = \
                                new_tower.construct_timer
                            current_tower.destroy = True
                            current_tower.option_selected = None
                            funds.adjust(-new_tower.buy)
                            build_tower_sound.play()
                        else:
                            current_tower.option_selected = None
                current_tower.draw()

                if current_tower_index != 0:
                    tower_position = tower_list.index(tower_location)
                    if not current_tower.constructing:
                        missile = \
                            missile_list[tower_position][current_tower_index]
                        for enemy in enemies_list:
                            hit = missile.lock_enemy(
                                current_tower, enemy)
                            if hit:
                                damage, specialty, hit_sound = hit
                                enemy.hit(damage, specialty)
                                hit_sound.play()
                            kill = enemy.check_death()
                            if kill:
                                points, cash = kill
                                score_board.adjust(points)
                                funds.adjust(cash)
                        missile.adjust_counters()


def draw_enemies(enemies_list, castle):
    # Draw and move enemies
    # If enemies reach castle, damage castle
    for enemy in enemies_list:
        if enemy.lives == 0:
            enemies_list.pop(enemies_list.index(enemy))
        castle_damage = enemy.draw()

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
                castle_hit.play()


def draw_mage(mage, game_clock, score_board, funds, enemies_list):
    mage.draw(game_clock.frames)
    for enemy in enemies_list:
        if helpers.collision(mage, enemy):
            if not enemy.destroy:
                enemy.take_damage(3000, True)
        kill = enemy.check_death()
        if kill:
            points, cash = kill
            score_board.adjust(points)
            funds.adjust(cash)
        if mage.pop_enemies_counter == 0:
            enemies_list.pop(enemies_list.index(enemy))


def tower_costs_display():
    font = pygame.font.SysFont('Comic Sans MS', 16, bold=False)
    # Backdrop
    pygame.draw.rect(gameDisplay, black,
                     (275, display_height - 110, 175, 100))
    # Text
    helpers.blit_text(gameDisplay, tower_costs,
                      (282, display_height - 106), font, color=white)


if __name__ == "__main__":
    settings = generalClass.Settings()
    load_intro_music()
    pygame.quit()
    quit()
