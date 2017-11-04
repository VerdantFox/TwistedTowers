import random

import pygame
import helpers

from gameText import mage_speech1, mage_speech2
from Enemies.orc.orcPics import orc_list, orcdead
from Enemies.spider.spiderPics import spider_list, spiderdead
from Enemies.turtle.turtlePics import turtle_list, turtledead
from Enemies.wolf.wolfPics import wolf_list, wolfdead
from Enemies.dragon.dragonPics import dragon_list, dragondead
from Enemies.lizard.lizardPics import lizard_list, lizarddead
from Enemies.mage.magePics import mage_list, magestanding
from definitions import *
from gameParameters import gameDisplay
from lists import *
from towers.towerPics import fire_pic, ice_pic, poison_list, stun_list
from sounds import spider_death_sound, wolf_death_sound, turtle_death_sound, \
    dragon_death_sound, orc_death_sound, lizard_death_sound, mage_spell_sound, \
    grumbling_sound


class Orc:
    """Orc enemy class, high health, low armor (base for other enemies)

    Args:
        location (tuple, default=path_nodes[0]): Defines (self.x, self.y)
        next_node (tuple, default=path_nodes[0]): Defines self.next_node
        stationary (bool, default=False): Defines self.stationary
        destroy (bool, default=True): Defines self.destroy

    Attributes:
        # Position and movement
        x, y (tuple, int): Gives location of enemy
        base_speed (float): Enemy move and image cycling speed, default: 1
        speed: Actual speed used (adjusted by ice, reverts to base_speed)
        right (bool): True if next node x greater than enemy x
        left (bool): True if next node x less than enemy x
        up (bool): True if next node y less than enemy y
        down (bool): True if next node y greater than enemy y
        next_node (tuple, int): The point on map enemy travels to next
        node_index (int): Index used to get next node in 'enemy_nodes' list
        stationary (bool): If True, stops x,y movement (default: False)

        # Image manipulation
        image (loaded Pygame image): The image displayed
        image_width (int): Width of image
        image_height (int): Height of image
        default_frames_to_picswap (int): Default frames until image change
        frames_to_picswap (int): Frames to change (reverts to default)
        frame_counter (int): counts down, at zero changes image
        direction_index (int): Changes image facing direction in list
        frame (int): Index of current image frame in list of images

        # Interaction with other objects
        radius (int): Radius for collision detection with other objects
        initial_fire_radius: Radius for fire1 detection
        fire_radius: Radius for fire2 detection (reverts to initial)

        # hp manipulation
        max_hp (float): Maximum health of enemy (800 for orc)
        hp (float): Actual health of enemy, decreases with damage
        armor (float): Resistance to damage (0-100) (20 for orc)

        # Death and destruction
        death_sound: Sound object to play() on death (in sounds.py)
        destroy (bool): Removes live body if False
        dead (bool): Used to return stat and money
        cash: Amount of money returned for kill
        points: Amount of points returned for kill
        spawn_timer (int): Time from dead (initially True) to spawning
        spawn_countdown (int): Counts down from spawn_timer to zero
        lives (int): Number of lives (need minimum of 2 b/c start dead)
        dead_image: Image displayed after death
        dead_image_timer (int):  Time dead_image is shown (4 * seconds)
        dead_image_countdown: Counts down from dead_image_timer to 0
        dead_x: x coordinate location of enemy at time of death
        dead_y: y coordinate location of enemy at time of death
        dead_font: Font used for stat display

        # Ice specialties
        ice_loc(tuple in tuple, int): Relative x, y adjustments for ice image
        ice1 (bool): True for ice_counter secs if hit by tier 1 ice tower
        ice2 (bool): True for ice_counter secs if hit by tier 2 ice tower
        ice_counter (int): Duration of slow from ice tower strike
        ice1_countdown (int): Counts down from ice_counter to 0
        ice2_countdown (int): Counts down from ice_counter to 0

        # Fire specialties
        fire_loc (tuple, int): x, y offset for fire image relative to body
        fireball1 (int): Counts down time enemy can flame other enemies
        fireball2 (int): Counts down time enemy can flame other enemies
        fire1 (float): Damage taken per second while on fire
        fire2 (float): Damage taken per second while on fire
        burned_counter (int): Each tick down damages enemy
        fire_countdown (int): Frame count (time) between burn ticks

        # Poison specialties
        poison_loc (tuple in tuple, int): Relative x, y adjustments
                                          for poison image
        stun_loc: (tuple in tuple, int): Relative x, y adjustments
                                          for stun image
        poison1 (float): Poison damage per tick from tier 1 poison
        poison2 (float): Poison damage per tick from tier 2 poison
        poison_tick (int): Frames (time) until next poison tick damage
        poison_charges (int): Remaining ticks of poison damage
        stun (bool): True if stunned
        stun_duration (int): frames (time) of stun duration
        stun_duration_countdown (int): countdown from stun_duration to 0
        stun_frameswap_rate (int): Game frames until next stun image frame
        stun_frame (int): Index of stun image list
        stun_framecounter (int): Counts frames from stun_frameswap_rate to 0
        
    Methods:
        draw: Moves enemy unless stunned, changing image to show walking
              motion. Checks for special (elemental) attributes and calls
              associated functions if it find them. If enemy is dead, shows
              corpse and stat loot and removes elemental effects.
        walk: Changes image as enemy moves to animate movement
        show: Shows enemy, health bar, and calls elemental effects functions
        show_poison: Show poison cloud attached to enemy
        show_stun: Shows poison cloud attached to enemy
        show_fire: Shows fire attached to enemy
        show_ice: Shows ice attached to enemy
        take_damage: Reduces enemy's health as damage taken, modified by armor
        health_bar: Displays health bar as a visual of enemy percent health
        iced: Slows enemy movement and animation, doubly so for rank 2
        burning: Causes fire damage over time to enemy, prioritising rank 2
        poisoned: Damages enemies as % hp or min damage, stuns toward end
        check_death: Checks if enemy is dead, plays sound
                     and returns stat/points
        hit: Expressed on tower shot hit, translates specialty and damage
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        # Position and movement
        self.x, self.y = location
        self.base_speed = 1
        self.speed = self.base_speed
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.next_node = next_node  # see lists.py
        self.node_index = 0
        self.stationary = stationary

        # Image manipulation
        self.image = orc_list[0][0]
        self.image_width = 60
        self.image_height = 60
        self.default_frames_to_picswap = 8
        self.frames_to_picswap = 8
        self.frame_counter = 0
        self.direction_index = 2
        self.frame = 0

        # Interaction with other objects
        self.radius = 5
        self.initial_fire_radius = 30
        self.fire_radius = 30

        # hp manipulation
        self.max_hp = 800
        self.hp = 800
        self.armor = 20

        # Death and destruction
        self.death_sound = orc_death_sound
        self.destroy = destroy  # Removes live body
        self.dead = False  # Used to return stat and money
        self.cash = 75
        self.points = self.cash // 3
        self.spawn_timer = random.randint(5 * seconds, 6.75 * seconds)
        self.spawn_countdown = self.spawn_timer
        self.lives = 2  # start dead, need 1 more than that
        self.dead_image = orcdead
        self.dead_image_timer = 4 * seconds
        self.dead_image_countdown = 0
        self.dead_x = 0
        self.dead_y = 0
        self.dead_font = pygame.font.SysFont("Comic Sans MS", 14, bold=True)

        # Ice specialties
        self.ice_loc = ((-18, 10), (-18, 10), (-18, 10),
                        (-18, 10), (-18, 3))
        self.ice1 = False
        self.ice2 = False
        self.ice_counter = 2.5 * seconds
        self.ice1_countdown = self.ice_counter
        self.ice2_countdown = self.ice_counter

        # Fire specialties
        self.fire_loc = (-10, -50)
        self.fireball1 = 0
        self.fireball2 = 0
        self.fire1 = None
        self.fire2 = None
        self.burned_counter = 0
        self.fire_countdown = 1 * seconds

        # Poison specialties
        self.poison_loc = ((-27, -45), (-36, -57), (-51, -40),
                           (-45, -9), (-27, -3))
        self.stun_loc = ((-10, -40), (-5, -50), (-5, -50),
                         (-5, -50), (-10, -50))
        self.poison1 = None
        self.poison2 = None
        self.poison_tick = 0
        self.poison_charges = 0
        self.stun = False
        self.stun_duration = 0.75 * seconds
        self.stun_duration_countdown = 0 * seconds
        self.stun_frameswap_rate = 10
        self.stun_framecounter = 0
        self.stun_frame = 0

    def draw(self):
        """Calls manipulates enemy and calls associated functions

        Moves enemy unless stunned, changing image to show walking motion.
        Checks for special (elemental) attributes and calls associated
        functions if it find them. If enemy is dead, shows corpse and
        stat loot and removes elemental effects.

        No args

        Returns:
            1 if enemy reaches last node (castle), else None
        """
        if not self.destroy:
            if not self.stun:
                if not self.stationary:
                    # Move towards node by self.speed.
                    if self.x < self.next_node[0] - 5:
                        self.x += self.speed
                        self.right = True
                    if self.x > self.next_node[0] + 5:
                        self.x -= self.speed
                        self.left = True
                    if self.y < self.next_node[1] - 5:
                        self.y += self.speed
                        self.down = True
                    if self.y > self.next_node[1] + 5:
                        self.y -= self.speed
                        self.up = True

                # Change walking frame if frame_counter reaches 0
                if self.frame_counter < 1:
                    # Determine direction_index
                    self.direction_index = 2  # Default is right
                    if self.down and not self.right:
                        self.direction_index = 0
                    if self.down and self.right:
                        self.direction_index = 1
                    if self.right and not (self.up or self.down):
                        self.direction_index = 2
                    if self.up and self.right:
                        self.direction_index = 3
                    if self.up and not self.right:
                        self.direction_index = 4

                    self.walk()
                    self.frame_counter = self.frames_to_picswap
                if self.frame_counter > 0:
                    self.frame_counter -= self.speed

            if self.stun:
                if self.stun_duration_countdown == 0:
                    self.stun = False
                if self.stun_duration_countdown > 0:
                    self.stun_duration_countdown -= 1

            # Check for special attributes
            if self.ice1 or self.ice2:
                self.iced()
            if self.poison2:
                self.poisoned(self.poison2)
            if self.poison1 and not self.poison2:
                self.poisoned(self.poison1)
            if self.fire1 or self.fire2:
                self.burning()
            if self.fireball1 > 0:
                self.fireball1 -= 1
            if self.fireball2 > 0:
                self.fireball2 -= 1
            else:
                self.fire_radius = self.initial_fire_radius

            # Show
            self.show()

            # Switch to next node in path if at current node goal
            if self.next_node[0] - 10 < self.x < self.next_node[0] + 10:
                if self.next_node[1] - 10 < self.y < self.next_node[1] + 10:
                    if self.node_index < len(path_nodes) - 2:
                        self.node_index += 1
                        # see lists.py
                        node_x, node_y = path_nodes[self.node_index]
                        # Introduce some randomness to node locations
                        node_x += random.randrange(-10, 10)
                        node_y += random.randrange(-15, 15)
                        self.next_node = (node_x, node_y)  # See lists
                    else:
                        # Destroy and remove all affects, move to start of path
                        self.destroy = True
                        self.poison1 = None
                        self.poison2 = None
                        self.poison_tick = 0
                        self.poison_charges = 0
                        self.ice1 = False
                        self.ice2 = False
                        self.speed = self.base_speed
                        self.fire1 = None
                        self.fire2 = None
                        self.fireball1 = 0
                        self.fireball2 = 0
                        self.x, self.y = path_nodes[0]
                        # Return damage to castle
                        return 1

        # If enemy is dead
        if self.destroy:
            # Show body
            if self.dead_image_countdown > 0:
                gameDisplay.blit(
                    self.dead_image, (self.dead_x - self.image_width // 2,
                                      self.dead_y - self.image_height // 2))
                self.dead_image_countdown -= 1
            # Show money earned
            if self.dead_image_countdown > 3 * seconds:
                text_surface = self.dead_font.render(
                    "${}".format(self.cash), True, yellow)
                text_rect = text_surface.get_rect()
                text_rect.center = (self.dead_x, self.dead_y - 30)
                gameDisplay.blit(text_surface, text_rect)

            # Start respawn timer countdown
            if self.spawn_countdown > 0:
                self.spawn_countdown -= 1
            # If respawn timer reaches 0, respawn enemy and reset timer
            elif self.spawn_countdown <= 0:
                self.lives -= 1
                self.poison1 = None
                self.poison2 = None
                self.poison_tick = 0
                self.poison_charges = 0
                self.fire1 = None
                self.fire2 = None
                self.fireball1 = 0
                self.fireball2 = 0
                self.burned_counter = 0
                self.ice1 = False
                self.ice2 = False
                self.speed = self.base_speed
                self.destroy = False
                self.x, self.y = path_nodes[0]
                self.node_index = 0
                self.next_node = path_nodes[0]
                self.hp = self.max_hp
                self.spawn_countdown = self.spawn_timer

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = orc_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(orc_list[0]) - 1:
            self.frame = 0

    def show(self):
        """Shows enemy, health bar, and calls elemental effects functions"""
        if not self.destroy:
            if self.poison1 or self.poison2:
                self.show_poison()
            if self.fire1 or self.fire2:
                self.show_fire()
            if self.stun:
                self.show_stun()
            if self.ice1 or self.ice2:
                self.show_ice()

            gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                          self.y - self.image_height // 2))
            self.health_bar()

    def show_poison(self):
        """Show poison cloud attached to enemy"""
        gameDisplay.blit(
            poison_list[self.direction_index][0],
            (self.x + self.poison_loc[self.direction_index][0],
             self.y + self.poison_loc[self.direction_index][1]))

    def show_stun(self):
        """Shows stun attached to enemy"""
        gameDisplay.blit(
            stun_list[self.stun_frame][0],
            (self.x + self.stun_loc[self.direction_index][0],
             self.y + self.stun_loc[self.direction_index][1]))

        self.stun_framecounter -= 1
        if self.stun_framecounter < 1:
            self.stun_framecounter = self.stun_frameswap_rate
            self.stun_frame += 1
            if self.stun_frame == len(stun_list[0]):
                self.stun_frame = 0

    def show_fire(self):
        """Shows fire attached to enemy"""
        gameDisplay.blit(
            fire_pic[0], (self.x + self.fire_loc[0],
                          self.y + self.fire_loc[1]))

    def show_ice(self):
        """Shows ice attached to enemy"""
        gameDisplay.blit(
            ice_pic[0], (self.x + self.ice_loc[self.direction_index][0],
                         self.y + self.ice_loc[self.direction_index][1]))

    def take_damage(self, damage, armor_shred=False):
        """Reduces enemy's health as damage taken, modified by armor

        Args:
            damage (float): Enemy health reduced by damage taken
            armor_shred (bool): If True, armor doesn't reduce damage
        """
        if self.hp > 0:
            damage_reduced = (100 - self.armor) / 100
            if not armor_shred:
                self.hp -= damage * damage_reduced
            if armor_shred:
                self.hp -= damage

        if self.hp <= 0:
            self.dead_x = self.x
            self.dead_y = self.y
            self.dead_image_countdown = self.dead_image_timer
            self.dead = True
            self.destroy = True

    def health_bar(self):
        """Displays health bar as a visual of enemy percent health"""
        max_width = self.image_width // 2
        if self.hp >= 0:
            damage_width = int(max_width * self.hp // self.max_hp)
        else:
            damage_width = 0
        height = 4
        back_color = red
        front_color = green
        x = self.x - self.image_width // 4
        y = self.y - self.image_height * 3 // 4

        pygame.draw.rect(gameDisplay, back_color,
                         (x, y, max_width, height))
        if damage_width:
            pygame.draw.rect(gameDisplay, front_color,
                             (x, y, damage_width, height))

    def iced(self):
        """Slows enemy movement and animation, doubly so for rank 2"""
        if self.ice1_countdown > 0:
            self.ice1_countdown -= 1
        else:
            self.ice1 = False
        if self.ice2_countdown > 0:
            self.ice2_countdown -= 1
        else:
            self.ice2 = False
        multiplier = 1
        if self.ice2:
            multiplier = .4
        if self.ice1 and not self.ice2:
            multiplier = .7
        if not (self.ice1 or self.ice2):
            self.speed = self.base_speed
            self.frames_to_picswap = self.default_frames_to_picswap
        else:
            self.speed = self.base_speed * multiplier
            self.frames_to_picswap = int(
                self.default_frames_to_picswap * 1 / multiplier)

    def burning(self):
        """Causes fire damage over time to enemy, prioritising rank 2"""
        if self.burned_counter > 0:
            if self.fire_countdown == 0:
                if self.fire2:
                    self.take_damage(self.fire2)
                if self.fire1 and not self.fire2:
                    self.take_damage(self.fire1)
                self.fire_countdown = 1 * seconds
                self.burned_counter -= 1
            else:
                self.fire_countdown -= 1
        else:
            self.fire1 = None
            self.fire2 = None

    def poisoned(self, percent_hp):
        """Damages enemies as % hp or min damage, stuns toward end

        Args:
            percent_hp (float): Percentage of enemy health damaged per tick
        """
        # Stun
        if self.poison_charges == 2 and self.poison_tick == 0:
            if self.poison2:
                self.stun_duration_countdown = self.stun_duration * 2
            if self.poison1 and not self.poison2:
                self.stun_duration_countdown = self.stun_duration
            self.stun = True

        # Damage
        poison_damage = percent_hp * self.hp
        if self.poison1:
            if poison_damage < 15:
                poison_damage = 15
        if self.poison2:
            if poison_damage < 22.5:
                poison_damage = 22.5
        if self.poison_charges > 0:
            # 50% armor shred
            if self.poison_tick == 0:
                self.take_damage(poison_damage / 2, True)
                self.take_damage(poison_damage / 2, False)
                self.poison_tick = 2 * seconds
                self.poison_charges -= 1
            else:
                self.poison_tick -= 1
        else:
            self.poison1 = None
            self.poison2 = None

    def check_death(self):
        """Checks if enemy is dead, plays sound and returns stat/points

        Returns:
            self.points (int), self.stat (int): a tuple to adjust game points
                                                and funds
        """
        if self.dead:
            self.death_sound.play()
            self.dead = False
            return self.points, self.cash
        else:
            return None

    def hit(self, damage, specialty):
        """Expressed on tower shot hit, translates specialty and damage

        Args:
            damage: Damage taken from tower shot (from missiles.damage),
                    means different things for different damage types
            specialty: Elemental type, to specialise damage and disabilities
        """
        if specialty == "basic":
            self.take_damage(damage)
        if specialty == "ice1":
            self.take_damage(damage)
            self.ice1 = True
            self.ice1_countdown = self.ice_counter
        if specialty == "ice2":
            self.take_damage(damage)
            self.ice2 = True
            self.ice2_countdown = self.ice_counter
        if specialty == "fire1":
            self.fireball1 = int(0.05 * seconds)
            self.fire1 = damage
            self.burned_counter = 3
        if specialty == "fire2":
            self.fireball2 = int(2.9 * seconds)
            self.fire_radius = self.initial_fire_radius * 2
            self.fire2 = damage
            self.burned_counter = 3
        if specialty == "poison1":
            self.poison1 = damage
            self.poison_charges = 5
        if specialty == "poison2":
            self.poison2 = damage
            self.poison_charges = 5
        if specialty == "dark1":
            self.take_damage(damage)
            self.take_damage(damage, True)
        if specialty == "dark2":
            self.take_damage(damage, True)


class Spider(Orc):
    """Spider enemy class, low health, no armor

    Attributes and Methods:
        See parent class, Orc, for details
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = spider_list[0][0]
        self.image_width = 30
        self.image_height = 30
        self.frames_to_picswap = 6
        # Damage locations
        self.ice_loc = ((-25, 0), (-25, 0), (-25, -5),
                        (-25, 0), (-25, 0))
        self.fire_loc = (-20, -45)
        self.poison_loc = ((-30, -60), (-54, -60), (-60, -36),
                           (-54, -6), (-30, -3))
        self.stun_loc = ((-14, -38), (-14, -38), (-14, -38),
                         (-14, -38), (-14, -38))
        # hp manipulation
        self.max_hp = 100
        self.hp = 100
        self.armor = 0
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 8
        self.points = self.cash // 3
        self.dead_image = spiderdead
        self.death_sound = spider_death_sound

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = spider_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(spider_list[0]) - 1:
            self.frame = 0


class Wolf(Orc):
    """Wolf enemy class, medium health, low armor, fast-moving

    Attributes and Methods:
        See parent class, Orc, for details
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = wolf_list[0][0]
        self.image_width = 50
        self.image_height = 50
        self.frames_to_picswap = 10
        # Damage locations
        self.ice_loc = ((-18, 15), (-18, 10), (-18, -10),
                        (-18, 10), (-18, 3))
        self.poison_loc = ((-20, -45), (-40, -40), (-51, -44),
                           (-45, -9), (-23, -3))
        self.stun_loc = ((-5, -40), (-5, -40), (-5, -40),
                         (-5, -40), (-5, -50))
        # hp manipulation
        self.max_hp = 240
        self.hp = 240
        self.armor = 20
        # Position and movement
        self.base_speed = 2
        self.speed = self.base_speed
        # Death
        self.cash = 50
        self.points = self.cash // 3
        self.dead_image = wolfdead
        self.death_sound = wolf_death_sound

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = wolf_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(wolf_list[0]) - 1:
            self.frame = 0


class Turtle(Orc):
    """Turtle (spiker) enemy class, low health, high armor, slow

    Attributes and Methods:
        See parent class, Orc, for details
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = turtle_list[0][0]
        self.image_width = 44
        self.image_height = 44
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-22, 10), (-22, 10), (-25, 10),
                        (-22, 10), (-22, 12))
        self.poison_loc = ((-27, -60), (-52, -52), (-65, -35),
                           (-45, -9), (-27, 5))
        self.stun_loc = ((-10, -45), (-10, -40), (-10, -45),
                         (-10, -45), (-10, -45))
        # hp manipulation
        self.max_hp = 200
        self.hp = 200
        self.armor = 90
        # Position and movement
        self.base_speed = .8
        self.speed = self.base_speed
        # Death
        self.cash = 75
        self.points = self.cash // 3
        self.dead_image = turtledead
        self.death_sound = turtle_death_sound

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = turtle_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(turtle_list[0]) - 1:
            self.frame = 0


class Lizard(Orc):
    """Lizard enemy class, medium health, medium armor

    Attributes and Methods:
        See parent class, Orc, for details
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = lizard_list[0][0]
        self.image_width = 60
        self.image_height = 60
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-25, 10), (-25, 10), (-25, 5),
                        (-22, 10), (-30, 10))
        self.poison_loc = ((-40, -80), (-52, -52), (-80, -40),
                           (-65, -5), (-30, 5))
        self.stun_loc = ((-15, -60), (-15, -60), (-10, -55),
                         (-15, -65), (-15, -60))
        self.fire_loc = (-20, -65)

        # hp manipulation
        self.max_hp = 300
        self.hp = 300
        self.armor = 50
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 50
        self.points = self.cash // 3
        self.dead_image = lizarddead
        self.death_sound = lizard_death_sound

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = lizard_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(lizard_list[0]) - 1:
            self.frame = 0


class Dragon(Orc):
    """Dragon enemy class (boss), high health, high armor, slow

    Attributes and Methods:
        See parent class, Orc, for details
    """
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = dragon_list[0][0]
        self.image_width = 150
        self.image_height = 150
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-5, 30), (-22, 10), (-25, 10),
                        (-22, 10), (-5, 30))
        self.poison_loc = ((-15, -80), (-52, -52), (-65, -60),
                           (-65, -20), (-15, 15))
        self.stun_loc = ((10, -75), (30, -70), (30, -85),
                         (30, -85), (0, -95))
        self.fire_loc = (0, -100)

        # hp manipulation
        self.max_hp = 2000
        self.hp = 2000
        self.armor = 75
        # Position and movement
        self.base_speed = .6
        self.speed = self.base_speed
        # Death
        self.cash = 750
        self.points = self.cash // 3
        self.dead_image = dragondead
        self.death_sound = dragon_death_sound

    def walk(self):
        """Changes image (in direction) as enemy moves to animate movement"""
        self.image = dragon_list[self.direction_index][self.frame]
        self.frame += 1
        if self.frame > len(dragon_list[0]) - 1:
            self.frame = 0


class Mage:
    """Hero that runs scripted series of events to end the game (not enemy)

    Attributes:
        # Animation
        image (loaded Pygame image): The mage image displayed
        frame_counter (int): counts down, at zero changes image
        frame (int): Index of current image frame in list of images
        image_width (int): Width of image
        image_height (int): Height of image
        frames_to_picswap (int): Frames until image change

        # Position
        x, y (tuple, int): Gives location of mage
        end_x, end_y (tuple, int): location mage runs to

        # Spell
        start_spell (bool): When True starts mage spell movement animation
        spell_cast (bool): When True starts spell animation and sound
        radius: radius of explosion spell (expands out from mage)
        thickness (int): thickness of the circles expanding outward from mage

        # Win
        stop_spawn (bool): Used to stop the spawning of enemies
        pop_enemies_counter (int): Counter that counts down, used to pop
                                   enemies from the enemies_list, endgame
        win (bool): When declared, the game will end and go to end_screen

        # Walking
        walking (bool): Mage walks down while True

        # Speech
        wait (bool): If True mage waits, does nothing
        speech1 (bool): While True, mage gives his first speech
        speech2 (bool): While True, mage gives his second speech
        wait_counter (int): While counting down to 0, mage stands still
        speech_timer (int): Number of game frames (time) for one chat bubble
        speech_counter (int): Counts down from speech_timer to 0
        speech_index (int): Index for which text from speech to display
        font: Font used in speech chat bubble
        crystal_show (bool): While True, animates mage pulling out crystal
        crystal_away (bool): While True, animates mage putting back crystal

    Methods:
        draw: Goes through a series of pre-planned animations, sounds,
         and texts, that result in the mage killing all living enemies,
         stopping spawn of future enemies, and ending the game in victory.
    """
    def __init__(self):
        # Animation
        self.image = magestanding
        self.frame_counter = 0
        self.frame = 0
        self.image_width = 60
        self.image_height = 60
        self.frames_to_picswap = 4

        # Position
        self.x, self.y = (340, -65)
        self.end_x, self.end_y = (340, 75)

        # Spell
        self.start_spell = False
        self.spell_cast = False
        self.radius = 0
        self.thickness = 10

        # Win
        self.stop_spawn = False
        self.pop_enemies_counter = 3 * seconds
        self.win = False

        # Walking
        self.walking = False

        # Speech
        self.wait = False
        self.speech1 = False
        self.speech2 = False
        self.wait_counter = 1 * seconds
        self.speech_timer = 3.5 * seconds
        self.speech_counter = self.speech_timer
        self.speech_index = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 16, bold=True)
        self.crystal_show = False
        self.crystal_away = False

    def draw(self, game_frames):
        # Sequence takes ~ 40 seconds until all enemies dead
        if game_frames == int(6.74 * minutes):
            self.walking = True
        if game_frames > int(6.74 * minutes):
            gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                          self.y - self.image_height // 2))

        # Walk south
        if self.walking:
            # Animation
            if self.frame_counter > 0:
                self.frame_counter -= 1
            else:
                self.image = mage_list[0][self.frame]
                self.frame += 1
                if self.frame > len(mage_list[0]) - 1:
                    self.frame = 0
                self.frame_counter = self.frames_to_picswap

            # Motion
            if self.y < self.end_y:
                self.y += 1
            else:

                self.walking = False
                self.wait = True
                self.image = magestanding

        if self.wait:
            self.wait_counter -= 1
            if self.wait_counter == 0:
                self.wait = False
                self.speech1 = True
                self.frame = 0

        if self.speech1:
            if self.speech_counter > 0:
                self.speech_counter -= 1
            else:
                if self.speech_index < len(mage_speech1) - 1:
                    self.speech_index += 1
                self.speech_counter = self.speech_timer
            if self.speech_index == 3 and self.speech_counter == 0.5 * seconds:
                self.crystal_show = True
            if self.speech_index == 7 and self.speech_counter == 2 * seconds:
                grumbling_sound.play()
            if self.speech_index == 7 and self.speech_counter == 0:
                self.crystal_away = True
            if self.speech_index == 9 and self.speech_counter == 3.25 * seconds:
                pygame.mixer.music.fadeout(2500)
            if self.speech_index == 9 and self.speech_counter == 0:
                self.speech1 = False
                self.start_spell = True
                self.frame = 0

            # White talking bubble
            pygame.draw.polygon(gameDisplay, white, (
                (self.x + 5, self.y - 15), (380, 5),
                (420, 5), (420, 57), (410, 15), (380, 15)))
            pygame.draw.rect(gameDisplay, white,
                             (420, 5, 250, 52))
            # Text
            helpers.blit_text(gameDisplay, mage_speech1[self.speech_index],
                              (425, 6), self.font, margin=190)

            if self.crystal_show:
                if self.frame_counter > 0:
                    self.frame_counter -= 1
                else:
                    self.image = mage_list[1][self.frame]
                    self.frame += 1
                    self.frame_counter = self.frames_to_picswap
                    if self.frame > 6:
                        self.crystal_show = False

            if self.crystal_away:
                if self.frame_counter > 0:
                    self.frame_counter -= 1
                else:
                    self.image = mage_list[1][self.frame]
                    self.frame += 1
                    self.frame_counter = self.frames_to_picswap
                    if self.frame > 18:
                        self.crystal_away = False
                        self.image = magestanding

        if self.start_spell:
            if self.frame_counter > 0:
                self.frame_counter -= 1
            else:
                if self.frame < len(mage_list[2]) - 1:
                    self.frame += 1
                self.frame_counter = self.frames_to_picswap
            self.image = mage_list[2][self.frame]
            if self.image == mage_list[2][5] and self.frame_counter == 1:
                mage_spell_sound.play()
            if self.image == mage_list[2][10]:
                pygame.mixer.music.load('music/Fall_of_the_Solar_King2.wav')
                pygame.mixer.music.play()
                self.stop_spawn = True
                self.spell_cast = True
                self.start_spell = False

        if self.radius < 1000 and self.spell_cast:
            self.radius += 10
            # Draw the expanding spell (4 circles of increasing thickness)
            # thickness = 0
            if self.radius > self.thickness:
                pygame.draw.circle(gameDisplay, blue, (self.x, self.y),
                                   self.radius, self.thickness)
            # thickness = 1
            if self.radius - self.thickness > self.thickness * 2:
                pygame.draw.circle(
                    gameDisplay, bright_blue, (self.x, self.y),
                    self.radius-self.thickness, self.thickness * 2)
            # thickness = 1 + 2 = 3
            if self.radius - self.thickness * 3 > self.thickness * 3:
                pygame.draw.circle(
                    gameDisplay, teal, (self.x, self.y),
                    self.radius - self.thickness * 3, self.thickness * 3)
            # thickness = 1 + 2 + 3 = 6
            if self.radius - self.thickness * 6 > self.thickness * 6:
                pygame.draw.circle(
                    gameDisplay, bright_teal, (self.x, self.y),
                    self.radius - self.thickness * 6, self.thickness * 6)
        if self.radius >= 1000:
            self.spell_cast = False
            self.speech2 = True
            self.speech_counter = self.speech_timer
            self.speech_index = 0
            self.radius = 0
            self.image = magestanding

        if self.stop_spawn and self.pop_enemies_counter > 0:
            self.pop_enemies_counter -= 1

        if self.speech2:
            if self.speech_counter > 0:
                self.speech_counter -= 1
            else:
                if self.speech_index < len(mage_speech2) - 1:
                    self.speech_index += 1
                self.speech_counter = self.speech_timer

            if self.speech_index == 9 and self.speech_counter == 1:
                self.win = True

            # White talking bubble
            pygame.draw.polygon(gameDisplay, white, (
                (self.x + 5, self.y - 15), (380, 5),
                (420, 5), (420, 57), (410, 15), (380, 15)))
            pygame.draw.rect(gameDisplay, white,
                             (420, 5, 250, 52))
            # Text
            helpers.blit_text(gameDisplay, mage_speech2[self.speech_index],
                              (425, 6), self.font, margin=190)
