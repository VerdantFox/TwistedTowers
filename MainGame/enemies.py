import pygame
import random
from gameParameters import gameDisplay
from pics import orc_left
from definitions import *
from lists import *


class Enemy:
    def __init__(self, respawn_wait=120, hp=30, points=1, cash=25,
                 speed=1, slow=0, frames_to_picswap=10, location=path_nodes[0]):
        self.image, self.image_width, self.image_height = orc_left[0]
        self.x, self.y = location
        self.speed = speed  # Max speed wiggle-room = 10
        self.slow_initial = slow
        self.slow = slow
        self.slow_countdown = slow
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0
        self.frames_to_picswap = frames_to_picswap
        self.frame_counter = 0
        self.radius = 5
        self.fire_radius = 20
        self.max_hp = hp
        self.hp = hp
        self.armor = 20
        self.damage_reduced = (100 - self.armor) / 100
        self.destroy = False  # Removes body until respawn timer returns to play
        self.dead = False  # Used to return cash and money
        self.points = points
        self.cash = cash
        self.respawn_wait = respawn_wait
        self.respawn_timer = respawn_wait
        # Ice specialties
        self.ice = None
        self.ice_counter = 2 * seconds
        self.ice_countdown = self.ice_counter
        # Fire specialties
        self.fire = None
        self.burned_counter = 3
        self.fire_countdown = 1 * seconds
        self.fire_lockout = 4 * seconds
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
                if self.x > self.next_node[0]:
                    self.x -= self.speed
                if self.y < self.next_node[1]:
                    self.y += self.speed
                if self.y > self.next_node[1]:
                    self.y -= self.speed

                # Running motion
                if self.frame_counter < 1:
                    if self.frame < 6:
                        self.image = orc_left[self.frame][0]
                        self.frame += 1
                        if self.frame > 5:
                            self.frame = 0
                    self.frame_counter = self.frames_to_picswap
                if self.frame_counter > 0:
                    self.frame_counter -= self.speed
                self.slow_countdown -= self.slow

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
                self.ice = None
                self.dark = None
                self.destroy = False
                self.x, self.y = path_nodes[0]
                self.node = 0
                self.next_node = path_nodes[0]
                self.hp = self.max_hp
                self.respawn_timer = self.respawn_wait

    def show(self):
        gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                      self.y - self.image_height // 2))
        self.health_bar()

    def take_damage(self, damage, armor_shred=False):
        if self.hp > 0:
            if not armor_shred:
                self.hp -= damage * self.damage_reduced
            if armor_shred:
                self.hp -= damage

        if self.hp <= 0:
            self.dead = True
            self.destroy = True

    def health_bar(self):
        max_width = 10
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
                print("Took fire damage")
                self.fire_countdown = 1 * seconds
                self.burned_counter -= 1
            else:
                self.fire_countdown -= 1
        else:
            self.fire = None

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
