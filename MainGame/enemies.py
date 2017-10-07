import pygame
from enemyPath import *

# Hard-coding in parameters for our game until better plan devised
display_width = 860
display_height = 760
gameDisplay = pygame.display.set_mode((display_width, display_height))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed=1, slow=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.x_position = self.rect.left
        self.feet_y = self.rect.top
        self.speed = speed
        self.slow = slow
        self.next_node = path_nodes[0]
        self.node = 0

    def move(self):
        while True:
            # print("self.node{}".format(self.next_node))
            # print("     Feet({}, {})".format(self.x_position, self.feet_y))
            # print(self.node)
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
                    self.next_node = path_nodes[self.node]

            pygame.time.wait(self.slow)
            yield Enemy.show(self)

    def show(self):
        gameDisplay.blit(self.image, (self.x_position - 30,
                                      self.feet_y - 30))
