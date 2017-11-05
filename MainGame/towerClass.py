import pygame

import helpers
from definitions import *
from gameParameters import gameDisplay
from towers.towerPics import basicTower1, iceTower1, iceTower2, fireTower1, \
    fireTower2, poisonTower1, poisonTower2, darkTower1, darkTower2, \
    hammer_list, wood
from sounds import tower_shoot_sound, basic_hit_sound, ice_hit_sound, \
    fire_hit_sound, poison_hit_sound, dark_hit_sound


class TowerButton:
    """Base class for tower buttons (circular buttons)
    

    Define a button with x, y coordinates specified. Draws button options for
    selling or buying other towers. Calls functions for drawing tower with
    associated option buttons, constructing new tower, selling current tower.

    Args:
        location (tuple, int): Defines self.x, self.y
        destroy (bool, default=False): Defines self.destroy
        main_msg (str, default=None): Helps define self.circle_list
        set_options_timer (int, default=30): Defines self.set_options_timer
        main_color1 (tuple, int, default=light_brown): Helps define 
                                                       self.circle_list
        main_color2 (tuple, int, default=orange): Helps define self.circle_list 
        font (str, default="Comic Sans MS"): Defines self._font
        font_size (int, default=20): Defines self._font_size
        message_color (tuple, int, default=black): Helps define self.circle_list
        option_count (int, default=1): Defines self.option_count
        opt1_col1 (tuple, int, default=yellow): Helps define self.options_list 
        opt1_col2 (tuple, int, default=bright_yellow ): Helps define 
                                                         self.options_list
        opt2_col1 (tuple, int, default=teal): Helps define 
                                               self.options_list
        opt2_col2 (tuple, int, default=bright_teal): Helps define 
                                                      self.options_list
        opt3_col1 (tuple, int, default=red): Helps define self.options_list
        opt3_col2 (tuple, int, default=bright_red): Helps define 
                                                     self.options_list 
        opt4_col1 (tuple, int, default=green): Helps define self.options_list
        opt4_col2 (tuple, int, default=bright_green): Helps define 
                                                       self.options_list 
        opt5_col1 (tuple, int, default=purple): Helps define self.options_list
        opt5_col2 (tuple, int, default=bright_purple): Helps define 
                                                        self.options_list 
        opt1_msg (str, default="Basic"): Helps define self.options_list
        opt2_msg (str, default=None): Helps define self.options_list
        opt3_msg (str, default=None): Helps define self.options_list
        opt4_msg (str, default=None): Helps define self.options_list
        opt5_msg (str, default=None): Helps define self.options_list
        opt1_msg_col (tuple, int, default=black): Helps define self.options_list
        opt2_msg_col (tuple, int, default=black): Helps define self.options_list
        opt3_msg_col (tuple, int, default=black): Helps define self.options_list
        opt4_msg_col (tuple, int, default=black): Helps define self.options_list
        opt5_msg_col (tuple, int, default=black): Helps define self.options_list
        opt1_action (str, default="basic"): Helps define self.options_list
        opt2_action (str, default=None): Helps define self.options_list
        opt3_action (str, default=None): Helps define self.options_list
        opt4_action (str, default=None): Helps define self.options_list
        opt5_action (str, default=None): Helps define self.options_list
    
    Attributes:
        construct_image: Hammer image shown during construct()
        construct_width: Hammer image width
        construct_height: Hammer image height

        # Construction
        constructing (bool): When True, game_loop will call construct()
        construct_timer (int): Time for duration of tower construction
        construct_countdown (int): Counts down from construct_timer to 0
        frame_counter (int): Counts game frames until image frame swap
        frame (int): The frame (image) index of the hammer currently shown
        frames_to_picswap (int): Game frames to count down until image change
        destroy (bool): If True, game_loop won't draw() tower

        # Selling
        selling (bool): If True, game_loop will call sell()
        sell_timer (int): Duration in game frames sell() will be called
        sell_countdown (int): Counts down from sell_timer to 0
        sell_font (obj): Font of sale shown while sell() is called
        previous_sell_value (int): Taken from tower being sold in game_loop,
                                   this is the sale towers .sell value
        tier (int): The level of the tower (from 0 to 3)

        # Map visuals
        image (obj): Image of tower
        _button_radius (int): Radius of main tower button
        x, y (tuple, int): Coordinates for tower's location (circle's center)
        
        # Event detection
        _mouse (tuple, int): The coordinates where user's mouse is hovering
        _click (tuple int): Detection of user's mouse clicks
                            (left, center, right)
        
        # Text
        _font (str): Font used for buttons
        _font_size (int): Font size used for buttons (adjusts automatically
                          for options buttons)
        
        # Options
        option_selected (str): The option for whichever circle_option is hovered
        set_options_timer (int): The duration options will show after stopping
                                 their hover before options will disappear
        _options_countdown (int): Counts down from set_options_timer to 0
        option_count (int): The number of options circles to display
        option_lockout (bool): If True, options cannot be selected
        gray_out (bool): If True, options color turn gray
        
        # List = x_offset, y_offset, no_hover_color, hover_color, msg, msg_col
        # Circle list index 0 refers to main circle (tower location)
        self.circle_list (list of lists):
            One list per option. Within each option's list are [x-coordinate
            relative offset (int), y-coordinate relative offset (int),
            color of button not highlighted (tuple, int), color of
            button highlighted (tuple, int), button's text (str),
            text's color (tuple, int), the action associated with
            that button (str)]
        self.options_list:
            Same as circle list, used to append only the options used,
            listed by option_count, to the circle list.
        
    Methods:
        construct: Show's tower building animation, un-destroys tower
        construction_bar: Show's animation of construction duration
        sell: Shows money earned from tower sale, un-destroys tower
        draw: Draws tower, associated buttons, and acts on buttons
        gray_options (static): Returns True for grayed-out options
        show_tower_image: Shows the tower image
        set_text: Draw text inside of option circle if specified
    """
    def __init__(
            self, location, destroy=False,
            main_msg=None, set_options_timer=30, main_color1=light_brown,
            main_color2=orange, font="Comic Sans MS", font_size=20,
            message_color=black, option_count=1, opt1_col1=yellow,
            opt1_col2=bright_yellow, opt2_col1=teal,
            opt2_col2=bright_teal, opt3_col1=red,
            opt3_col2=bright_red, opt4_col1=green,
            opt4_col2=bright_green, opt5_col1=purple,
            opt5_col2=bright_purple, opt1_msg="Basic", opt2_msg=None,
            opt3_msg=None, opt4_msg=None, opt5_msg=None, opt1_msg_col=black,
            opt2_msg_col=black, opt3_msg_col=black, opt4_msg_col=black,
            opt5_msg_col=black, opt1_action="basic", opt2_action=None,
            opt3_action=None, opt4_action=None, opt5_action=None):
        
        self.construct_image, self.construct_width, self.construct_height = \
            hammer_list[0]

        # Construction
        self.constructing = False
        self.construct_timer = 1.5 * seconds
        self.construct_countdown = self.construct_timer
        self.frame_counter = 0
        self.frame = 0
        self.frames_to_picswap = 1
        self.destroy = destroy

        # Selling
        self.selling = False
        self.sell_timer = 0.5 * seconds
        self.sell_countdown = self.sell_timer
        self.sell_font = pygame.font.SysFont(
            font, 20, bold=True)
        self.previous_sell_value = None
        self.tier = 0

        # Map visuals
        self.image = None
        self._button_radius = 24
        self.x, self.y = location
        
        # Event detection
        self._mouse = None
        self._click = None
        
        # Text
        self._font = font
        self._font_size = font_size
        
        # Options
        self.option_selected = None
        self.set_options_timer = set_options_timer
        self._options_countdown = 0
        self.option_count = option_count
        self.option_lockout = False
        self.gray_out = False
        
        # List == x_offset, y_offset, no_hover_color, hover_color, msg, msg_col
        # Circle list index 0 refers to main circle (tower location)
        self.circle_list = [
            [0, 0, main_color1, main_color2, main_msg, message_color, None]]
        # Option list specifies circles (options) to tower location
        self.options_list = [
            [-0.6, 2.3, opt1_col1, opt1_col2,
             opt1_msg, opt1_msg_col, opt1_action],
            [1.3, 1.9, opt2_col1, opt2_col2,
             opt2_msg, opt2_msg_col, opt2_action],
            [2.2, 0.25, opt3_col1, opt3_col2,
             opt3_msg, opt3_msg_col, opt3_action],
            [1.7, -1.6, opt4_col1, opt4_col2,
             opt4_msg, opt4_msg_col, opt4_action],
            [-0.1, -2.2, opt5_col1, opt5_col2,
             opt5_msg, opt5_msg_col, opt5_action]]
        # Append to circle_list as many options as specified by option_count
        for option in self.options_list:
            if self.options_list.index(option) == self.option_count:
                break
            else:
                self.circle_list.append(option)

    def construct(self):
        """Show's tower building animation, un-destroys tower"""
        # Count down construction duration (in game frames)
        if self.construct_countdown > 0:
            self.construct_countdown -= 1
            # Count down duration (in game frames) on current image of hammer
            if self.frame_counter > 0:
                self.frame_counter -= 1
            # Switch to next hammer image
            else:
                self.construct_image = hammer_list[self.frame][0]
                self.frame += 1
                if self.frame > len(hammer_list) - 1:
                    self.frame = 0
                self.frame_counter = self.frames_to_picswap
            # Show wooden plank
            gameDisplay.blit(
                wood[0],
                (int(self.x - 0.5 * self.construct_width),
                 int(self.y - .8 * self.construct_height)))
            # Show hammer image
            gameDisplay.blit(
                self.construct_image,
                (int(self.x - 0.3 * self.construct_width),
                 int(self.y - 1 * self.construct_height)))
            # Call (show) construction_bar()
            self.construction_bar()
        # Un-destroy tower and stop construction
        else:
            self.destroy = False
            self.constructing = False

    def construction_bar(self):
        """Show's animation of construction duration"""
        # Define maximum width of construction bar (back bar width)
        max_width = self.construct_width // 2
        if self.construct_countdown >= 0:
            # Define current width of construction bar (front bar width)
            construct_width = int(max_width
                                  * (self.construct_timer
                                     - self.construct_countdown)
                                  // self.construct_timer)
        else:
            construct_width = 0
        # Define height and colors of construction bars
        height = 4
        back_color = white
        front_color = bright_orange
        # Define x, y coordinates of construction bar relative to tower location
        x = self.x - self.construct_width // 4
        y = self.y - self.construct_height * 1 // 4
        # Draw back, then front construction bars
        pygame.draw.rect(gameDisplay, back_color,
                         (x, y, max_width, height))
        if construct_width:
            pygame.draw.rect(gameDisplay, front_color,
                             (x, y, construct_width, height))
    
    def sell(self):
        """Shows money earned from tower sale, un-destroys tower"""
        # Counts down time of sale (from game frames)
        if self.sell_countdown > 0:
            self.sell_countdown -= 1
            # Define and display sale text
            text_surface = self.sell_font.render(
                '$' + str(self.previous_sell_value), True, black)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.x, self.y)
            gameDisplay.blit(text_surface, text_rect)
        # When sale ends, un-destroy tower and stop selling
        else:
            self.destroy = False
            self.selling = False

    def draw(self):
        """Draws tower, associated buttons, and acts on buttons"""
        # Count down options
        if self._options_countdown > 0:
            self._options_countdown -= 1
        # Get mouse position and click information
        self._mouse = pygame.mouse.get_pos()
        self._click = pygame.mouse.get_pressed()
        # define relevant variables
        for circle in self.circle_list:
            circle_number = self.circle_list.index(circle)
            x_offset, y_offset, no_hov_color, hov_color, \
                msg, msg_col, action = circle
            if circle_number == 0:
                radius = self._button_radius
            else:
                radius = int(self._button_radius * 0.7)
                if self.option_lockout:
                    action = None
                if self.gray_out:
                    gray_out = self.gray_options(circle_number)
                    if gray_out is True:
                        no_hov_color = gray
                        hov_color = gray
            x = int(self.x + x_offset * radius)
            y = int(self.y + y_offset * radius)
            
            # If hovering over a circle
            if (x - radius < self._mouse[0] < x + radius
                    and y - radius < self._mouse[1] < y + radius):
                # Display main circle or hovered option circle (highlight color)
                if circle_number == 0 or self._options_countdown > 0:
                    pygame.draw.circle(gameDisplay, hov_color, (x, y), radius)
                    # Call show_tower_image()
                    if circle_number == 0:
                        self.show_tower_image()
                    # Start countdown for stop showing options
                    if circle_number > 0:
                        self._options_countdown = self.set_options_timer
                    # If left clicked
                    if self._click[0] == 1:
                        # If main circle show options
                        if circle_number == 0:
                            self._options_countdown = int(
                                self.set_options_timer * 1.5)
                            # Prevents accidentally clicking main and
                            # option_circles at same time
                            self.option_lockout = True
                        # If option's circle and not grayed out, perform action
                        else:
                            if action is not None:
                                if hov_color != gray:
                                    self.option_selected = action

            # If not hovering circle, draw inactive circle if possible
            else:
                if circle_number == 0:
                    if not self.image:
                        pygame.draw.circle(
                            gameDisplay, no_hov_color, (x, y), radius)
                    if circle_number == 0:
                        self.show_tower_image()
                if self._options_countdown > 0:
                    pygame.draw.circle(
                        gameDisplay, no_hov_color, (x, y), radius)
                    if circle_number == 0:
                        self.show_tower_image()
            # If message exists, show message
            if msg and (circle_number == 0 or self._options_countdown > 0):
                if circle_number == 0:
                    self.set_text(x, y, msg, msg_col, True)
                else:
                    self.set_text(x, y, msg, msg_col, False)
        # release from option_lockout (must be re-called each frame)
        self.option_lockout = False

    @staticmethod
    def gray_options(circle_number):
        """Returns True for grayed-out options"""
        if circle_number > 0:
            return True
        else:
            return False

    def show_tower_image(self):
        """Shows the tower image (except for tier 0 tower)"""
        pass

    def set_text(self, x, y, msg, msg_color, is_main):
        """Draw text inside of option circle if specified"""
        if is_main:
            font = pygame.font.SysFont(self._font, self._font_size, bold=True)
        else:
            font = pygame.font.SysFont(
                self._font, int(self._font_size * .6), bold=True)
        text_surface = font.render(msg, True, msg_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        gameDisplay.blit(text_surface, text_rect)


class BasicTower(TowerButton):
    """Base class for all towers (inherits from TowerButton)
    

    See Tower button for how buttons work and most arguments and attributes.
    Here only non-inherited arguments attributes will be defined. No new 
    methods are defined here (just slight augmentations of TowerButton methods).
    
    Args:
        tower_range (int, default=125): Defines self.radius 
    
    Attributes:
        radius (int): The distance at which a tower will detect and
                     fire at an enemy
        buy (int): The cost of the tower
        sell (int): The price the tower will sell for
    """
    def __init__(
            self, location, tower_range=125, destroy=True,
            option_count=5, opt1_msg="Sell", opt1_action="sell",
            opt2_msg="Ice", opt2_action="ice1", opt3_msg="Fire",
            opt3_action="fire1", opt4_msg="Poison", opt4_action="poison1",
            opt5_msg="Dark", opt5_action="dark1",
            main_color1=grass_green, main_color2=bright_green,
            opt1_col1=yellow,
            opt1_col2=bright_yellow, opt2_col1=teal,
            opt2_col2=bright_teal, opt3_col1=red,
            opt3_col2=bright_red, opt4_col1=green,
            opt4_col2=bright_green, opt5_col1=purple,
            opt5_col2=bright_purple
    ):
        super().__init__(
            location, destroy=destroy,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, opt2_msg=opt2_msg, opt2_action=opt2_action,
            opt3_msg=opt3_msg, opt3_action=opt3_action, opt4_msg=opt4_msg,
            opt4_action=opt4_action, opt5_msg=opt5_msg, opt5_action=opt5_action,
            main_color1=main_color1, main_color2=main_color2,
            opt1_col1=opt1_col1, opt1_col2=opt1_col2, opt2_col1=opt2_col1,
            opt2_col2=opt2_col2, opt3_col1=opt3_col1, opt3_col2=opt3_col2,
            opt4_col1=opt4_col1, opt4_col2=opt4_col2, opt5_col1=opt5_col1,
            opt5_col2=opt5_col2
        )
        self.image, self.image_width, self.image_height = basicTower1
        self.radius = tower_range  # range
        self.buy = 100
        self.sell = 75
        self.tier = 1

    def show_tower_image(self):
        """Shows the tower image"""
        gameDisplay.blit(
            self.image, (int(self.x - 0.5 * self.image_width),
                         int(self.y - .8 * self.image_height)))

    @staticmethod
    def gray_options(circle_number):
        """Returns True for grayed-out options"""
        if circle_number > 1:
            return True
        else:
            return False


class IceTower1(BasicTower):
    """Tier 1 ice tower (inherits from BasicTower, and TowerButton)
    
    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            opt2_msg="Tier 3", opt2_action="ice2",
            main_color1=blue, main_color2=bright_blue, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, opt2_msg=opt2_msg,
            opt2_action=opt2_action, destroy=destroy)
        self.image, self.image_width, self.image_height = iceTower1
        self.buy = 125
        self.sell = 170
        self.tier = 2


class IceTower2(BasicTower):
    """Tier 3 ice tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=blue, main_color2=bright_blue, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, destroy=destroy)
        self.image, self.image_width, self.image_height = iceTower2
        self.buy = 150
        self.sell = 280
        self.tier = 3


class FireTower1(BasicTower):
    """Tier 1 fire tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=red, main_color2=bright_red,
            opt2_msg="Tier 3", opt2_action="fire2", opt2_col1=red,
            opt2_col2=bright_red, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, opt2_msg=opt2_msg,
            opt2_action=opt2_action, opt2_col1=opt2_col1,
            opt2_col2=opt2_col2, destroy=destroy)
        self.image, self.image_width, self.image_height = fireTower1
        self.buy = 125
        self.sell = 170
        self.tier = 2


class FireTower2(BasicTower):
    """Tier 3 fire tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=1, opt1_msg="Sell", opt1_action="sell",
            main_color1=red, main_color2=bright_red, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, destroy=destroy)
        self.image, self.image_width, self.image_height = fireTower2
        self.buy = 150
        self.sell = 280
        self.tier = 3


class PoisonTower1(BasicTower):
    """Tier 1 poison tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=green, main_color2=bright_green,
            opt2_msg="Tier 3", opt2_action="poison2", opt2_col1=green,
            opt2_col2=bright_green, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, opt2_msg=opt2_msg,
            opt2_action=opt2_action, opt2_col1=opt2_col1,
            opt2_col2=opt2_col2, destroy=destroy)
        self.image, self.image_width, self.image_height = poisonTower1
        self.buy = 125
        self.sell = 170
        self.tier = 2


class PoisonTower2(BasicTower):
    """Tier 3 poison tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=1, opt1_msg="Sell", opt1_action="sell",
            main_color1=red, main_color2=bright_red, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, destroy=destroy)
        self.image, self.image_width, self.image_height = poisonTower2
        self.buy = 150
        self.sell = 280
        self.tier = 3


class DarkTower1(BasicTower):
    """Tier 1 dark tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=purple, main_color2=bright_purple,
            opt2_msg="Tier 3", opt2_action="dark2", opt2_col1=purple,
            opt2_col2=bright_purple, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, opt2_msg=opt2_msg,
            opt2_action=opt2_action, opt2_col1=opt2_col1,
            opt2_col2=opt2_col2, destroy=destroy)
        self.image, self.image_width, self.image_height = darkTower1
        self.buy = 125
        self.sell = 170
        self.tier = 2


class DarkTower2(BasicTower):
    """Tier 3 dark tower (inherits from BasicTower, and TowerButton)

    See BasicTower and TowerButton for explanations, arguments, attributes,
    and method descriptions.
    """
    def __init__(
            self, location, tower_range=125,
            option_count=1, opt1_msg="Sell", opt1_action="sell",
            main_color1=red, main_color2=bright_red, destroy=True):
        super().__init__(
            location, tower_range=tower_range,
            option_count=option_count, opt1_msg=opt1_msg,
            opt1_action=opt1_action, main_color1=main_color1,
            main_color2=main_color2, destroy=destroy)
        self.image, self.image_width, self.image_height = darkTower2
        self.buy = 150
        self.sell = 280
        self.tier = 3


class BasicMissile:
    """Basic missile (fire from BasicTower) locks onto and hits enemy
    
    The basic missile locks onto enemy within associated tower's attack radius.
    It will travel toward that enemy until enemy is hit or dies. If hit occurs,
    that information will be returned to the function caller.
    
    Args:
        location (tuple, int): Defines self.x, self.y
        
    Attributes:
        x (int): The x-coordinate missile is currently at
        y (int): The y-coordinate missile is currently at
        _tower_location (tuple, int): Location of tower, missiles origin
        speed (int): speed at which missile moves toward enemy
        lock_on (obj): Enemy which missile is locked on to
        destroy (bool): If True, missile deletes and returns to tower
        radius (int): Defines size of missile picture and collision detection
        shoot_rate (int): Game frames until next fire after destroyed
        shoot_counter (int): Counts from shoot_rate to 0
        missile_color (tuple, int): Color of the missile
        damage (int): Damage given to enemy on hit (varies by specialty)
        specialty (str): Defines special attributes of missile
        hit_sound (obj): Object of sound to play on missile hit
        
    Methods:
        lock_enemy: Locks missile onto enemy and calls shoot
        shoot: Causes missile to travel toward locked enemy and call hit
        hit: Determines if missile hit enemy
        adjust_counters: Decrements shoot counter
    """
    def __init__(self, location):
        self.x, self.y = location
        x, y = location
        self.x = x
        self.y = y - 50
        self._tower_location = self.x, self.y
        self.speed = 4
        self.lock_on = None
        self.destroy = True
        self.radius = 5
        self.shoot_rate = 2 * seconds
        self.shoot_counter = 0
        self.missile_color = gray
        self.damage = 50
        self.specialty = "basic"
        self.hit_sound = basic_hit_sound

    def lock_enemy(self, tower, enemy):
        """Locks missile onto enemy and calls shoot()

        To lock on need shoot_counter at 0, enemy alive, no missile alive.
        Then, if enemy in range of tower, un-destroy missile. Then call shoot
        and listen for and return hit.

        Args:
            tower (obj): Tower associated with missile
            enemy (obj): Enemy to try to lock on to

        Returns:
            hit (tuple, int, str, obj): The result passed returned by shoot()
        """
        if self.shoot_counter < 1:
            if not enemy.destroy:
                if self.destroy is True:
                    if self.lock_on is None:
                        if helpers.collision(tower, enemy):
                            tower_shoot_sound.play()
                            self.lock_on = enemy
                            self.destroy = False
                            self.shoot_counter = self.shoot_rate
        hit = self.shoot(enemy)
        return hit

    def shoot(self, enemy):
        """Causes missile to travel toward locked enemy and call hit

        Move missile towards locked on enemy by self.speed and redraw. Call and
        return hit.

        Args:
            enemy (obj): Enemy missiles is firing at

        Returns:
            hit (tuple, int, str, obj): the result of hit() function call
        """
        if not self.destroy:
            if self.lock_on == enemy:
                if self.x < enemy.x:
                    self.x += self.speed
                if self.x > enemy.x:
                    self.x -= self.speed
                if self.y < enemy.y:
                    self.y += self.speed
                if self.y > enemy.y:
                    self.y -= self.speed
                pygame.draw.circle(
                    gameDisplay, self.missile_color,
                    (self.x, self.y), self.radius)
                hit = self.hit(enemy)
                if hit:
                    return hit

    def hit(self, enemy):
        """Determines if missile hit enemy

        Check for collision between missile and enemy. If collision with locked
        on target occurs, destroy missile and set its location back to tower.
        If the enemy is not destroyed, return damage, specialty and hit_sound.

        Args:
            enemy: Locked on enemy to check missile collision against

        Returns:
            self.damage (int): Damage given to enemy on hit
                               (varies by specialty)
            self.specialty (str): Defines special attributes of missile
            self.hit_sound (obj): Object of sound to play on missile hit
        """
        if helpers.collision(self, enemy):
            self.destroy = True
            self.lock_on = None
            self.x, self.y = self._tower_location
            if not enemy.destroy:
                return self.damage, self.specialty, self.hit_sound

    def adjust_counters(self):
        if self.shoot_counter > 0:
            self.shoot_counter -= 1


class IceMissile1(BasicMissile):
    """T1 ice missile (from T1 ice tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'ice1' specialty slows enemy and deals up-front damage reduced by armor
    """
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5
        self.missile_color = bright_blue
        self.specialty = "ice1"
        self.hit_sound = ice_hit_sound


class IceMissile2(BasicMissile):
    """T2 ice missile (from T2 ice tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'ice2' specialty slows enemy and deals up-front damage reduced by armor
    """
    def __init__(self, location):
        super().__init__(location)
        self.damage = 56.25
        self.missile_color = bright_teal
        self.specialty = "ice2"
        self.radius = 6
        self.hit_sound = ice_hit_sound


class FireMissile1(BasicMissile):
    """T1 fire missile (from T1 fire tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'fire1' burns catches enemy on fire, dealing damage per second for 3
    seconds. Does no up-front damage, DoT burn reduced by armor.
    Enemies on fire will catch other nearby enemies on fire.
    """
    def __init__(self, location):
        super().__init__(location)
        self.damage = 25
        self.missile_color = red
        self.specialty = "fire1"
        self.shoot_rate = 3 * seconds
        self.hit_sound = fire_hit_sound

    def lock_enemy(self, tower, enemy):
        """Locks missile onto enemy and calls shoot()

        Difference with BasicMissile lock_enemy: Will not lock onto enemy
        if burn just applied to that enemy.
        """
        if self.shoot_counter < 1:
            # Only lock-on if not freshly burned
            if enemy.burned_counter < 2:
                if not enemy.destroy:
                    if self.destroy is True:
                        if self.lock_on is None:
                            if helpers.collision(tower, enemy):
                                self.lock_on = enemy
                                self.destroy = False
                                self.shoot_counter = self.shoot_rate
        hit = self.shoot(enemy)
        return hit


class FireMissile2(BasicMissile):
    """T2 fire missile (from T2 fire tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'fire2' burns catches enemy on fire, dealing damage per second for 3
    seconds. Does no up-front damage, DoT burn reduced by armor.
    Enemies on fire will catch other nearby enemies on fire."""
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5
        self.missile_color = bright_red
        self.specialty = "fire2"
        self.shoot_rate = 3 * seconds
        self.radius = 8
        self.hit_sound = fire_hit_sound

    def lock_enemy(self, tower, enemy):
        """Locks missile onto enemy and calls shoot()

        Difference with BasicMissile lock_enemy: Will not lock onto enemy
        if burn just applied to that enemy.
        """
        if self.shoot_counter < 1:
            # Only lock-on if not freshly burned
            if enemy.burned_counter < 2:
                if not enemy.destroy:
                    if self.destroy is True:
                        if self.lock_on is None:
                            if helpers.collision(tower, enemy):
                                self.lock_on = enemy
                                self.destroy = False
                                self.shoot_counter = self.shoot_rate
        hit = self.shoot(enemy)
        return hit


class PoisonMissile1(BasicMissile):
    """T1 poison missile (from T1 poison tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'poison1' deals armor piercing, percentage-current-health damage every
    2 seconds for 10 seconds (no up-front damage), and stuns at end of
    poison duration."""
    def __init__(self, location):
        super().__init__(location)
        self.damage = 0.05
        self.missile_color = green
        self.specialty = "poison1"
        self.shoot_rate = 3 * seconds
        self.hit_sound = poison_hit_sound

    def lock_enemy(self, tower, enemy):
        """Locks missile onto enemy and calls shoot()

        Difference with BasicMissile lock_enemy: Will not lock onto enemy
        until poison off or nearly off.
        """
        if self.shoot_counter < 1:
            # Only lock-on if not poisoned (or about to be)
            if enemy.poison_charges < 2:
                if not enemy.destroy:
                    if self.destroy is True:
                        if self.lock_on is None:
                            if helpers.collision(tower, enemy):
                                self.lock_on = enemy
                                self.destroy = False
                                self.shoot_counter = self.shoot_rate
        hit = self.shoot(enemy)
        return hit


class PoisonMissile2(BasicMissile):
    """T2 poison missile (from T2 poison tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'poison2' deals armor piercing, percentage-current-health damage every
    2 seconds for 10 seconds (no up-front damage), and stuns at end of
    poison duration."""
    def __init__(self, location):
        super().__init__(location)
        self.damage = 0.10
        self.missile_color = bright_green
        self.specialty = "poison2"
        self.shoot_rate = 3 * seconds
        self.radius = 6
        self.hit_sound = poison_hit_sound

    def lock_enemy(self, tower, enemy):
        """Locks missile onto enemy and calls shoot()

        Difference with BasicMissile lock_enemy: Will not lock onto enemy
        until poison off or nearly off.
        """
        if self.shoot_counter < 1:
            # Only lock-on if not poisoned (or nearly so)
            if enemy.poison_charges < 2 or not enemy.poison2:
                if not enemy.destroy:
                        if self.destroy is True:
                            if self.lock_on is None:
                                if helpers.collision(tower, enemy):
                                    self.lock_on = enemy
                                    self.destroy = False
                                    self.shoot_counter = self.shoot_rate

        hit = self.shoot(enemy)
        return hit


class DarkMissile1(BasicMissile):
    """T1 dark missile (from T1 poison tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'dark1' deals armor piercing, up front damage."""
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5  # 75 / 2 (for 1/2 armor pen)
        self.missile_color = purple
        self.specialty = "dark1"
        self.hit_sound = dark_hit_sound


class DarkMissile2(BasicMissile):
    """T2 dark missile (from T2 poison tower), inherits from BasicMissile

    See BasicMissile for explanations, arguments, attributes,
    and method descriptions.

    'dark2' deals armor piercing, up front damage."""
    def __init__(self, location):
        super().__init__(location)
        self.damage = 112.5
        self.missile_color = bright_purple
        self.specialty = "dark2"
        self.radius = 6
        self.hit_sound = dark_hit_sound
