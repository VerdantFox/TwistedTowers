import pygame
from colors import *

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
                 inactive_color=light_brown, active_color=orange, action=None,
                 font="Comic Sans MS", font_size=20, message_color=black,
                 upgrade_count=0, options_available=True):
        super().__init__()
        self._message = message
        self._radius = radius
        self._mouse = None
        self._click = None
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._inactive_color = inactive_color
        self._active_color = active_color
        self._action = action
        self._font = pygame.font.SysFont(font, font_size)
        self._message_color = message_color
        self.upgrade = False
        self.upgrade_count = upgrade_count
        self.options_available = options_available
        self.options_timer = 0

    def draw(self, is_main=True, tower_option=None, upgrade_color=blue):
        # Get mouse position and listen for left-clicks
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        #
        if self.upgrade is False:

            # If hovering over a circle
            if (self._x_coord - self._radius
                    < self._mouse[0]
                    < self._x_coord + self._radius
                    and self._y_coord - self._radius
                    < self._mouse[1]
                    < self._y_coord + self._radius):

                # If hovering tower itself, not tower options
                if is_main:
                    pygame.draw.circle(
                        gameDisplay, self._active_color,
                        (self._x_coord, self._y_coord), self._radius)
                    if self.options_available:
                        self.options_timer = 300
                    if self._click[0] == 1 and self._action is not None:
                        self._action()

                # If hovering over tower options
                else:
                    pygame.draw.circle(
                        gameDisplay, upgrade_color,
                        (self._x_coord, self._y_coord + int(1.5 * self._radius)),
                        int(self._radius * 0.75))
                    if self._click[0] == 1:
                        # upgrade_tower(tower_option) #TODO
                        pass
            # If not hovering circle, draw inactive circle
            else:
                pygame.draw.circle(
                    gameDisplay, self._inactive_color,
                    (self._x_coord, self._y_coord), self._radius)
        # Call option menu
        if self.options_available and is_main:
            self.options_menu()
        if self._message:
            self.set_text()

    def set_text(self):
        text_surface = self._font.render(
            self._message, True, self._message_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self._x_coord, self._y_coord)
        gameDisplay.blit(text_surface, text_rect)

    def options_menu(self):
        if self.options_timer > 0:
            print(self.options_timer)
            self.draw(is_main=False)
            self.options_timer -= 1


class BasicTower(TowerButton):
    def __init__(self, x_coord, y_coord, **kwargs):
        super().__init__(x_coord, y_coord, **kwargs)
