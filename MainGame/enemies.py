import pygame
import random
from gameParameters import gameDisplay
from pics import basic_enemy
from colors import *
from lists import *


class Enemy:
    def __init__(self, respawn_wait=120, hp=30, points=1, cash= 25,
                 speed=1, slow=1, frames_to_picswap=10, location=path_nodes[0]):
        self.image, self.image_width, self.image_height = basic_enemy[0]
        self.x, self.y = location
        self.speed = speed  # Max speed wiggle-room = 10
        self.slow = slow
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0
        self.frames_to_picswap = frames_to_picswap
        self.frame_counter = 0
        self.random_counter = 0
        self.radius = 3
        self.max_hp = hp
        self.hp = self.max_hp
        self.destroy = False
        self.points = points
        self.cash = cash
        self.respawn_wait = respawn_wait
        self.respawn_timer = respawn_wait

    def move(self):

        if not self.destroy:
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
                if self.image == basic_enemy[0][0]:
                    self.image = basic_enemy[1][0]
                elif self.image == basic_enemy[1][0]:
                    self.image = basic_enemy[0][0]
                self.frame_counter = self.frames_to_picswap
            if self.frame_counter > 0:
                self.frame_counter -= 1
            pygame.time.wait(self.slow)
            self.show()

        # Switch to next node in path if at current node goal
        if self.next_node[0] - 10 < self.x < self.next_node[0] + 10:
            if self.next_node[1] - 10 < self.y < self.next_node[1] + 10:
                if self.node < 9:
                    self.node += 1
                    node_x, node_y = path_nodes[self.node]  # see lists.py
                    # Introduce some randomness to node locations
                    node_x += random.randrange(-10, 10)
                    node_y += random.randrange(-15, 15)
                    self.next_node = (node_x, node_y)  # See lists
                else:
                    self.destroy = True
                    self.x, self.y = path_nodes[0]
                    return 1

        # If enemy is dead
        if self.destroy:
            # Start respawn timer countdown
            if self.respawn_timer > 0:
                self.respawn_timer -= 1
            # If respawn timer hits 0, respawn enemy and reset timer
            elif self.respawn_timer == 0:
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

    def take_damage(self, damage):
        if self.hp > 0:
            self.hp -= damage

        if self.hp <= 0:
            self.destroy = True
            return self.points, self.cash

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
