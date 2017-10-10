import pygame
from lists import *
from gameParameters import gameDisplay
from enemyPics import basic_enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=1, slow=1, frames_to_picswap=10,
                 location=(path_nodes[0][0], path_nodes[0][1])):
        pygame.sprite.Sprite.__init__(self)
        self.image = basic_enemy[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.x_position = self.rect.left
        self.feet_y = self.rect.top
        self.speed = speed  # Note: speed divisible by 1, 2, 3 (not 4)
        self.slow = slow
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0
        self.frames_to_picswap = frames_to_picswap
        self.frame_counter = 0

    def move(self):
        while True:
            # Move towards node by self.speed (divisible by 1, 2, 3)
            if self.x_position < self.next_node[0]:
                self.x_position += self.speed
            if self.x_position > self.next_node[0]:
                self.x_position -= self.speed
            if self.feet_y < self.next_node[1]:
                self.feet_y += self.speed
            if self.feet_y > self.next_node[1]:
                self.feet_y -= self.speed

            # Switch to next node in path if at current node goal
            if (self.x_position, self.feet_y) == self.next_node:
                if self.node < 9:
                    self.node += 1
                    self.next_node = path_nodes[self.node]  # See lists

            # Running motion
            if self.frame_counter < 1:
                if self.image == basic_enemy[0]:
                    self.image = basic_enemy[1]
                elif self.image == basic_enemy[1]:
                    self.image = basic_enemy[0]
                self.frame_counter = self.frames_to_picswap

            self.frame_counter -= 1
            pygame.time.wait(self.slow)
            yield Enemy.show(self)

    def show(self):
        gameDisplay.blit(self.image, (self.x_position - 30,
                                      self.feet_y - 30))
