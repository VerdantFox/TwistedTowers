import pygame
# from generalClass import Background


# https://stackoverflow.com/questions/28005641
# /how-to-add-a-background-image-into-pygame
class Background:
    """Creates background as image_image file"""
    def __init__(self, image_file, location=(0, 0)):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# Set constants for game dimensions, background, title and icon
backgroundImage = Background('TowerpathCastle3.png')
display_width = 860
display_height = 760

gameDisplay = pygame.display.set_mode((display_width, display_height))

caption = pygame.display.set_caption('Tower Defense')
icon = pygame.display.set_icon(pygame.image.load('TowerpathCastle3.png'))

# Initialize and set clock
init = pygame.init()
clock = pygame.time.Clock()
