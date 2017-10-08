def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(x_coord, y_coord, width, height, color):
    pygame.draw_main.rect(gameDisplay, color, [x_coord, y_coord, width, height])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects("You crashed", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play again", 150, 450, 125, 50, green, bright_green, game_loop)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def button(message, x_coord, y_coord, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_coord + width > mouse[0] > x_coord and y_coord + height > mouse[1] > y_coord:
        pygame.draw_main.rect(gameDisplay, active_color, (x_coord, y_coord, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw_main.rect(gameDisplay, inactive_color, (x_coord, y_coord, width, height))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(message, small_text)
    text_rect.center = ((x_coord + width / 2), (y_coord + height / 2))
    gameDisplay.blit(text_surf, text_rect)


def quit_game():
    pygame.quit()
    quit()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("A bit Racey", large_text)
        text_rect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(text_surf, text_rect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()


def pause_game():
    global pause
    pause = True
    pygame.mixer.music.pause()

    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects("Paused", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)
