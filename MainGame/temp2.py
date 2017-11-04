# class GameScore:
#     """Keeps track of game's score and displays it on screen (if drawn).
#
#     Args:
#         location (tuple, int): Defines self.x, self.y
#         width (int, default=120): Defines self._width
#         height (int, default=30): Defines self._height
#         background_color (int, default=green): Defines self._background_color
#         font (str, default="Comic Sans MS"): Defines font for self._font
#         font_size (int, default=20): Defines font size for self._font
#         text_color (tuple, int, default=black): Defines self._text_color
#
#     Attributes:
#         x, y (tuple, int): Defines location of upper left corner of scoreboard
#         score (int): Keeps track of the players score, displayed on scoreboard
#         _width (int): Width of scoreboard
#         _height (int): Height of scoreboard
#         _background_color (tuple, int): color of scoreboard
#         _font (object): Font for scoreboard, defined by args font, font_size
#         text_color (tuple, int): color of the scoreboard's text
#         background (bool): If True, shows colored background of the scoreboard
#
#     Methods:
#         draw: Draws the scoreboard background, calls set_text()
#         set_text: Writes text (the player's score) to the scoreboard
#         adjust: Adds points to the player's score
#     """
#
#     def __init__(self, location, width=120, height=30, background_color=green,
#                  font="Comic Sans MS", font_size=20, text_color=black):
#         self.x, self.y = location
#         self.score = 0
#         self._width = width
#         self._height = height
#         self._background_color = background_color
#         self._font = pygame.font.SysFont(font, font_size)
#         self.text_color = text_color
#         self.background = True
#
#     def draw(self):
#         """Draws the scoreboard background, calls set_text()"""
#         if self.background:
#             pygame.draw.rect(
#                 gameDisplay, self._background_color,
#                 (self.x, self.y, self._width, self._height))
#         self.set_text()
#
#     def set_text(self):
#         """Writes text (the player's score) to the scoreboard"""
#         text_surface = self._font.render(
#             "Score: " + str(self.score), True, self.text_color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = ((self.x + self._width // 2),
#                             (self.y + self._height // 2))
#         gameDisplay.blit(text_surface, text_rect)
#
#     def adjust(self, amount):
#         """Adds points to the player's score"""
#         self.score += amount
#
#
# class GameClock:
#     """Keeps track of game time (defined by game frames) and displays time
#
#     Args:
#         location (tuple, int): Defines self.x, self.y
#         width (int, default=120): Defines self._width
#         height (int, default=30): Defines self._height
#         background_color (tuple, int, default=black):
#             Defines self._background_color
#         font (str, default="Comic Sans MS"): Defines font-type for self._font
#         font_size (int, default=20): Defines font size for self._font
#         text_color (tuple, int, default=white): Defines self._text_color
#
#     Attributes:
#         x, y (tuple, int): Coordinates for upper-left corner of game clock
#         frames (int): number of frames passed since game start (defines time)
#         _width (int): Width of game clock background
#         _height (int): Height pf game clock background
#         _background_color (tuple, int): Color of game clock background
#         _font (object): Font of game clock, defined with font and font_size
#         _text_color (tuple, int): Color of game clock text
#         background (bool): If True, rectangle for game clock background shown
#
#     Methods:
#         draw: Draws the background of the game clock, calls set_text
#         set_text: Writes the game clock, calculated by self.frames
#     """
#
#     def __init__(self, location, width=120, height=30, background_color=black,
#                  font="Comic Sans MS", font_size=20, text_color=white):
#         self.x, self.y = location
#         self.frames = 0
#         self._width = width
#         self._height = height
#         self._background_color = background_color
#         self._font = pygame.font.SysFont(font, font_size)
#         self._text_color = text_color
#         self.background = True
#
#     def draw(self):
#         """Draws the background of the game clock, calls set_text"""
#         if self.background:
#             pygame.draw.rect(
#                 gameDisplay, self._background_color,
#                 (self.x, self.y, self._width, self._height))
#         self.set_text()
#         self.frames += 1
#
#     def set_text(self):
#         """Writes the game clock, calculated by self.frames"""
#         minutes_elapsed = self.frames // minutes
#         remaining_seconds = (self.frames % minutes) // seconds
#         text_surface = self._font.render(
#             "Time: {0}:{1:02}".format(minutes_elapsed, remaining_seconds),
#             True, self._text_color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = ((self.x + self._width // 2),
#                             (self.y + self._height // 2))
#         gameDisplay.blit(text_surface, text_rect)
#
#
# class Money:
#     """Keeps track of player's money and shows it on screen
#
#     Args:
#         location (tuple, int): Defines self.x, self.y
#         width (int, default=120): Defines self._width
#         height (int, default=30): Defines self._height
#         start_cash (int, default=1200): Defines self.stat
#         background_color (tuple, int, default=black):
#             Defines self._background_color
#         font (str, default="Comic Sans MS"): Defines font-type for self._font
#         font_size (int, default=20): Defines font-size for self._font
#         text_color (str, default=white): Defines self.text_color
#
#     Attributes:
#         x, y (tuple, int): Coordinates for upper-left corner of money display
#         cash (int): Tracks player's available money for spending
#         _width (int): Width of background rectangle for money display
#         _height (int): Height of background rectangle for money display
#         _background_color (tuple, int): Money display rectangle background color
#         _font (object): Font for money display, defined by font and font_size
#         text_color (tuple, int): Color of money display text
#         background (bool): If True, displays background for money display
#
#     Methods:
#         draw: Draws background of money display, calls set_text
#         set_text: Writes text to money display
#         adjust: Adds stat to self.stat (can use with negative number)
#     """
#
#     def __init__(self, location, width=100, height=30, start_cash=1200,
#                  background_color=black, font="Comic Sans MS", font_size=20,
#                  text_color=white):
#         self.x, self.y = location
#         self.cash = start_cash
#         self._width = width
#         self._height = height
#         self._background_color = background_color
#         self._font = pygame.font.SysFont(font, font_size)
#         self.text_color = text_color
#         self.background = True
#
#     def draw(self):
#         if self.background:
#             pygame.draw.rect(
#                 gameDisplay, self._background_color,
#                 (self.x, self.y, self._width, self._height))
#         self.set_text()
#
#     def set_text(self):
#         text_surface = self._font.render(
#             "$" + str(self.cash), True, self.text_color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = ((self.x + self._width // 2),
#                             (self.y + self._height // 2))
#         gameDisplay.blit(text_surface, text_rect)
#
#     def adjust(self, amount):
#         self.cash += amount
#
#
# class Castle:
#     def __init__(self, health_location, width=250, height=50, max_health=10,
#                  back_color=red, front_color=green, font="Comic Sans MS",
#                  font_size=30, message_color=white):
#         self.x, self.y = health_location
#         self.max_hp = max_health
#         self.hp = max_health
#         self._width = width
#         self._height = height
#         self._back_color = back_color
#         self._front_color = front_color
#         self._font = pygame.font.SysFont(font, font_size)
#         self.text_color = message_color
#         self.background = True
#         self.game_over = False
#
#     def adjust(self, amount):
#         self.hp += amount
#
#     def draw(self):
#         if self.background:
#             if self.hp > 0:
#                 damage_width = int(self._width * self.hp // self.max_hp)
#             else:
#                 damage_width = 0
#
#             pygame.draw.rect(
#                 gameDisplay, self._back_color,
#                 (self.x, self.y, self._width, self._height))
#             pygame.draw.rect(
#                 gameDisplay, self._front_color,
#                 (self.x, self.y, damage_width, self._height))
#
#     def draw(self):
#         if self.background:
#             if self.stat > 0:
#                 damage_width = int(self._width * self.hp // self.max_hp)
#             else:
#                 damage_width = 0
#
#             pygame.draw.rect(
#                 gameDisplay, self._back_color,
#                 (self.x, self.y, self._width, self._height))
#             pygame.draw.rect(
#                 gameDisplay, self._front_color,
#                 (self.x, self.y, damage_width, self._height))
#
#         self.set_text()
#
#         if self.hp <= 0:
#             self.game_over = True
#
#     def set_text(self):
#         text_surface = self._font.render(
#             "Castle: {}/{}".format(self.hp, self.max_hp),
#             True, self.text_color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = ((self.x + self._width // 2),
#                             (self.y + self._height // 2))
#         gameDisplay.blit(text_surface, text_rect)
#
#
# class Tracker:
#     """Keeps track of a statistic for player and displays it on screen
#
#     Args:
#         location (tuple, int): Defines self.x, self.y
#         width (int, default=120): Defines self._width
#         height (int, default=30): Defines self._height
#         start_cash (int, default=1200): Defines self.stat
#         background_color (tuple, int, default=black):
#             Defines self._background_color
#         font (str, default="Comic Sans MS"): Defines font-type for self._font
#         font_size (int, default=20): Defines font-size for self._font
#         text_color (str, default=white): Defines self.text_color
#
#     Attributes:
#         x, y (tuple, int): Coordinates for upper-left corner of money display
#         cash (int): Tracks player's available money for spending
#         _width (int): Width of background rectangle for money display
#         _height (int): Height of background rectangle for money display
#         _background_color (tuple, int): Money display rectangle background color
#         _font (object): Font for money display, defined by font and font_size
#         text_color (tuple, int): Color of money display text
#         background (bool): If True, displays background for money display
#
#     Methods:
#         draw: Draws background of money display, calls set_text
#         set_text: Writes text to money display
#         adjust: Adds stat to self.stat (can use with negative number)
#     """
#
#     def __init__(self, location, width=100, height=30, start_cash=1200,
#                  background_color=black, font="Comic Sans MS", font_size=20,
#                  text_color=white):
#         self.x, self.y = location
#         self.cash = start_cash
#         self._width = width
#         self._height = height
#         self._background_color = background_color
#         self._font = pygame.font.SysFont(font, font_size)
#         self.text_color = text_color
#         self.background = True
#
#     def draw(self):
#         if self.background:
#             pygame.draw.rect(
#                 gameDisplay, self._background_color,
#                 (self.x, self.y, self._width, self._height))
#         self.set_text()
#
#     def set_text(self):
#         text_surface = self._font.render(
#             "$" + str(self.cash), True, self.text_color)
#         text_rect = text_surface.get_rect()
#         text_rect.center = ((self.x + self._width // 2),
#                             (self.y + self._height // 2))
#         gameDisplay.blit(text_surface, text_rect)
#
#     def adjust(self, amount):
#         self.cash += amount