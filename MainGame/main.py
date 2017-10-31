import pygame
import generalClass
import towerClass
import enemies
import helpers
import random
from definitions import *
from lists import *
from gameParameters import backgroundImage, gameDisplay, display_height, clock


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
    text = "The time to act is now! Lord Darken has set his armies of " \
           "the damned upon the innocents within StoneBorn Castle. As " \
           "general of the Resistance Army it is your duty to direct the " \
           "building of our static tower defenses. Enlist the help of " \
           "our builders and the magician, Jorah, to erect magical towers to" \
           " keep our enemies at bay. Our fighters within the keep can " \
           "hold off only a limited number of enemies before the " \
           "castle falls. A raven has been sent to the Archmage Stormbender. " \
           "If we can just hold long enough I know he can save us..."
    title = "Teddy's Towers!"
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
        helpers.blit_text(gameDisplay, text, (100, 150), font, margin=100)
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
    basic_tower_text = "Basic Tower (Tier 1 Tower):\n" \
                       "\nTier 1 tower, does normal damage." \
                       "\nDamage:            50 per hit" \
                       "\nRate of fire:       every other second" \
                       "\nCost: $100" \
                       "\nSells for: $75" \
                       "\nSpecial attributes: None"
    ice1_text = "Rank 1 Ice Tower (Tier 2 Tower):\n" \
                "\nDoes normal damage and slows 30%." \
                "\nDamage:         37.5 damage per hit" \
                "\nRate of fire:    Once per second" \
                "\nCost:            Basic Tower + $125 ($225 total)" \
                "\nSells for:        $170" \
                "\nRecommend: Pair with dark towers for extra hits."
    ice2_text = "Rank 2 Ice Tower (Tier 3 Tower):\n" \
                "\n1.5x rank1 damage, double slow (60%)." \
                "\nDamage:        56.25 damage per hit" \
                "\nRate of fire:   Once per second" \
                "\nCost:           Rank 1 + $150 ($375 total)" \
                "\nSells for:       $280" \
                "\nRecommend: Pair with dark towers for extra hits."
    fire1_text = "Rank 1 Fire  (Tier 2 Tower):\n" \
                 "\nDoes damage over time in area of effect." \
                 "\nDamage:         75 damage over 3 seconds" \
                 "\nRate of fire:    Once per 3 seconds" \
                 "\nCost:            Basic Tower + $125 ($225 total)" \
                 "\nSells for:        $170" \
                 "\nRecommend: vs. bunched enemies (spiders)."
    fire2_text = "Rank 2 Fire Tower (Tier3 tower):\n" \
                 "\n1.5x rank1 damage, 1st target catches other enemies " \
                 "aflame in larger area." \
                 "\nDamage:        112.5 damage over 3 seconds" \
                 "\nRate of fire:   Once per second" \
                 "\nCost:           Rank 1 + $150 ($375 total)" \
                 "\nSells for:       $280" \
                 "\nRecommend: vs. bunched enemies (spiders)."
    poison1_text = "Rank 1 Poison Tower (Tier2 tower) :\n" \
                   "\nDoes % current hp over time, 50% armor shred, stuns" \
                   "for 0.75 seconds at last damage tic." \
                   "\nDamage:        ~22% current hp over 10 seconds" \
                   "\nRate of fire:    Once per 3 seconds" \
                   "\nCost:            Basic Tower + $125 ($225 total)" \
                   "\nSells for:        $170" \
                   "\nRecommend: vs high hp enemies (Orc, Dragon)."
    poison2_text = "Rank 2 Poison Tower (Tier3 tower):\n" \
                   "\n1.5x rank1 damage, double stun (1.5 seconds)." \
                   "\nDamage:        ~41% current hp over 10 seconds" \
                   "\nRate of fire:   Once per second" \
                   "\nCost:           Rank 1 + $150 ($375 total)" \
                   "\nSells for:       $280" \
                   "\nRecommend: vs high hp enemies (Orc, Dragon)."
    dark1_text = "Rank 1 Dark Tower (Tier2 tower) :\n" \
                 "\nDoes damage on hit ignoring 50% of enemy armor" \
                 "for 0.75 seconds at last damage tic." \
                 "\nDamage:        75 damage per hit" \
                 "\nRate of fire:    Every other second" \
                 "\nCost:            Basic Tower + $125 ($225 total)" \
                 "\nSells for:        $170" \
                 "\nRecommend: vs. high armor enemies (Spiker, Dragon)."
    dark2_text = "Rank 2 Dark Tower (Tier3 tower):\n" \
                 "\n1.5x rank1 damage, double stun (1.5 seconds)." \
                 "\nDamage:        ~41% current hp over 10 seconds" \
                 "\nRate of fire:   Once per second" \
                 "\nCost:           Rank 1 + $150 ($375 total)" \
                 "\nSells for:       $280" \
                 "\nRecommend: vs. high armor enemies (Spiker, Dragon)."

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
    spider_text = "Spider\n" \
                  "\nIndividually weak but forms large groups" \
                  "\nHealth:     100" \
                  "\nArmor:      0" \
                  "\nSpeed:      1.2" \
                  "\nKill value:   $8" \
                  "\nRecommend: Fire towers most effective."
    lizard_text = "Lizard Men\n" \
                  "\nWell rounded foot soldier of medium difficulty" \
                  "\nHealth:     300" \
                  "\nArmor:      50 (50% reduced damage)" \
                  "\nSpeed:      1.2" \
                  "\nKill value:   $50" \
                  "\nRecommend: All towers fairly equally effective."
    wolf_text = "Demon Wolf\n" \
                "\nNot particularly strong, but very fast" \
                "\nHealth:     240" \
                "\nArmor:      20 (20% reduced damage)" \
                "\nSpeed:      2" \
                "\nKill value:   $50" \
                "\nRecommend: Numerous and well spaced towers."
    turtle_text = "Spikers\n" \
                  "\nSlow, but highly armored enemy with low health" \
                  "\nHealth:     200" \
                  "\nArmor:      90 (90% reduced damage)" \
                  "\nSpeed:      0.8" \
                  "\nKill value:   $75" \
                  "\nRecommend: Dark towers most effective."
    orc_text = "Orc\n" \
               "\nFairly slow, low armor, but high health" \
               "\nHealth:      800" \
               "\nArmor:      20 (20% reduced damage)" \
               "\nSpeed:      1" \
               "\nKill value:   $75" \
               "\nRecommend: Early poison towers."
    dragon_text = "Dragon\n" \
                  "\nThe big one! Slow, with HIGH health and armor" \
                  "\nHealth:      2000" \
                  "\nArmor:      75 (75% reduced damage)" \
                  "\nSpeed:      0.6" \
                  "\nKill value:   $750" \
                  "\nRecommend: Early poison towers and dark towers " \
                  "               paired with ice towers for extra hits."

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
            spider.move()
            lizard.move()
            helpers.blit_text(gameDisplay, spider_text, (275, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, lizard_text, (275, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 1:
            wolf.move()
            turtle.move()
            helpers.blit_text(gameDisplay, wolf_text, (275, 135),
                              font, margin=125)
            helpers.blit_text(gameDisplay, turtle_text, (275, 400),
                              font, margin=125)
            pygame.draw.rect(gameDisplay, black,
                             (150, 385, 550, 5))
        if info_index == 2:
            orc.move()
            dragon.move()
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
    # sound_off_button = generalClass.Button(
    #     (display_width * 2 // 3 - 100, display_height * 2 // 3),
    #     message="Hard", action=settings_loop, font_size=40,
    #     width=300, height=60, color1=orange, color2=bright_orange)
    # Sound_on_button = generalClass.Button(
    #     (display_width * 2 // 3 - 100, display_height * 2 // 3),
    #     message="Hard", action=settings_loop, font_size=40,
    #     width=300, height=60, color1=orange, color2=bright_orange)

    easy_text = "Enemies will spawn more slowly, passive gold generation up, " \
                "higher starting gold."
    medium_text = "Normal spawn, gold generation, and starting gold."
    hard_text = "Fastest spawn rate, normal gold generation, " \
                "lower starting gold."
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
    settings.spawn_rate = 10 * seconds
    settings.starting_gold = 1600
    settings.gold_generation = 0.5 * seconds
    settings.difficulty = 2


def medium_settings():
    settings.spawn_rate = 7 * seconds
    settings.starting_gold = 1200
    settings.gold_generation = 1 * seconds
    settings.difficulty = 1


def hard_settings():
    settings.spawn_rate = 5 * seconds
    settings.starting_gold = 800
    settings.gold_generation = 2 * seconds
    settings.difficulty = 1


pause = False


def unpause():
    global pause
    pause = False


def pause_game():

    resume_button = generalClass.Button(
        (20, 80), message="Resume", width=120, color1=green,
        color2=bright_green, action=unpause)

    reset_button = generalClass.Button(
        (20, 110), message="Reset", width=120, color1=red,
        color2=bright_red, action=game_loop)

    main_button = generalClass.Button(
        (20, 140), message="Main Menu", width=120, color1=yellow,
        color2=bright_yellow, action=intro_loop)

    global pause
    pause = True
    # pygame.mixer.music.pause()
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

    # Blank list
    enemies_list = []

    # Fast enemies

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

    # # 10 wolves
    # enemies_list = [enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
    #                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
    #                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
    #                 enemies.Wolf(), enemies.Wolf(), enemies.Wolf(),
    #                 ]

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
            # print(event)

        # Draw background
        gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

        # add new enemies
        if not mage.stop_spawn:
            add_enemies(game_clock.frames, enemies_list, enemy_spawn_rate,
                        difficulty)

        # Draw top towers
        draw_towers(top_tower_list, top_missile_list, funds,
                    score_board, enemies_list)
        # Draw enemies
        draw_enemies(enemies_list, castle)
        # Draw bot towers
        draw_towers(bot_tower_list, bot_missile_list, funds,
                    score_board, enemies_list)

        # Draw in mage
        draw_mage(mage, game_clock, score_board, funds, enemies_list)

        funds.draw()
        castle.draw()
        score_board.draw()
        game_clock.draw()
        pause_button.draw()
        pygame.display.update()
        clock.tick(60)
        if mage.win:
            end_screen.score = score_board.score
            end_screen.time_elapsed = game_clock.frames
            end = end_screen.draw("win")
            if end == "play":
                game_loop()
            if end == "main":
                intro_loop()
        if castle.game_over:
            end_screen.score = score_board.score
            end_screen.time_elapsed = game_clock.frames
            end = end_screen.draw("lose")
            if end == "play":
                game_loop()
            if end == "main":
                intro_loop()
        if game_clock.frames % passive_money_rate == 0:
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
        if frames == 3 * min_rate:
            picker = 13
        if 3.5 * min_rate < frames <= 5 * min_rate:
            picker = random.randint(14, 18)
        if frames == 4 * min_rate:
            picker = 13
        if 5 * min_rate < frames <= 7 * min_rate:
            picker = random.randint(13, 19)
        if frames > 7 * min_rate:
            picker = random.randint(14, 20)
        if frames == 7 * min_rate:
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


if __name__ == "__main__":
    settings = generalClass.Settings()
    intro_loop()
    pygame.quit()
    quit()
