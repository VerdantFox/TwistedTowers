import pygame
from generalClass import Background

# Set constants for game dimensions, background, title and icon
backgroundImage = Background('TowerpathCastle3.png')
display_width = 860
display_height = 760

gameDisplay = pygame.display.set_mode((display_width, display_height))

caption = pygame.display.set_caption('Tower Defense')
icon = pygame.display.set_icon(pygame.image.load('TowerpathCastle3.png'))
