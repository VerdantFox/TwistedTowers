import pygame
from colors import *

# Hard-coding in parameters for our game until better plan devised
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))


# https://stackoverflow.com/questions/28005641
# /how-to-add-a-background-image-into-pygame
class Background:
    """Creates background as image_image file"""
    def __init__(self, image_file, location=(0, 0)):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class RectButton:
    """Class for rectangular buttons

    Attributes:


    """
    def __init__(self, location, width=80, height=30,
                 message=None, inactive_color=green, active_color=bright_green,
                 action=None, font="Comic Sans MS", font_size=20,
                 message_color=black):
        self._mouse = None
        self._click = None
        self._message = message
        self.x, self.y = location
        self._width = width
        self._height = height
        self._color1 = inactive_color
        self._color2 = active_color
        self._action = action
        self._font = pygame.font.SysFont(font, font_size)
        self._message_color = message_color

    def draw(self):
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        if (self.x < self._mouse[0] < self.x + self._width
                and self.y <
                self._mouse[1] <
                self.y + self._height):
            pygame.draw.rect(
                gameDisplay, self._color2,
                (self.x, self.y, self._width, self._height))
            if self._click[0] == 1 and self._action is not None:
                self._action()
        else:
            pygame.draw.rect(
                gameDisplay, self._color1,
                (self.x, self.y, self._width, self._height))
        if self._message:
            self.set_text()

    def set_text(self):
        text_surface = self._font.render(
            self._message, True, self._message_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.x + self._width // 2),
                            (self.y + self._height // 2))
        gameDisplay.blit(text_surface, text_rect)


class GameScore:
    def __init__(self, location, width=90, height=30, background_color=green,
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


class Money:
    def __init__(self, location, width=90, height=30, start_cash=400,
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

