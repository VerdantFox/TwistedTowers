import pygame
from colors import *

# Hard-coding in parameters for our game until better plan devised
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))


# https://stackoverflow.com/questions/28005641
# /how-to-add-a-background-image-into-pygame
class Background(pygame.sprite.Sprite):
    """Creates background as image_image file"""

    def __init__(self, image_file, location=(0, 0)):
        pygame.sprite.Sprite.__init__(self)  # Call Sprite initializer
        # Suppress Error
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Button:
    def __init__(self, x_coord, y_coord, width=100, height=50, message=None,
                 inactive_color=green, active_color=bright_green, action=None,
                 font="Calibri", font_size=20, message_color=black):
        self._mouse = None
        self._click = None
        self._message = message
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._width = width
        self._height = height
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._action = action
        self._font = pygame.font.SysFont(font, font_size)
        self._message_color = message_color

    def draw(self):
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        if (self._x_coord < self._mouse[0] < self._x_coord + self._width
                and self._y_coord <
                self._mouse[1] <
                self._y_coord + self._height):
            pygame.draw.rect(
                gameDisplay, self._active_color,
                (self._x_coord, self._y_coord, self._width, self._height))
            if self._click[0] == 1 and self._action is not None:
                self._action()
        else:
            pygame.draw.rect(
                gameDisplay, self._inactive_color,
                (self._x_coord, self._y_coord, self._width, self._height))
        if self._message:
            self.set_text()

    def set_text(self):
        text_surface = self._font.render(
            self._message, True, self._message_color)
        text_rect = text_surface.get_rect()
        text_rect.center = ((self._x_coord + self._width / 2),
                            (self._y_coord + self._height / 2))
        gameDisplay.blit(text_surface, text_rect)


class TowerButton(Button):
    def __init__(self, x_coord, y_coord, radius, inactive_color=brown,
                 active_color=orange, action=None):
        self._radius = radius
        self._mouse = None
        self._click = None
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._action = action

    def draw(self):
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        if (self._x_coord - self._radius
                < self._mouse[0]
                < self._x_coord + self._radius
                and self._y_coord - self._radius
                < self._mouse[1]
                < self._y_coord + self._radius):
            pygame.draw.circle(
                gameDisplay, self._active_color,
                (self._x_coord, self._y_coord), self._radius)
            if self._click[0] == 1 and self._action is not None:
                self._action()
        else:
            pygame.draw.circle(
                gameDisplay, self._inactive_color,
                (self._x_coord, self._y_coord), self._radius)

