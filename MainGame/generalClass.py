import pygame
from definitions import *
from gameParameters import backgroundImage, gameDisplay, display_width, \
    display_height, clock
# import main


class Button:
    """Class for rectangular buttons

    Attributes:


    """
    def __init__(self, location, width=80, height=30,
                 message=None, color1=green, color2=bright_green,
                 action=None, font="Comic Sans MS", font_size=20,
                 message_color=black, permanent=False):
        self._mouse = None
        self._click = None
        self._message = message
        self.x, self.y = location
        self._width = width
        self._height = height
        self._color1 = color1
        self._color2 = color2
        self._action = action
        self._font = pygame.font.SysFont(font, font_size)
        self._message_color = message_color
        self.permanent = permanent
        self.selected = False
        self.selected_color = purple
        self.selected_text_color = white
        self.clickable = True
        self.unclickable_timer = 0.3 * seconds
        self.unclickable_countdown = 0

    def draw(self, *args):
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        # If mouse hovering button
        if (self.x < self._mouse[0] < self.x + self._width
                and self.y <
                self._mouse[1] <
                self.y + self._height):
            if self.selected:
                pygame.draw.rect(
                    gameDisplay, self.selected_color,
                    (self.x, self.y, self._width, self._height))
            else:
                pygame.draw.rect(
                    gameDisplay, self._color2,
                    (self.x, self.y, self._width, self._height))
            if self._click[0] == 1 and self._action is not None:
                if self.clickable:
                    self.clickable = False
                    self.unclickable_countdown = self.unclickable_timer
                    if self.permanent:
                        self.selected = True
                        for arg in args:
                            arg.selected = False
                    if isinstance(self._action, str):
                        return self._action
                    else:
                        self._action()

        # If mouse not hovering over button
        else:
            if self.selected:
                pygame.draw.rect(
                    gameDisplay, self.selected_color,
                    (self.x, self.y, self._width, self._height))
            else:
                pygame.draw.rect(
                    gameDisplay, self._color1,
                    (self.x, self.y, self._width, self._height))
        if self._message:
            self.set_text()

        # Can button be clicked?
        if self.unclickable_countdown > 0:
            self.unclickable_countdown -= 1
            self.clickable = False
        else:
            self.clickable = True

    def set_text(self):
        if self.selected:
            text_surface = self._font.render(
                self._message, True, self.selected_text_color)
        else:
            text_surface = self._font.render(
                self._message, True, self._message_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)


class GameScore:
    def __init__(self, location, width=120, height=30, background_color=green,
                 font="Comic Sans MS", font_size=20, message_color=black):
        self.x, self.y = location
        self.score = 0
        self._width = width
        self._height = height
        self._background_color = background_color
        self._font = pygame.font.SysFont(font, font_size)
        self.text_color = message_color
        self.background = True

    def draw(self):
        if self.background:
            pygame.draw.rect(
                gameDisplay, self._background_color,
                (self.x, self.y, self._width, self._height))
        self.set_text()

    def set_text(self):
        text_surface = self._font.render(
            "Score: " + str(self.score), True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)

    def adjust(self, amount):
        self.score += amount


class GameClock:
    def __init__(self, location, width=120, height=30, background_color=black,
                 font="Comic Sans MS", font_size=20, message_color=white):
        self.x, self.y = location
        self.frames = 0
        self._width = width
        self._height = height
        self._background_color = background_color
        self._font = pygame.font.SysFont(font, font_size)
        self.text_color = message_color
        self.background = True

    def draw(self):
        if self.background:
            pygame.draw.rect(
                gameDisplay, self._background_color,
                (self.x, self.y, self._width, self._height))
        self.set_text()
        self.frames += 1

    def set_text(self):
        minutes_elapsed = self.frames // minutes
        remaining_seconds = (self.frames % minutes) // seconds
        text_surface = self._font.render(
            "Time: {0}:{1:02}".format(minutes_elapsed, remaining_seconds),
            True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)


class Money:
    def __init__(self, location, width=100, height=30, start_cash=400,
                 background_color=black, font="Comic Sans MS", font_size=20,
                 message_color=white):
        self.x, self.y = location
        self.cash = start_cash
        self._width = width
        self._height = height
        self._background_color = background_color
        self._font = pygame.font.SysFont(font, font_size)
        self.text_color = message_color
        self.background = True

    def adjust(self, amount):
        self.cash += amount

    def draw(self):
        if self.background:
            pygame.draw.rect(
                gameDisplay, self._background_color,
                (self.x, self.y, self._width, self._height))
        self.set_text()

    def set_text(self):
        text_surface = self._font.render(
            "$" + str(self.cash), True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)


class Castle:
    def __init__(self, health_location, width=250, height=50, max_health=10,
                 back_color=red, front_color=green, font="Comic Sans MS",
                 font_size=30, message_color=white):
        self.x, self.y = health_location
        self.max_hp = max_health
        self.hp = max_health
        self._width = width
        self._height = height
        self._back_color = back_color
        self._front_color = front_color
        self._font = pygame.font.SysFont(font, font_size)
        self.text_color = message_color
        self.background = True
        self.game_over = False

    def adjust(self, amount):
        self.hp += amount

    def draw(self):
        if self.background:
            if self.hp > 0:
                damage_width = int(self._width * self.hp // self.max_hp)
            else:
                damage_width = 0

            pygame.draw.rect(
                gameDisplay, self._back_color,
                (self.x, self.y, self._width, self._height))
            pygame.draw.rect(
                gameDisplay, self._front_color,
                (self.x, self.y, damage_width, self._height))

        self.set_text()

        if self.hp <= 0:
            self.game_over = True

    def set_text(self):
        text_surface = self._font.render(
            "Castle: {}/{}".format(self.hp, self.max_hp),
            True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)


class EndScreen:
    def __init__(self):
        self.center_x = display_width // 2
        self.game_y = 100
        self.score_y = 250
        self.time_y = 325
        self.score = 0
        self.time_elapsed = 0  # Game time approximation, based on frames (slow)
        self.game_font = pygame.font.SysFont("Comic Sans MS", 120)
        self.score_font = pygame.font.SysFont("Comic Sans MS", 80)
        self.time_font = pygame.font.SysFont("Comic Sans MS", 40)
        self.text_color = black
        self.play_button = Button(
            (75, display_height - 300), message="Play", action="play",
            font_size=40, width=200, height=60, color1=green,
            color2=bright_green)
        self.main_button = Button(
            (325, display_height - 300), message="Main menu", action="main",
            font_size=40, width=200, height=60, color1=yellow,
            color2=bright_yellow)
        self.quit_button = Button(
            (575, display_height - 300), message="Quit", action=quit,
            font_size=40, width=200, height=60, color1=red, color2=bright_red)

    def draw(self, win_loss):
        # pygame.mixer.music.stop()
        # pygame.mixer.Sound.play(castle_falls)

        minutes_elapsed = self.time_elapsed // minutes
        remaining_seconds = (self.time_elapsed % minutes) // seconds
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.blit(backgroundImage.image, backgroundImage.rect)

            # Draw "Defeat/Victory" text
            if win_loss == "lose":
                self.set_text(self.center_x, self.game_y, "Defeat!",
                              self.game_font)
            if win_loss == "win":
                self.set_text(self.center_x, self.game_y, "Victory!!",
                              self.game_font)

            # Draw "Score" text
            self.set_text(self.center_x, self.score_y,
                          "score: {}".format(self.score), self.score_font)

            # Draw "Time elapsed" text
            self.set_text(self.center_x, self.time_y, "Time: {0}:{1:02}".format(
                    minutes_elapsed, remaining_seconds), self.time_font)

            # Draw quit button
            self.quit_button.draw()
            # Draw play button
            play = self.play_button.draw()
            if play == "play":
                return play
            # Draw main button
            main = self.main_button.draw()
            if main == "main":
                return main
            # Update game
            pygame.display.update()
            clock.tick(30)

    def set_text(self, x, y, message, font):
        text_surface = font.render(message, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)


class Settings:
    def __init__(self):
        self.spawn_rate = 5 * seconds
        self.gold_generation = 1 * seconds
        self.starting_gold = 1000
        self.difficulty = 1
