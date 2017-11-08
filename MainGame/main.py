import random
import sys

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
    """Loads and plays music for Intro, explanation and settings screens"""
    pygame.mixer.music.load('music/Anamalie.mp3')
    pygame.mixer.music.play(-1)
    intro_loop()


def intro_loop():
    """First loop seen, explains game story with links to other loops

    Note: Texts stored in gameText.py
    """
    play_button = generalClass.Button(
        (450, display_height - 250),
        message="Play", action=game_loop, font_size=40, width=300, height=60)
    quit_button = generalClass.Button(
        (450, display_height - 180),
        message="Quit", action=sys.exit, font_size=40, width=300, height=60,
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
        message="Difficulty", action=settings_loop, font_size=40,
        width=300, height=60, color1=orange, color2=bright_orange)

    font = pygame.font.SysFont('Comic Sans MS', 20, bold=True)
    title_font = pygame.font.SysFont('Comic Sans MS', 72, bold=True)

    while True:
        # Activate quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
        clock.tick(30)


def tower_info_loop():
    """Shows and explains towers with buttons to navigate

    Note: Texts located in gameText.py
    """
    # Set buttons
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    previous_button = generalClass.Button(
        (50, display_height - 100), message="Previous", action="backward",
        font_size=40, width=200, height=60, color1=red, color2=bright_red)
    next_button = generalClass.Button(
        (600, display_height - 100), message="Next", action="forward",
        font_size=40, width=200, height=60, color1=green, color2=bright_green)
    # Set font
    font = pygame.font.SysFont('Comic Sans MS', 18, bold=True)
    # Set towers
    basic = towerClass.BasicTower((160, 400), destroy=False)
    ice1 = towerClass.IceTower1((155, 250), destroy=False)
    ice2 = towerClass.IceTower2((155, 530), destroy=False)
    fire1 = towerClass.FireTower1((155, 250), destroy=False)
    fire2 = towerClass.FireTower2((155, 530), destroy=False)
    poison1 = towerClass.PoisonTower1((155, 250), destroy=False)
    poison2 = towerClass.PoisonTower2((155, 530), destroy=False)
    dark1 = towerClass.DarkTower1((155, 250), destroy=False)
    dark2 = towerClass.DarkTower2((155, 530), destroy=False)
    # Define index for navigating pages
    info_index = 0
    while True:
        # Activate quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        pygame.draw.rect(gameDisplay, white,
                         (100, 125, 650, 525))
        # Draw buttons
        return_button.draw()
        next_tower = next_button.draw()
        previous_tower = previous_button.draw()
        # Define page navigation with index
        if next_tower:
            info_index += 1
        if previous_tower:
            info_index -= 1
        if info_index > 4:
            info_index = 0
        if info_index < 0:
            info_index = 4
        # Draw towers and tower info, pages indicated by index
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
        clock.tick(30)


def enemy_info_loop():
    """Show and explain enemies with buttons to navigate

    Note: Texts located in gameText.py
    """
    # Set buttons for page navigation
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    previous_button = generalClass.Button(
        (50, display_height - 100), message="Previous", action="backward",
        font_size=40, width=200, height=60, color1=red, color2=bright_red)
    next_button = generalClass.Button(
        (600, display_height - 100), message="Next", action="forward",
        font_size=40, width=200, height=60, color1=green, color2=bright_green)
    # Set font
    font = pygame.font.SysFont('Comic Sans MS', 18, bold=True)
    # Set enemies, indicating stationary=True and destroy=False
    spider = enemies.Spider((180, 250), (190, 250), True, False)
    lizard = enemies.Lizard((180, 530), (190, 530), True, False)
    wolf = enemies.Wolf((180, 250), (190, 250), True, False)
    turtle = enemies.Turtle((180, 530), (190, 530), True, False)
    orc = enemies.Orc((180, 250), (190, 250), True, False)
    dragon = enemies.Dragon((180, 530), (190, 530), True, False)
    # Define index for page navigation
    info_index = 0
    while True:
        # Activate quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        pygame.draw.rect(gameDisplay, white,
                         (100, 125, 650, 525))
        # Draw buttons
        return_button.draw()
        next_enemy = next_button.draw()
        previous_enemy = previous_button.draw()
        # Define page navigation with index
        if next_enemy:
            info_index += 1
        if previous_enemy:
            info_index -= 1
        if info_index > 2:
            info_index = 0
        if info_index < 0:
            info_index = 2
        # Draw enemies and enemy info, pages indicated by index
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
        clock.tick(30)


def settings_loop():
    """Allow user to adjust difficulty settings with buttons and explanations

    Note: Texts located in gameText.py
    """
    # Set buttons for difficulty selection and return to into_loop
    return_button = generalClass.Button(
        (50, 50), message="Return", action=intro_loop, font_size=40,
        width=200, height=60, color1=orange, color2=bright_orange)
    easy_button = generalClass.Button(
        (50, 200), message="Easy", action=easy_settings, font_size=40,
        width=200, height=60, color1=green, color2=bright_green, linked=True)
    medium_button = generalClass.Button(
        (50, 285), message="Medium", action=medium_settings, font_size=40,
        width=200, height=60, color1=yellow, color2=bright_yellow,
        linked=True)
    hard_button = generalClass.Button(
        (50, 370), message="Hard", action=hard_settings, font_size=40,
        width=200, height=60, color1=red, color2=bright_red, linked=True)
    # Set font for difficulty explanations
    font = pygame.font.SysFont('Comic Sans MS', 24, bold=True)

    while True:
        # Activate quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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
        clock.tick(30)


def easy_settings():
    """"Updates settings class to easy difficulty"""
    settings.spawn_rate = int(8 * seconds)
    settings.starting_gold = 1200
    settings.gold_generation = int(0.1 * seconds)
    settings.difficulty = 1.25


def medium_settings():
    """"Updates settings class to medium difficulty"""
    settings.spawn_rate = int(6 * seconds)
    settings.starting_gold = 1000
    settings.gold_generation = 0.5 * seconds
    settings.difficulty = 1


def hard_settings():
    """"Updates settings class to hard difficulty"""
    settings.spawn_rate = int(4 * seconds)
    settings.starting_gold = 800
    settings.gold_generation = int(2 * seconds)
    settings.difficulty = (2/3)


def unpause():
    """Un-pauses game and resumes music"""
    global pause
    pause = False
    pygame.mixer.music.unpause()


def pause_game():
    """Pauses game and music"""

    # Set navigation buttons
    resume_button = generalClass.Button(
        (20, 80), message="Resume", width=120, color1=green,
        color2=bright_green, action=unpause)

    reset_button = generalClass.Button(
        (20, 110), message="Reset", width=120, color1=red,
        color2=bright_red, action=game_loop)

    main_button = generalClass.Button(
        (20, 140), message="Main Menu", width=120, color1=yellow,
        color2=bright_yellow, action=load_intro_music)
    # Pause music
    pygame.mixer.music.pause()
    # Set global pause variable to True
    global pause
    pause = True

    while pause:
        # Activate quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    unpause()
        # Draw buttons
        resume_button.draw()
        reset_button.draw()
        main_button.draw()
        # Update game display
        pygame.display.update()


def game_loop():
    """Play the game

    This function sets up several buttons and texts to give info for game,
    then calls several other functions to run the game logic.
    """
    # Game crashes if loading new music while music is paused
    pygame.mixer.music.unpause()
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
    # Set up game rules with several stat trackers
    score = generalClass.Tracker(
        (140, 20), start_stat=0, width=120, height=30, background_color=green,
        font="Comic Sans MS", font_size=20, text_color=black, prefix="Score: ")
    game_clock = generalClass.Tracker(
        (20, 20), start_stat=0, width=120, height=30, background_color=black,
        font="Comic Sans MS", font_size=20, text_color=white, special="clock")
    funds = generalClass.Tracker(
        (20, display_height - 90), start_stat=start_cash, width=100, height=30,
        background_color=black, font="Comic Sans MS", font_size=20,
        text_color=white, prefix="$")
    castle = generalClass.Tracker(
        (20, display_height - 60), start_stat=20, width=250, height=50,
        background_color=red, front_color=green, font="Comic Sans MS",
        font_size=30, text_color=white, special="castle")
    # Set the end screen
    end_screen = generalClass.EndScreen()
    # Set blank enemies list
    enemies_list = []
    #
    # enemies_list.extend(
    #     [enemies.Lizard(), enemies.Lizard(), enemies.Wolf(),
    #      enemies.Wolf(), enemies.Orc(), enemies.Orc(),
    #      enemies.Turtle(), enemies.Turtle(), enemies.Spider(),
    #      enemies.Spider(), enemies.Spider(), enemies.Spider(),
    #      enemies.Spider(), enemies.Spider()])
    # Set towers' and missiles' lists
    bot_tower_list = []
    bot_missile_list = []
    top_tower_list = []
    top_missile_list = []
    # Call function to set up towers and missiles
    set_towers(bot_tower_locations, bot_tower_list, bot_missile_list)
    set_towers(top_tower_locations, top_tower_list, top_missile_list)
    # Set mage (for end game sequence)
    mage = enemies.Mage()

    # Actual game loop
    while True:
        # Set quit button and pause game listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_game()
        # Update game_clock by 1 per frame
        game_clock.stat += 1
        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)
        # Periodically add money
        if game_clock.stat % passive_money_rate == 0:
            funds.adjust(1)
        # Call function to add enemies
        if not mage.stop_spawn:
            add_enemies(game_clock.stat, enemies_list, enemy_spawn_rate,
                        difficulty)
        # Call function to draw top-side towers
        draw_towers(top_tower_list, top_missile_list, funds,
                    score, enemies_list)
        # Call function to draw enemies
        draw_enemies(enemies_list, castle)
        # Call function to draw bottom-side towers
        draw_towers(bot_tower_list, bot_missile_list, funds,
                    score, enemies_list)
        # Call function to draw mage (end of game sequence)
        draw_mage(mage, game_clock, score, funds, enemies_list)
        # Draw game info panels
        tower_costs_display()
        funds.draw()
        castle.draw()
        score.draw()
        game_clock.draw()
        pause_button.draw()
        # Check for win/lose conditions
        win_lose(mage, end_screen, score, game_clock, castle)
        # Update game
        pygame.display.update()
        clock.tick(30)


def set_towers(tower_locations, tower_list, missile_list):
    """Sets one of each tower/missile type at each pre-defined location

    Function sets one of each tower type object and one of each missile type
    object at each location indicated by tower_list, and effectively links the
    tower and missile lists by keeping consistent the index of each tower
    type with its corresponding missile type at a given location.

    Args:
        tower_locations (list of int,int tuples):
            A list of x, y coordinates for locations of tower placements
        tower_list (list of obj): A list for storing towers added
        missile_list (list of obj): A list for storing missiles added
    """
    for tower_location in tower_locations:  # See lists.py
        tower_list.append([
            towerClass.TowerButton(tower_location),
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
    """Adds enemies to enemies_list, ramping up difficulty over time.

    Function adds an enemy object or group of enemy objects to the enemies_list
    at intervals pre-defined by enemy_spawn_rate (from settings). It picks
    which enemy or group of enemies to add with 'picker' variable which gets
    set purposefully or randomly with random.randint to a number defined by
    the game frames (time) in the game (modified through 'difficulty' setting).
    Enemies are then appended/extended to enemies_list based on the 'picker'.

    Args:
        frames (int): The number of game frames since start of game
                      (estimates time)
        enemies_list (list of obj): A list for which to append/extend
                                    enemy objects onto
        enemy_spawn_rate (int): Difficulty setting that places interval
                                of enemy spawn
        difficulty (int): difficulty setting that defines how quickly
                          difficulty of enemy spawns ramps up
    """
    # Define 'picker' variable
    picker = -1
    # Change picker and add enemies at interval of enemy_spawn_rate
    if frames % enemy_spawn_rate == 0:
        # Define rate of 'picker' ramp up based on difficulty
        min_rate = minutes * difficulty
        # Set the 'picker' based on frames (time) past and difficulty
        if frames <= 0.2 * min_rate:
            picker = 0
        if 0.2 * min_rate < frames <= .5 * min_rate:
            picker = 1
        if 0.5 * min_rate < frames <= 1 * min_rate:
            picker = random.randint(2, 3)
        if 1 * min_rate < frames <= 2 * min_rate:
            picker = random.randint(3, 7)
        if 2 * min_rate < frames <= 2.9 * min_rate:
            picker = random.randint(8, 12)
        if 2.9 * min_rate < frames <= 3.5 * min_rate:
            pass
        if int((3 * min_rate) - (2 * seconds)) < frames <= \
                int((3 * min_rate) + (2 * seconds)):
            picker = 13
        if 3.5 * min_rate < frames <= 3.75 * min_rate:
            picker = random.randint(8, 12)
        if 3.75 * min_rate < frames <= 4.5 * min_rate:
            picker = random.randint(14, 18)
        if int((4 * min_rate) - (2 * seconds)) < frames <= \
                int((4 * min_rate) + (2 * seconds)):
            picker = 13
        if 4.5 * min_rate < frames <= 5 * min_rate:
            picker = random.randint(15, 19)
        if int((4.5 * min_rate) - (2 * seconds)) < frames <= \
                int((4.5 * min_rate) + (2 * seconds)):
            picker = 20
        if 5 * min_rate < frames <= 5.75 * min_rate:
            picker = random.randint(15, 20)
        if 5.75 * min_rate < frames <= 6.5 * min_rate:
            picker = random.randint(20, 24)
        if frames > 6.5 * min_rate:
            picker = random.randint(20, 24)

        # Append or extend list with enemies indicated by 'picker'
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
            enemies_list.extend(
                [enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider()])
        elif picker == 15:
            enemies_list.extend([enemies.Lizard(), enemies.Lizard(),
                                 enemies.Lizard()])
        elif picker == 16:
            enemies_list.extend([enemies.Wolf(), enemies.Wolf(),
                                 enemies.Wolf()])
        elif picker == 17:
            enemies_list.extend([enemies.Orc(), enemies.Orc(), enemies.Orc()])
        elif picker == 18:
            enemies_list.extend([enemies.Turtle(), enemies.Turtle(),
                                 enemies.Turtle()])
        elif picker == 19:
            enemies_list.extend(
                [enemies.Lizard(), enemies.Lizard(), enemies.Wolf(),
                 enemies.Wolf(), enemies.Orc(), enemies.Orc(),
                 enemies.Turtle(), enemies.Turtle(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider()])
        elif picker == 20:
            enemies_list.extend([enemies.Dragon(), enemies.Dragon()])
        elif picker == 21:
            enemies_list.extend([enemies.Lizard(), enemies.Lizard(),
                                 enemies.Lizard(), enemies.Lizard()])
        elif picker == 22:
            enemies_list.extend([enemies.Wolf(), enemies.Wolf(),
                                 enemies.Wolf(), enemies.Wolf()])
        elif picker == 23:
            enemies_list.extend([enemies.Orc(), enemies.Orc(),
                                 enemies.Orc(), enemies.Orc()])
        elif picker == 24:
            enemies_list.extend([enemies.Turtle(), enemies.Turtle(),
                                 enemies.Turtle(), enemies.Turtle()])
        elif picker == 25:
            enemies_list.extend(
                [enemies.Lizard(), enemies.Lizard(), enemies.Wolf(),
                 enemies.Wolf(), enemies.Orc(), enemies.Orc(),
                 enemies.Turtle(), enemies.Turtle(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider(), enemies.Spider(),
                 enemies.Spider(), enemies.Spider()])
        elif picker == 26:
            enemies_list.extend([enemies.Dragon(), enemies.Dragon(),
                                 enemies.Dragon()])
        elif picker == 27:
            enemies_list.extend([enemies.Lizard(), enemies.Lizard(),
                                 enemies.Lizard(), enemies.Lizard(),
                                 enemies.Wolf(), enemies.Wolf()])
        elif picker == 28:
            enemies_list.extend([enemies.Wolf(), enemies.Wolf(),
                                 enemies.Wolf(), enemies.Wolf(),
                                 enemies.Orc(), enemies.Orc()])
        elif picker == 29:
            enemies_list.extend([enemies.Orc(), enemies.Orc(),
                                 enemies.Orc(), enemies.Orc(),
                                 enemies.Turtle(), enemies.Turtle()])
        elif picker == 30:
            enemies_list.extend([enemies.Turtle(), enemies.Turtle(),
                                 enemies.Turtle(), enemies.Turtle(),
                                 enemies.Lizard(), enemies.Lizard()])


def draw_towers(tower_list, missile_list, funds, score_board, enemies_list):
    """Draw towers and associated missiles, and run their logic

    Goes through list of towers, drawing towers if not destroyed, then drawing
    missiles to match appropriate tower. Allows for buying new towers and
    selling current towers. Missiles of associated towers detect enemies,
    lock on, and hit enemies, transferring damage and associated effects to
    enemies. Detects enemy deaths and records associated points and money.

    Args:
        tower_list (list of list of obj): List of towers locations
                                          containing a list of tower objects
        missile_list (list of list of obj):
            List of missiles to draw (tied by first index to towers
            location and second index to tower object types).
        funds (obj): Players current amount of money object
        score_board (obj): Players current score object
        enemies_list (list of obj): List of enemies
    """
    # Iterate over all tower locations and towers at a given location
    for tower_location in tower_list:
        for current_tower in tower_location:
            # Construct towers if just bought
            if current_tower.constructing:
                current_tower.construct()
                current_tower.option_selected = None
                current_tower.option_lockout = True
            # Sell towers if just sold
            if current_tower.selling:
                current_tower.sell()
                current_tower.option_selected = None
                current_tower.option_lockout = True
            # If tower is activated (not destroyed)
            if not current_tower.destroy:
                # gray out and disallow purchase of towers above players moeny
                if current_tower.tier == 0:
                    if funds.stat < 100:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                if current_tower.tier == 1:
                    if funds.stat < 125:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                if current_tower.tier == 2:
                    if funds.stat < 150:
                        current_tower.gray_out = True
                    else:
                        current_tower.gray_out = False
                # Get selection from towers options (listened for by tower)
                selected = current_tower.option_selected
                # Turn selected tower option into an index (for tower list)
                new_tower_index = tower_types.get(selected)  # See lists.py
                # Get current tower's index in tower list
                current_tower_index = tower_location.index(current_tower)
                # Perform actions on current tower's selected option
                if selected:
                    # Get new tower at current location based on selected index
                    new_tower = tower_location[new_tower_index]
                    # Sell tower if that option was selected
                    if selected == "sell":
                        new_tower.option_selected = None
                        new_tower.option_lockout = True
                        new_tower.selling = True
                        new_tower.previous_sell_value = current_tower.sell
                        new_tower.sell_countdown = new_tower.sell_timer
                        current_tower.option_selected = None
                        current_tower.option_lockout = True
                        current_tower.destroy = True
                        funds.adjust(current_tower.sell)
                        sell_tower_sound.play()
                    # Else option will be buy. Buy if player has enough money
                    else:
                        if new_tower.buy <= funds.stat:
                            new_tower.constructing = True
                            new_tower.construct_countdown = \
                                new_tower.construct_timer
                            current_tower.option_selected = None
                            current_tower.destroy = True
                            funds.adjust(-new_tower.buy)
                            build_tower_sound.play()
                        else:
                            current_tower.option_selected = None
                # Draw tower on map
                current_tower.draw()
                # Run logic for missile associated with tower
                if current_tower_index != 0:
                    tower_position = tower_list.index(tower_location)
                    # Don't run logic while tower is building
                    if not current_tower.constructing:
                        # Define missile for tower location and tower type
                        missile = \
                            missile_list[tower_position][current_tower_index]
                        # Iterate over enemies, locking on and firing at them
                        for enemy in enemies_list:
                            # If striking enemy return damage and special type
                            hit = missile.lock_enemy(
                                current_tower, enemy)
                            if hit:
                                damage, specialty, hit_sound = hit
                                enemy.hit(damage, specialty)
                                hit_sound.play()
                            # If enemy dies due to shot give player money/points
                            kill = enemy.check_death()
                            if kill:
                                points, cash = kill
                                score_board.adjust(points)
                                funds.adjust(cash)
                        # Update counter associated with missile
                        missile.adjust_counters()


def draw_enemies(enemies_list, castle):
    """Draw enemies, damage castle if appropriate and check enemy interactions

    Enemies struck by fire tower will light other nearby enemies on fire.
    Function will pop enemies from enemies_list once they die and have 0 lives.
    Enemies will damage castle if they reach it.

    Args:
        enemies_list (list of obj): list of all enemies in play
        castle (obj): Castle object determines game loss if too many hits
    """
    # Iterate over all enemies
    for enemy in enemies_list:
        # Pop from list after last death
        if enemy.lives == 0:
            enemies_list.pop(enemies_list.index(enemy))
        # Check for enemies damaging castle
        castle_damage = enemy.draw()

        # Check for enemies lit on fire by fire tower
        # Light other nearby enemies on fire if current enemy is aflame
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
        # Reduce castle health if enemy reaches castle
        if castle_damage:
            if castle.stat > 0:
                castle.adjust(-castle_damage)
                castle_hit.play()


def draw_mage(mage, game_clock, score_board, funds, enemies_list):
    """Draw mage, kill enemies if spell hits them, pop enemies from enemies_list

    Args:
        mage (obj): The mage hero object to draw and interact with enemies
        game_clock (obj): Game time to pass to mage
        score_board (obj): Score to adjust when enemies die
        funds (obj): Players money to adjust when enemies die
        enemies_list (list of obj): List of enemies for mage to interact with
    """
    # Draw mage
    mage.draw(game_clock.stat)
    # Kill enemies hit by mage spell and collect their points/money
    for enemy in enemies_list:
        if helpers.collision(mage, enemy):
            if not enemy.destroy:
                enemy.take_damage(3000, True)
        kill = enemy.check_death()
        if kill:
            points, cash = kill
            score_board.adjust(points)
            funds.adjust(cash)
        # Pop enemies from from enemy_list when indicated by mage
        if mage.pop_enemies_counter == 0:
            enemies_list.pop(enemies_list.index(enemy))


def tower_costs_display():
    """Draws a display of tower costs"""
    # Font
    font = pygame.font.SysFont('Comic Sans MS', 16, bold=False)
    # Backdrop
    pygame.draw.rect(gameDisplay, black,
                     (275, display_height - 110, 175, 100))
    # Text
    helpers.blit_text(gameDisplay, tower_costs,
                      (282, display_height - 106), font, color=white)


def win_lose(mage, end_screen, score, game_clock, castle):
    """Determines conditions for winning or losing and directs to end screen

    Args:
        mage (obj): Mage object determines win condition
        end_screen (obj): End Screen object shows victory/defeat screen
        score (obj): Players score to pass to end_screen
        game_clock (obj): Games clock used to show end_screen game time
        castle (obj): Castle object determines lose condition
    """
    # Set win condition
    if mage.win:
        end_screen.score = score.stat
        end_screen.time_elapsed = game_clock.stat
        end = end_screen.draw("win")
        if end == "play":
            game_loop()
        if end == "main":
            load_intro_music()
    # Set lose condition
    if castle.game_over:
        end_screen.score = score.stat
        end_screen.time_elapsed = game_clock.stat
        end = end_screen.draw("lose")
        if end == "play":
            game_loop()
        if end == "main":
            load_intro_music()


if __name__ == "__main__":
    # Globally define pause for game pausing/un-pausing functions
    pause = False
    settings = generalClass.Settings()
    medium_settings()
    load_intro_music()
    sys.exit()
