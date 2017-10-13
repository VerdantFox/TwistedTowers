import pygame
from lists import *
from gameParameters import gameDisplay
from pics import basic_enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=1, slow=1, frames_to_picswap=10,
                 location=(path_nodes[0][0], path_nodes[0][1])):
        pygame.sprite.Sprite.__init__(self)
        self.image = basic_enemy[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed  # Max speed wiggle-room = 10
        self.slow = slow
        self.next_node = path_nodes[0]  # see lists.py
        self.node = 0
        self.frames_to_picswap = frames_to_picswap
        self.frame_counter = 0

    def move(self):
        # Move towards node by self.speed (divisible by 1, 2, 3)
        if self.rect.left < self.next_node[0]:
            self.rect.left += self.speed
        if self.rect.left > self.next_node[0]:
            self.rect.left -= self.speed
        if self.rect.top < self.next_node[1]:
            self.rect.top += self.speed
        if self.rect.top > self.next_node[1]:
            self.rect.top -= self.speed

        # Switch to next node in path if at current node goal
        # if (self.rect.left, self.rect.top) == self.next_node:
        if self.next_node[0] - 10 < self.rect.left < self.next_node[0] + 10:
            if self.next_node[1] - 10 < self.rect.top < self.next_node[1] + 10:
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
        Enemy.show(self)

    def show(self):
        gameDisplay.blit(self.image, (self.rect.left - 30,
                                      self.rect.top - 30))
