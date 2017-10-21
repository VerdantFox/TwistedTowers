import pygame
import random
from gameParameters import gameDisplay
from towerPics import fire_pic, ice_pic, poison_pic
from orcPics import orc_list
from spiderPics import spider_list
from definitions import *
from lists import *


class Enemy:
    def __init__(self):

        # Position and movement
        self.x, self.y = path_nodes[0]
        self.speed = 1  # Max speed wiggle-room = 10
        self.slow_initial = 0
        self.slow = 0
        self.slow_countdown = 0
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
        self.frames_to_picswap = 10
        self.frame_counter = 0

        # Interaction with other objects
        self.radius = 5
        self.fire_radius = 20

        # hp manipulation
        self.max_hp = 30
        self.hp = 30
        self.armor = 30

        # Death and destruction ;-)
        self.destroy = False  # Removes body until respawn timer returns to play
        self.dead = False  # Used to return cash and money
        self.points = 5
        self.cash = 25
        self.respawn_wait = 120
        self.respawn_timer = 120

        # Ice specialties
        self.ice = None
        self.ice_counter = 2 * seconds
        self.ice_countdown = self.ice_counter
        # Fire specialties
        self.fireball = False
        self.fire = None
        self.burned_counter = 0
        self.fire_countdown = 1 * seconds
        self.fire_lockout = 3 * seconds
        # Poison specialties
        self.poison = None
        self.poison_tick = 0
        self.poison_countdown = 0
        # Dark specialties
        self.dark = False
        self.dark_timer = 2 * seconds
        self.frame = 0

    def move(self):
        if not self.destroy:
            # Move only if slow_countdown greater than 0
            if self.slow_countdown > 0:
                # Move towards node by self.speed.
                if self.x < self.next_node[0]:
                    self.x += self.speed
                    self.right = True
                if self.x > self.next_node[0]:
                    self.x -= self.speed
                    self.left = True
                if self.y < self.next_node[1]:
                    self.y += self.speed
                    self.down = True
                if self.y > self.next_node[1]:
                    self.y -= self.speed
                    self.up = True

                # Change walking frame if frame_counter reaches 0
                if self.frame_counter < 1:
                    # Determine direction
                    direction = 2  # Default is right
                    if self.down and not self.right:
                        direction = 0
                    if self.down and self.right:
                        direction = 1
                    if self.right and not (self.up or self.down):
                        direction = 2
                    if self.up and self.right:
                        direction = 3
                    if self.up and not self.right:
                        direction = 4

                    self.walk(direction)
                    self.frame_counter = self.frames_to_picswap
                if self.frame_counter > 0:
                    self.frame_counter -= self.speed
                self.slow_countdown -= self.slow

                self.right = False
                self.left = False
                self.up = False
                self.down = False

            # Don't move if slow_countdown reaches zero, reset countdown
            elif self.slow_countdown <= 0:
                self.slow_countdown = 60

            # Check for special attributes
            if self.ice:
                self.iced(self.ice)
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
            if self.respawn_timer > 0:
                self.respawn_timer -= 1
            # If respawn timer reaches 0, respawn enemy and reset timer
            elif self.respawn_timer == 0:
                self.poison = None
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
                self.respawn_timer = self.respawn_wait

    def walk(self, direction):
        # Change walking frame in direction
        self.image = orc_list[direction][self.frame]
        self.frame += 1
        if self.frame > len(orc_list[0]) - 1:
            self.frame = 0

    def show(self):
        if self.poison:
            gameDisplay.blit(
                poison_pic[0], (self.x - poison_pic[1]*3/4,
                                self.y - 20))
        if self.fire:
            gameDisplay.blit(
                fire_pic[0], (self.x, self.y - self.image_height // 2 - 20))
        if self.ice:
            gameDisplay.blit(
                ice_pic[0], (self.x, self.y))
        gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                      self.y - self.image_height // 2))
        self.health_bar()

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

    def iced(self, amount):
        if self.ice_countdown > 0:
            self.slow = self.slow_initial + amount
            self.ice_countdown -= 1
        else:
            self.slow = self.slow_initial
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

    def poisoned(self, damage_tick):
        if self.poison_tick == 0:
            self.take_damage(damage_tick, True)
            self.poison_tick = 5 * seconds
        else:
            self.poison_tick -= 1

    def darkness(self, damage):
        self.take_damage(damage, True)
        self.dark = False

    def check_death(self):
        if self.dead:
            self.dead = False
            return self.points, self.cash
        else:
            return None


class Spider(Enemy):
    def __init__(self):
        super().__init__()
        # Image manipulation
        self.image = spider_list[0][0]
        self.image_width = 30
        self.image_height = 30
        self.frames_to_picswap = 8
        # hp manipulation
        self.max_hp = 10
        self.hp = 10
        self.armor = 0

    def walk(self, direction):
        # Change walking frame in direction
        self.image = spider_list[direction][self.frame]
        self.frame += 1
        if self.frame > len(spider_list[0]) - 1:
            self.frame = 0
