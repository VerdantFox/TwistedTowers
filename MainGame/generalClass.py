import pygame
from definitions import *
from gameParameters import backgroundImage, gameDisplay, display_width, \
    display_height, clock
# import main


class Button:
    """Class for rectangular buttons

    Args:
        location (tuple, int): Defines self.x, self.y
        width (int, default=80): Defines self._width
        height (int, default=30): Defines self._height
        message (str, default=None): Defines self._message
        color1 (tuple, int, default=green): Defines self._color1
        color2 (tuple, int, default=bright_green): Defines self._color2
        action (func or str, default=None): Defines self._action
        font (default="Comic Sans MS"): Defines self._font
        font_size (int, default=20): Defines self.font_size
        message_color (tuple, int, default=black): Defines self._message_color
        linked (bool, default=False): Defines self.linked

    Attributes:
        _mouse: Tracks mouse position
        _click: Tracks mouse button clicking
        _message (str): The message written on center of button
        x, y (tuple, int): Location of upper left corner of button rectangle
        _width (int): Width of button rectangle
        _height (int): Height of button rectangle
        _color1 (tuple, int): Color of button while mouse not hovering
        _color2 (tuple, int): Color of button while mouse is hovering
        _action (function or str): Calls _action() as a function if function,
                                   else returns _action if string
        _font: Font object for button text
        _message_color (tuple, int): Color of text on button
        linked (bool): If True, indicates button should expect other buttons
                          linked to it, for selection interaction
        selected (bool): If True, makes button selected_color until a
                          different, linked button is pressed
        selected_color (tuple, int): Assigns color to selected button in a
                                     set of linked buttons
        selected_text_color (tuple, int): Assigns text color to selected button
                                          in a set of linked buttons
        clickable (bool): If True, button can be pressed
        unclickable_timer (int): Timer for length of unclickable duration
        unclickable_countdown (int): Counts down from unclickable_timer to 0

        Methods:
            draw: Draws button with overlaid text, listens for hover and
                  clicks, changing color on hover and calling function or
                  returning string on click. Can link to other buttons.
            set_text: Overlays text on top of button if text exists

    """
    def __init__(self, location, width=80, height=30,
                 message=None, color1=green, color2=bright_green,
                 action=None, font="Comic Sans MS", font_size=20,
                 message_color=black, linked=False):
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
        self.linked = linked
        self.selected = False
        self.selected_color = purple
        self.selected_text_color = white
        self.clickable = False
        self.unclickable_timer = 0.3 * seconds
        self.unclickable_countdown = 0.3 * seconds

    def draw(self, *args):
        """Draws the buttons and accepts hover and click input to perform tasks

        Draws button with overlaid text, listens for hover and
        clicks, changing color on hover and calling function or
        returning string on click. Can link to other buttons.

        Args:
            *args: Other Button class instances

        Returns:
            self._action (optional): Only returned if it is a string
        """
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
                    if self.linked:
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
        """Overlays text on top of button, if text exists"""
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


class Tracker:
    """Keeps track of a statistic for player and displays it on screen

    Args:
        location (tuple, int): Defines self.x, self.y
        start_stat (int): Defines self.stat
        width (int, default=120): Defines self._width
        height (int, default=30): Defines self._height
        background_color (tuple, int, default=black):
            Defines self._background_color
        font (str, default="Comic Sans MS"): Defines font-type for self._font
        font_size (int, default=20): Defines font-size for self._font
        text_color (str, default=white): Defines self.text_color
        prefix (str, default=None): Defines self.prefix
        special (str, default=None): Defines self.special

    Attributes:
        x, y (tuple, int): Coordinates for upper-left corner of stat display
        stat (int): Tracks player's stat
        _width (int): Width of background rectangle for stat display
        _height (int): Height of background rectangle for stat display
        _background_color (tuple, int): Stat display rectangle background color
        _font (obj): Font for stat display, defined by font and font_size
        text_color (tuple, int): Color of stat display text
        background (bool): If True, displays background for sta display
        prefix (str): String to display in front of stat
        special (str): Defines special tracker type for unique display

    Methods:
        draw: Draws background of stat display, calls set_text
        set_text: Writes text to stat display
        update_stat: Alters copied stat for display on screen
        adjust: Adds stat to self.stat (can use with negative number)
    """

    def __init__(self, location, start_stat, width=100, height=30,
                 background_color=black, front_color=None, font="Comic Sans MS",
                 font_size=20, text_color=white, prefix=None, special=None):

        self.x, self.y = location
        self.start_stat = start_stat
        self.stat = start_stat
        self.displayed_stat = start_stat
        self._width = width
        self._height = height
        self._background_color = background_color
        self._front_color = front_color
        self._font = pygame.font.SysFont(font, font_size)
        self.text_color = text_color
        self.background = True
        self.prefix = prefix
        self.game_over = False
        self.special = special

    def draw(self):
        """Draws background of stat display, calls set_text"""
        # If front_color defined, draw front bar as percentage of back bar
        if self._front_color and self.background:
            if self.stat > 0:
                stat_width = int(self._width * self.stat // self.start_stat)
            else:
                stat_width = 0
            pygame.draw.rect(
                gameDisplay, self._background_color,
                (self.x, self.y, self._width, self._height))
            pygame.draw.rect(
                gameDisplay, self._front_color,
                (self.x, self.y, stat_width, self._height))
        # If no background color
        elif self.background and not self._front_color:
            pygame.draw.rect(
                gameDisplay, self._background_color,
                (self.x, self.y, self._width, self._height))
        # Write text
        self.set_text()

    def set_text(self):
        """Writes text to stat display"""
        # Update how text to display
        self.update_stat()
        # Add prefix if there is one and then render text surface
        if self.prefix:
            text_surface = self._font.render(
                self.prefix + self.displayed_stat,
                True, self.text_color)
        else:
            text_surface = self._font.render(
                self.displayed_stat, True, self.text_color)
        # Get rectangle for text and center text in it
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        # Display text on screen
        gameDisplay.blit(text_surface, text_rect)

    def update_stat(self):
        """Alters copied stat for display on screen"""
        if self.special == "clock":
            minutes_elapsed = self.stat // minutes
            remaining_seconds = (self.stat % minutes) // seconds
            self.displayed_stat = \
                "Time: {0}:{1:02}".format(minutes_elapsed, remaining_seconds)
        elif self.special == "castle":
            self.displayed_stat = \
                "Castle: {}/{}".format(self.stat, self.start_stat)
            if self.stat <= 0:
                self.game_over = True
        else:
            self.displayed_stat = str(self.stat)

    def adjust(self, amount):
        """Adds stat to self.stat (can use with negative number)"""
        self.stat += amount


class EndScreen:
    """Creates an end of game screen for winning or losing game

    No Args
    
    Attributes:
        center_x (int): Gets the horizontal center of the screen
        game_y (int): Y coordinate for 'Victory' or 'Defeat'
        score_y (int): Y coordinate for end of game score
        time_y (int): Y coordinate for end of game time
        score: Players points obtained for display
        time_elapsed (int): Games frames used to approx. time
        game_font (obj): font for 'Victory/Defeat' display
        score_font (obj): font for 'score' display
        time_font (obj): font for 'time' display
        text_color (obj): color of all displays' screen text
        play_button (obj): Button for playing new game
        quit_button (obj): Button for quitting game
        main_button (obj): Button for returning to intro loop

    Methods:
        draw: Draws all message displays and buttons, calls set_text()
        set_text: Displays texts for message displays
    """
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
            (75, display_height - 320), message="Play", action="play",
            font_size=40, width=200, height=60, color1=green,
            color2=bright_green)
        self.quit_button = Button(
            (325, display_height - 320), message="Quit", action=quit,
            font_size=40, width=200, height=60, color1=red, color2=bright_red)
        self.main_button = Button(
            (575, display_height - 320), message="Main menu", action="main",
            font_size=40, width=200, height=60, color1=yellow,
            color2=bright_yellow)

    def draw(self, win_loss):
        """Draws all message displays and buttons, calls set_text()"""
        pygame.mixer.music.fadeout(750)
        if win_loss == "lose":
            pygame.mixer.music.load('music/Hero_Down.mp3')
            pygame.mixer.music.play(-1, start=1.5)
        if win_loss == "win":
            pygame.mixer.music.load('music/Amazing_Plan_Silent_Film_Dark.mp3')
            pygame.mixer.music.play(-1)
        # Define time for display
        minutes_elapsed = self.time_elapsed // minutes
        remaining_seconds = (self.time_elapsed % minutes) // seconds

        while True:
            # Check for quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # Show background
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
        """Displays texts for message displays"""
        text_surface = font.render(message, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)


class Settings:
    """Stores settings for game difficulty
    
    Attributes:
        spawn_rate (int): Rate of enemy spawning
        starting_gold (int): Money available at start of game
        gold_generation (int): Rate at which money is passively generated
        difficulty (int): Affects how quickly enemy difficulty ramps (default=1)
    """
    def __init__(self):
        self.spawn_rate = 6 * seconds
        self.starting_gold = 1200
        self.gold_generation = 1 * seconds
        self.difficulty = 1
