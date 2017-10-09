import pygame
from colors import *

# Hard-coding in parameters for our game until better plan devised
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))


class TowerButton(pygame.sprite.Sprite):
    """Base class for tower buttons (circular buttons)

    x, y:           (Required) positions center of tower circle
    radius:         radius of tower, defaults to 24 pixels
    message:        message to display on tower (optional)
    inactive_color: color without mouse hover (default light_brown)
    active_color:   color on mouse hover (default orange)
    font:           font for optional button message, default 'Comic Sans MS'
    font_size:      font size of optional message, defaults to 20
    message_color:  text color of optional message, defaults to black
    """
    def __init__(
            self, x, y, radius=24, main_msg=None,
            main_color1=light_brown, main_color2=orange,
            font="Comic Sans MS", font_size=20, message_color=black,
            upgrade_count=0, opt1_col1=yellow,
            opt1_col2=bright_yellow, opt2_col1=blue,
            opt2_col2=bright_blue, opt3_col1=red,
            opt3_col2=bright_red, opt4_col1=green,
            opt4_col2=bright_green, opt5_col1=purple,
            opt5_col2=bright_purple, opt1_msg="Sell", opt2_msg=None,
            opt3_msg=None, opt4_msg=None, opt5_msg=None, opt1_msg_col=black,
            opt2_msg_col=black, opt3_msg_col=black, opt4_msg_col=black,
            opt5_msg_col=black):
        super().__init__()
        self._radius = radius
        self._mouse = None
        self._click = None
        self._x = x
        self._y = y
        self._font = font
        self._font_size = font_size
        self.destroyed = False
        self._options_timer = 0
        # List == x_offset, y_offset, no_hover_color, hover_color, msg, msg_col
        self.circle_list = [
            [0, 0, main_color1, main_color2, main_msg, message_color]]
        self.upgrade_list = [
            [-0.6, 2.3, opt1_col1, opt1_col2, opt1_msg, opt1_msg_col],
            [1.3, 1.9, opt2_col1, opt2_col2, opt2_msg, opt2_msg_col],
            [2.2, 0.25, opt3_col1, opt3_col2, opt3_msg, opt3_msg_col],
            [1.7, -1.6, opt4_col1, opt4_col2, opt4_msg, opt4_msg_col],
            [-0.1, -2.2, opt5_col1, opt5_col2, opt5_msg, opt5_msg_col]]
        for upgrade in self.upgrade_list:
            if self.upgrade_list.index(upgrade) == upgrade_count:
                break
            else:
                self.circle_list.append(upgrade)

    def draw(self):
        # Parameter for killing tower (destroyed if replaced or sold)
        if self.destroyed is True:
            return None

        # Get mouse position and listen for left-clicks
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()

        # List == x_offset, y_offset, no_hover_color,
        #         hover_color, message, message_color
        # define relevant variables
        for circle in self.circle_list:
            circle_number = self.circle_list.index(circle)
            x_offset, y_offset, no_hov_color, hov_color, msg, msg_col = circle
            if circle_number == 0:
                radius = self._radius
            else:
                radius = int(self._radius * 0.7)
            x = int(self._x + x_offset * radius)
            y = int(self._y + y_offset * radius)

            # If hovering over a circle (needs fix for each options circle)
            if (x - radius < self._mouse[0] < x + radius
                    and y - radius < self._mouse[1] < y + radius):
                if circle_number == 0 or self._options_timer > 0:
                    pygame.draw.circle(gameDisplay, hov_color, (x, y), radius)
                    if circle_number > 0:
                        self._options_timer = 30
                    if self._click[0] == 1:
                        if circle_number == 0:
                            self._options_timer = 45
                    else:
                        # upgrade_tower or sell (option) #TODO
                        pass
            # If not hovering circle, draw inactive circle if possible
            else:
                if circle_number == 0 or self._options_timer > 0:
                    pygame.draw.circle(
                        gameDisplay, no_hov_color, (x, y), radius)
            if msg and (circle_number == 0 or self._options_timer > 0):
                if circle_number == 0:
                    self.set_text(x, y, msg, msg_col, True)
                else:
                    self.set_text(x, y, msg, msg_col, False)
        if self._options_timer > 0:
            self._options_timer -= 1

    def set_text(self, x, y, msg, msg_color, is_main):
        if is_main:
            font = pygame.font.SysFont(self._font, self._font_size, bold=True)
        else:
            font = pygame.font.SysFont(
                self._font, int(self._font_size * .7), bold=True)
        text_surface = font.render(msg, True, msg_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)


class BasicTower(TowerButton):
    def __init__(self, x, y, **kwargs):
        super().__init__(x, y, **kwargs)
