import pygame
from lists import *
from gameParameters import gameDisplay
from pics import basic_enemy
import random


class Enemy:
    def __init__(self, respawn_wait=120, hp=30, points=1, speed=1, slow=1,
                 frames_to_picswap=10, location=path_nodes[0]):
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
        self.radius = 3
        self.initial_hp = hp
        self.hp = self.initial_hp
        self.destroy = False
        self.points = points
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
                if self.image == basic_enemy[0]:
                    self.image = basic_enemy[1]
                elif self.image == basic_enemy[1]:
                    self.image = basic_enemy[0]
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
                    if self.node < 8:
                        # Introduce some randomness to node locations
                        node_x += random.randrange(-10, 10)
                        node_y += random.randrange(-15, 15)
                    self.next_node = (node_x, node_y)  # See lists

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
                self.hp = self.initial_hp
                self.respawn_timer = self.respawn_wait

    def show(self):
        gameDisplay.blit(self.image, (self.x - 30, self.y - 30))

    def take_damage(self, damage):
        if self.hp > 0:
            self.hp -= damage

        if self.hp <= 0:
            score = self.dead()
            return score

    def dead(self):
        self.destroy = True
        return self.points
