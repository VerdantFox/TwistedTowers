import pygame
from colors import *
from lists import *

# Hard-coding in parameters for our game until better plan devised
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))


class TowerButton(pygame.sprite.Sprite):
    """Base class for tower buttons (circular buttons)

    required inits: x_coord, y_coord (positions center of tower circle)
    radius:         radius of tower, defaults to 24 pixels
    message:        message to display on tower (optional)
    inactive_color: color without mouse hover (default light_brown)
    active_color:   color on mouse hover (default orange)
    font:           font for optional button message, default 'Comic Sans MS'
    font_size:      font size of optional message, defaults to 20
    message_color:  text color of optional message, defaults to black
    """
    def __init__(self, x_coord, y_coord, radius=24, message=None,
                 inactive_color=light_brown, active_color=orange,
                 font="Comic Sans MS", font_size=20, message_color=black,
                 upgrade_count=0, option1_no_hover=yellow,
                 option1_hover=bright_yellow, option2_no_hover=blue,
                 option2_hover=bright_blue, option3_no_hover=red,
                 option3_hover=bright_red, option4_no_hover=green,
                 option4_hover=bright_green, option1_message=None,
                 option2_message=None, option3_message=None,
                 option4_message=None):
        super().__init__()
        self._message = message
        self._radius = radius
        self._mouse = None
        self._click = None
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._font = pygame.font.SysFont(font, font_size)
        self._message_color = message_color
        self.destroyed = False
        self.upgrade_count = upgrade_count
        self.options_timer = 0
        self.option_hover_list = \
            [(option1_no_hover, option1_hover, option1_message),
             (option2_no_hover, option2_hover, option2_message),
             (option3_no_hover, option3_hover, option3_message),
             (option4_no_hover, option4_hover, option4_message)]

    def draw_main(self):
        # Get mouse position and listen for left-clicks
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()

        if self.destroyed is False:
            # If hovering over main circle draw circle give click opti
            if (self._x_coord - self._radius
                    < self._mouse[0]
                    < self._x_coord + self._radius
                    and self._y_coord - self._radius
                    < self._mouse[1]
                    < self._y_coord + self._radius):
                pygame.draw.circle(
                    gameDisplay, self._active_color,
                    (self._x_coord, self._y_coord), self._radius)
                # Set timer for options to be visible
                if self._click[0] == 1:
                    self.options_timer = 45
            # If not hovering circle, draw inactive circle
            else:
                pygame.draw.circle(
                    gameDisplay, self._inactive_color,
                    (self._x_coord, self._y_coord), self._radius)
        # Call option menu
        self.options_menu()
        # Bring up message (optional)
        if self._message:
            self.set_text(self._x_coord, self._y_coord, self._message)

    def draw_options(self):
        # Already listening for mouse + clicks from draw_main

        if self.destroyed is False:
            # redefine coordinates and radius for new option's circle
            for loc in circles:
                option_number, x_multiplier, y_multiplier = \
                    circles[circles.index(loc)]
                no_hover_color, hover_color, option_message = \
                    self.option_hover_list[option_number-1]
                x = self._x_coord + int(x_multiplier * self._radius)
                y = self._y_coord + int(y_multiplier * self._radius)
                radius = int(self._radius * 0.7)

                # If hovering over a circle (needs fix for each options circle)

                if (x - radius < self._mouse[0] < x + radius
                        and y - radius < self._mouse[1] < y + radius):
                    pygame.draw.circle(gameDisplay, hover_color, (x, y), radius)
                    self.options_timer = 30
                    if self._click[0] == 1:
                        # upgrade_tower(tower_option) #TODO
                        pass
                # If not hovering circle, draw inactive circle
                else:
                    pygame.draw.circle(
                        gameDisplay, no_hover_color,
                        (x, y),
                        radius)
                if option_message:
                    self.set_text(x, y, option_message)

    def set_text(self, x, y, message):
        text_surface = self._font.render(
            message, True, self._message_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)

    def options_menu(self):
        if self.options_timer > 0:
            self.draw_options()
            self.options_timer -= 1


class BasicTower(TowerButton):
    def __init__(self, x_coord, y_coord, **kwargs):
        super().__init__(x_coord, y_coord, **kwargs)
