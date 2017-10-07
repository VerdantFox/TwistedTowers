import pygame

# Hard-coding in parameters for our game until better plan devised
display_width = 850
display_height = 650
gameDisplay = pygame.display.set_mode((display_width, display_height))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed=1, slow=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.feet_x = self.rect.left + 15
        self.feet_y = self.rect.top - 30
        self.speed = speed
        self.slow = slow

    def move(self):
        self.feet_x += self.speed
        pygame.time.wait(self.slow)

    def show(self):
        gameDisplay.blit(self.image, (self.feet_x, self.feet_y))
