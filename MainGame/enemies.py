import random

import pygame

from Enemies.orc.orcPics import orc_list
from Enemies.spider.spiderPics import spider_list
from Enemies.turtle.turtlePics import turtle_list
from Enemies.wolf.wolfPics import wolf_list
from Enemies.dragon.dragonPics import dragon_list
from Enemies.lizard.lizardPics import lizard_list
from definitions import *
from gameParameters import gameDisplay
from lists import *
from towers.towerPics import fire_pic, ice_pic, poison_list, stun_list


class Orc:
    def __init__(self):
        # Position and movement
        self.x, self.y = path_nodes[0]
        self.base_speed = 1
        self.speed = self.base_speed
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0

        # Image manipulation
        self.image = orc_list[0][0]
        self.image_width = 60
        self.image_height = 60
        self.initial_frames_to_picswap = 8
        self.frames_to_picswap = 8
        self.frame_counter = 0
        self.direction = 2

        # Interaction with other objects
        self.radius = 5
        self.fire_radius = 20

        # hp manipulation
        self.max_hp = 30
        self.hp = 30
        self.armor = 40

        # Death and destruction ;-)
        self.destroy = False  # Removes body until respawn timer returns to play
        self.dead = False  # Used to return cash and money
        self.points = 5
        self.cash = 25
        self.respawn_timer = 3 * seconds
        self.respawn_countdown = 3 * seconds
        self.lives = 3
        self.added_to_list = False

        # Ice specialties
        self.ice_loc = ((-18, 10), (-18, 10), (-18, 10),
                        (-18, 10), (-18, 3))
        self.ice = False
        self.ice_counter = 2.5 * seconds
        self.ice_countdown = self.ice_counter
        # Fire specialties
        self.fire_loc = (-10, -50)
        self.fireball = False
        self.fire = None
        self.burned_counter = 0
        self.fire_countdown = 1 * seconds
        self.fire_lockout = 3 * seconds
        # Poison specialties
        self.poison_loc = ((-27, -45), (-36, -57), (-51, -40),
                           (-45, -9), (-27, -3))
        self.stun_loc = ((-10, -40), (-5, -50), (-5, -50),
                         (-5, -50), (-10, -50))
        self.poison = None
        self.poison_tick = 0
        self.poison_countdown = 0
        self.poison_charges = 0
        self.stun = False
        self.stun_duration = 1 * seconds
        self.stun_duration_countdown = 1 * seconds
        self.stun_frameswap_rate = 10
        self.stun_frame = 0
        self.stun_framecounter = 0
        # Dark specialties
        self.dark_loc = ()
        self.dark = False
        self.dark_timer = 2 * seconds
        self.frame = 0

    def move(self):
        if not self.destroy:
            if not self.stun:
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
                    # Determine direction
                    self.direction = 2  # Default is right
                    if self.down and not self.right:
                        self.direction = 0
                    if self.down and self.right:
                        self.direction = 1
                    if self.right and not (self.up or self.down):
                        self.direction = 2
                    if self.up and self.right:
                        self.direction = 3
                    if self.up and not self.right:
                        self.direction = 4

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
            if self.ice:
                self.iced()
            if self.poison:
                self.poisoned(self.poison)
            if self.fire:
                self.burning(self.fire)
            if self.fire_lockout > 0:
                self.fire_lockout -= 1
            if self.dark:
                self.darkness(self.dark)

            self.show()

            # Switch to next node in path if at current node goal
            if self.next_node[0] - 10 < self.x < self.next_node[0] + 10:
                if self.next_node[1] - 10 < self.y < self.next_node[1] + 10:
                    if self.node < len(path_nodes) - 2:
                        self.node += 1
                        node_x, node_y = path_nodes[self.node]  # see lists.py
                        # Introduce some randomness to node locations
                        node_x += random.randrange(-10, 10)
                        node_y += random.randrange(-15, 15)
                        self.next_node = (node_x, node_y)  # See lists
                    else:
                        # Destroy and remove all affects, move to start of path
                        self.destroy = True
                        self.poison = None
                        self.poison_tick = 0
                        self.poison_countdown = 0
                        self.poison_charges = 0
                        self.ice = None
                        self.fire = None
                        self.fireball = None
                        self.dark = None
                        self.x, self.y = path_nodes[0]
                        # Return damage to castle
                        return 1

        # If enemy is dead
        if self.destroy:
            # Start respawn timer countdown
            if self.respawn_countdown > 0:
                self.respawn_countdown -= 1
            # If respawn timer reaches 0, respawn enemy and reset timer
            elif self.respawn_countdown <= 0:
                self.poison = None
                self.poison_tick = 0
                self.poison_countdown = 0
                self.poison_charges = 0
                self.fire = None
                self.fireball = None
                self.burned_counter = 0
                self.ice = None
                self.dark = None
                self.destroy = False
                self.x, self.y = path_nodes[0]
                self.node = 0
                self.next_node = path_nodes[0]
                self.hp = self.max_hp
                self.respawn_countdown = self.respawn_timer + random.randrange(
                    -2 * seconds, 2 * seconds)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def walk(self):
        # Change walking frame in direction
        self.image = orc_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(orc_list[0]) - 1:
            self.frame = 0

    def show(self):
        if self.poison:
            self.show_poison()
        if self.fire:
            self.show_fire()
        if self.stun:
            self.show_stun()
        if self.ice:
            self.show_ice()

        gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                      self.y - self.image_height // 2))
        self.health_bar()

    def show_poison(self):
        gameDisplay.blit(
            poison_list[self.direction][0],
            (self.x + self.poison_loc[self.direction][0],
             self.y + self.poison_loc[self.direction][1]))

    def show_stun(self):
        gameDisplay.blit(
            stun_list[self.stun_frame][0],
            (self.x + self.stun_loc[self.direction][0],
             self.y + self.stun_loc[self.direction][1]))

        self.stun_framecounter -= 1
        if self.stun_framecounter < 1:
            self.stun_framecounter = self.stun_frameswap_rate
            self.stun_frame += 1
            if self.stun_frame == len(stun_list[0]):
                self.stun_frame = 0

    def show_fire(self):
        gameDisplay.blit(
            fire_pic[0], (self.x + self.fire_loc[0],
                          self.y + self.fire_loc[1]))

    def show_ice(self):
        gameDisplay.blit(
            ice_pic[0], (self.x + self.ice_loc[self.direction][0],
                         self.y + self.ice_loc[self.direction][1]))

    def take_damage(self, damage, armor_shred=False):
        if self.hp > 0:
            damage_reduced = (100 - self.armor) / 100
            if not armor_shred:
                self.hp -= damage * damage_reduced
            if armor_shred:
                self.hp -= damage

        if self.hp <= 0:
            self.dead = True
            self.destroy = True

    def health_bar(self):
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
        if self.ice_countdown > 0:
            self.speed = self.base_speed * .7
            self.frames_to_picswap = int(self.initial_frames_to_picswap * 1/.7)
            self.ice_countdown -= 1
        else:
            self.speed = self.base_speed
            self.frames_to_picswap = self.initial_frames_to_picswap
            self.ice = None
            self.ice_countdown = self.ice_counter

    def burning(self, amount):
        if self.burned_counter > 0:
            if self.fire_countdown == 0:
                self.take_damage(amount)
                self.fire_countdown = 1 * seconds
                self.burned_counter -= 1
            else:
                self.fire_countdown -= 1
        else:
            self.fire = None
            self.fireball = False

    def poisoned(self, percent_hp):
        if self.poison_charges == 1 and self.poison_tick == 2 * seconds:
            self.stun_duration_countdown = self.stun_duration
            self.stun = True
            print("stunned")

        poison_damage = percent_hp * self.hp
        if poison_damage < 1.6:
            poison_damage = 1.6  # 8 damage minimum
        if self.poison_charges > 0:
            if self.poison_tick == 0:
                self.take_damage(poison_damage, True)
                self.poison_tick = 2 * seconds
                self.poison_charges -= 1
            else:
                self.poison_tick -= 1
        else:
            self.poison = False

    def darkness(self, damage):
        self.take_damage(damage, True)
        self.dark = False

    def check_death(self):
        if self.dead:
            self.lives -= 1
            self.dead = False
            return self.points, self.cash
        else:
            return None


class Spider(Orc):
    def __init__(self):
        super().__init__()
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
        self.max_hp = 10
        self.hp = 10
        self.armor = 0
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 5

    def walk(self):
        # Change walking frame in direction
        self.image = spider_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(spider_list[0]) - 1:
            self.frame = 0


class Wolf(Orc):
    def __init__(self):
        super().__init__()
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
        self.max_hp = 30
        self.hp = 30
        self.armor = 25
        # Position and movement
        self.base_speed = 2
        self.speed = self.base_speed
        # Death
        self.cash = 25

    def walk(self):
        # Change walking frame in direction
        self.image = wolf_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(wolf_list[0]) - 1:
            self.frame = 0


class Turtle(Orc):
    def __init__(self):
        super().__init__()
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
        self.max_hp = 30
        self.hp = 30
        self.armor = 80
        # Position and movement
        self.base_speed = .8
        self.speed = self.base_speed
        # Death
        self.cash = 25

    def walk(self):
        # Change walking frame in direction
        self.image = turtle_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(turtle_list[0]) - 1:
            self.frame = 0


class Dragon(Orc):
    def __init__(self):
        super().__init__()
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
        self.max_hp = 300
        self.hp = 300
        self.armor = 90
        # Position and movement
        self.base_speed = 1
        self.speed = self.base_speed
        # Death
        self.cash = 25

    def walk(self):
        # Change walking frame in direction
        self.image = dragon_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(dragon_list[0]) - 1:
            self.frame = 0


class Lizard(Orc):
    def __init__(self):
        super().__init__()
        # Image manipulation
        self.image = lizard_list[0][0]
        self.image_width = 80
        self.image_height = 80
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-35, 10), (-35, 10), (-35, 0),
                        (-22, 10), (-30, 10))
        self.poison_loc = ((-40, -80), (-52, -52), (-80, -50),
                           (-65, -20), (-35, 5))
        self.stun_loc = ((-15, -60), (-15, -60), (-10, -55),
                         (-15, -65), (-15, -60))
        self.fire_loc = (-20, -65)

        # hp manipulation
        self.max_hp = 40
        self.hp = 40
        self.armor = 90
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 25

    def walk(self):
        # Change walking frame in direction
        self.image = lizard_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(lizard_list[0]) - 1:
            self.frame = 0
