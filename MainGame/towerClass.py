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

    Attributes:
        location:       (Required) tuple(x, y), positions center of tower circle
        button_ radius: radius of tower, defaults to 24 pixels
        main_msg:       message to display on tower (optional)
        main_color1:    color without mouse hover (default light_brown)
        main_color2:    color on mouse hover (default orange)
        font:           font for optional button message,
                        default 'Comic Sans MS'
        font_size:      font size of optional message, defaults to 20
        message_color:  txt color of main button optional msg, defaults = black
        option_count:   number of option buttons to create (default = 1)
                        Note: can specify 0-5 options
                        (numbers greater than 5 won't have button)

        The following entries will use # to designate an option number:
        opt#_col1:      option's color while mouse not hovering button
                        default different for each option
        opt#_col2:      option's color while mouse is hovering button
        opt#_msg:       that option's message (default is None)
        opt#_msg_col:   that option's message color (default is black)

    Usage:
        Define a button with x, y coordinates specified, and optional kwargs
        call draw in main loop to draw button and associated option buttons
    """

    def __init__(
            self, location, button_radius=24, destroy=False,
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

        self.image = None
        self._button_radius = button_radius
        self._mouse = None
        self._click = None
        self.x, self.y = location
        self._font = font
        self._font_size = font_size
        self.destroy = destroy
        self.option_selected = None
        self._options_countdown = 0
        self.set_options_timer = set_options_timer
        self.option_count = option_count
        self.lockout = 20
        self.lockout_timer = self.lockout
        self.option_lockout = self.lockout_timer
        self.gray_out = False
        self.tier = 0
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
        if self.construct_countdown > 0:
            self.construct_countdown -= 1
            if self.frame_counter > 0:
                self.frame_counter -= 1
            else:
                self.construct_image = hammer_list[self.frame][0]
                self.frame += 1
                if self.frame > len(hammer_list) - 1:
                    self.frame = 0
                self.frame_counter = self.frames_to_picswap
            gameDisplay.blit(
                wood[0],
                (int(self.x - 0.5 * self.construct_width),
                 int(self.y - .8 * self.construct_height)))
            gameDisplay.blit(
                self.construct_image,
                (int(self.x - 0.3 * self.construct_width),
                 int(self.y - 1 * self.construct_height)))
            self.construction_bar()
        else:
            self.destroy = False
            self.constructing = False

    def construction_bar(self):
        max_width = self.construct_width // 2
        if self.construct_countdown >= 0:
            construct_width = int(max_width
                                  * (self.construct_timer
                                     - self.construct_countdown)
                                  // self.construct_timer)
        else:
            construct_width = 0
        height = 4
        back_color = white
        front_color = bright_orange
        x = self.x - self.construct_width // 4
        y = self.y - self.construct_height * 1 // 4
        pygame.draw.rect(gameDisplay, back_color,
                         (x, y, max_width, height))
        if construct_width:
            pygame.draw.rect(gameDisplay, front_color,
                             (x, y, construct_width, height))

    def draw(self):
        """Draw main and option circles, highlight color if hovered
        perform action if clicked,
        show options for a period of set_option_timer"""
        if self._options_countdown > 0:
            self._options_countdown -= 1
        if self.lockout_timer > 0:
            self.lockout_timer -= 1

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
                if self.option_lockout > 0:
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
                if circle_number == 0 or self._options_countdown > 0:
                    pygame.draw.circle(gameDisplay, hov_color, (x, y), radius)
                    if circle_number == 0:
                        self.show_tower_image()
                    if circle_number > 0:
                        self._options_countdown = self.set_options_timer
                    if self._click[0] == 1:
                        if circle_number == 0:
                            self._options_countdown = int(
                                self.set_options_timer * 1.5)
                            # Prevents accidentally clicking main and
                            # option_circles at same time
                            self.option_lockout = True
                        else:
                            if action is not None:
                                if hov_color != gray:
                                    self.option_selected = action
                                    self.lockout_timer = self.lockout

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

            if msg and (circle_number == 0 or self._options_countdown > 0):
                if circle_number == 0:
                    self.set_text(x, y, msg, msg_col, True)
                else:
                    self.set_text(x, y, msg, msg_col, False)

        self.option_lockout = False

    @staticmethod
    def gray_options(circle_number):
        if circle_number > 0:
            return True
        else:
            return False

    def show_tower_image(self):
        pass

    def set_text(self, x, y, msg, msg_color, is_main):
        """Draw text over main or option circles if specified"""
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
        gameDisplay.blit(
            self.image, (int(self.x - 0.5 * self.image_width),
                         int(self.y - .8 * self.image_height)))

    @staticmethod
    def gray_options(circle_number):
        if circle_number > 1:
            return True
        else:
            return False


class IceTower1(BasicTower):
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            opt2_msg="Tier 2", opt2_action="ice2",
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
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=red, main_color2=bright_red,
            opt2_msg="Tier 2", opt2_action="fire2", opt2_col1=red,
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
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=green, main_color2=bright_green,
            opt2_msg="Tier 2", opt2_action="poison2", opt2_col1=green,
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
    def __init__(
            self, location, tower_range=125,
            option_count=2, opt1_msg="Sell", opt1_action="sell",
            main_color1=purple, main_color2=bright_purple,
            opt2_msg="Tier 2", opt2_action="dark2", opt2_col1=purple,
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


# Deals up-front damage, reduced by armor
class BasicMissile:
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
        # Checks, need: shoot_counter at 0, enemy alive, no missile alive,
        # Then, if enemy in range of tower, un-destroy missile
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
        # Move missile towards locked on enemy by self.speed and redraw.
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
        # Check for collision between missile and enemy
        # If collision to locked on target,
        # destroy missile and set its location back to tower
        if helpers.collision(self, enemy):
            self.destroy = True
            self.lock_on = None
            self.x, self.y = self._tower_location
            if not enemy.destroy:
                return self.damage, self.specialty, self.hit_sound

    def adjust_counters(self):
        if self.shoot_counter > 0:
            self.shoot_counter -= 1


# Slows enemy and deals up-front damage reduced by armor
class IceMissile1(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5
        self.missile_color = bright_blue
        self.specialty = "ice1"
        self.hit_sound = ice_hit_sound


# Slows enemy and deals up-front damage reduced by armor
class IceMissile2(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 56.25
        self.missile_color = bright_teal
        self.specialty = "ice2"
        self.radius = 6
        self.hit_sound = ice_hit_sound


# Burns catches enemy on fire, dealing damage per second for 3 seconds
# No up-front damage, DoT burn reduced by armor
# Enemies on fire will catch other nearby enemies on fire
class FireMissile1(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 25
        self.missile_color = red
        self.specialty = "fire1"
        self.shoot_rate = 3 * seconds
        self.hit_sound = fire_hit_sound

    def lock_enemy(self, tower, enemy):
        # Checks, need: shoot_counter at 0, enemy alive, no missile alive,
        # Then, if enemy in range of tower, un-destroy missile
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


# Burns catches enemy on fire, dealing damage per second for 3 seconds
# No up-front damage, DoT burn reduced by armor
# Enemies on fire will catch other nearby enemies on fire
class FireMissile2(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5
        self.missile_color = bright_red
        self.specialty = "fire2"
        self.shoot_rate = 3 * seconds
        self.radius = 8
        self.hit_sound = fire_hit_sound

    def lock_enemy(self, tower, enemy):
        # Checks, need: shoot_counter at 0, enemy alive, no missile alive,
        # Then, if enemy in range of tower, un-destroy missile
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


# Deals armor piercing DoT every 5 seconds (no up-front damage)
# Poison lasts indefinitely
class PoisonMissile1(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 0.05
        self.missile_color = green
        self.specialty = "poison1"
        self.shoot_rate = 3 * seconds
        self.hit_sound = poison_hit_sound

    def lock_enemy(self, tower, enemy):
        # Checks, need: shoot_counter at 0, enemy alive, no missile alive,
        # Then, if enemy in range of tower, un-destroy missile
        if self.shoot_counter < 1:
            # Only lock-on if not poisoned
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


# Deals armor piercing DoT every 5 seconds (no up-front damage)
# Poison lasts indefinitely
class PoisonMissile2(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 0.10
        self.missile_color = bright_green
        self.specialty = "poison2"
        self.shoot_rate = 3 * seconds
        self.radius = 6
        self.hit_sound = poison_hit_sound

    def lock_enemy(self, tower, enemy):
        # Checks, need: shoot_counter at 0, enemy alive, no missile alive,
        # Then, if enemy in range of tower, un-destroy missile
        if self.shoot_counter < 1:
            # Only lock-on if not poisoned
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


# Deals quadruple damage (3/4 as armor piercing)
class DarkMissile1(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 37.5  # 75 / 2 (for 1/2 armor pen)
        self.missile_color = purple
        self.specialty = "dark1"
        self.hit_sound = dark_hit_sound


# Deals quadruple damage (3/4 as armor piercing)
class DarkMissile2(BasicMissile):
    def __init__(self, location):
        super().__init__(location)
        self.damage = 112.5
        self.missile_color = bright_purple
        self.specialty = "dark2"
        self.radius = 6
        self.hit_sound = dark_hit_sound
