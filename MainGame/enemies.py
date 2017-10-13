import pygame
from lists import *
from gameParameters import gameDisplay
from pics import basic_enemy
import random


class Enemy:
    def __init__(self, speed=1, slow=1, frames_to_picswap=10,
                 location=(path_nodes[0][0], path_nodes[0][1])):
        self.image = basic_enemy[0]
        # self.rect = self.image.get_rect()
        self.x, self.y = location
        self.speed = speed  # Max speed wiggle-room = 10
        self.slow = slow
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0
        self.frames_to_picswap = frames_to_picswap
        self.frame_counter = 0
        self.random_counter = 0
        self.radius = 4

    def move(self):

        # Move towards node by self.speed.
        if self.x < self.next_node[0]:
            self.x += self.speed
        if self.x > self.next_node[0]:
            self.x -= self.speed
        if self.y < self.next_node[1]:
            self.y += self.speed
        if self.y > self.next_node[1]:
            self.y -= self.speed

        # Switch to next node in path if at current node goal
        if self.next_node[0] - 10 < self.x < self.next_node[0] + 10:
            if self.next_node[1] - 10 < self.y < self.next_node[1] + 10:
                if self.node < 9:
                    self.node += 1
                    node_x, node_y = path_nodes[self.node]  # see lists.py
                    if self.node < 8:
                        # Introduce some randomness to node locations
                        node_x += random.randrange(-10, 10)
                        node_y += random.randrange(-15, 15)
                    self.next_node = (node_x, node_y)  # See lists

        # Running motion
        if self.frame_counter < 1:
            if self.image == basic_enemy[0]:
                self.image = basic_enemy[1]
            elif self.image == basic_enemy[1]:
                self.image = basic_enemy[0]
            self.frame_counter = self.frames_to_picswap

        self.frame_counter -= 1
        pygame.time.wait(self.slow)
        Enemy.show(self)

    def show(self):
        gameDisplay.blit(self.image, (self.x - 30,
                                      self.y - 30))
