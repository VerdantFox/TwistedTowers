class EndScreen:
    def __init__(self):
        self.score_x = display_width // 2
        self.score_y = display_height * 3 // 2
        self.score = 0
        self.score_width = 90
        self.score_height = 30
        self.score_background = None
        self.score_font = pygame.font.SysFont("Comic Sans MS", 72)
        self.text_color = black
        self.play_button = Button(
            (display_width * 2 // 3, display_height * 2 // 3), message="Play",
            action=game_loop)
        self.quit_button = Button(
            (display_width * 3 // 2, display_height * 2 // 3), message="Quit",
            action=quit)

    def draw(self):
        # pygame.mixer.music.stop()
        # pygame.mixer.Sound.play(castle_falls)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

            self.play_button.draw()
            self.quit_button.draw()
            pygame.display.update()
            clock.tick(30)