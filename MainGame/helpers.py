import pygame
import generalClass
from colors import *

pygame.init()
clock = pygame.time.Clock()
pause = False


def unpause():
    global pause
    pause = False
    # pygame.mixer.music.unpause()


def pause_game():
    global pause
    pause = True
    # pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        unpause_button.draw()
        pygame.display.update()

unpause_button = generalClass.RectButton(
    20, 50, message="Resume", inactive_color=red,
    active_color=bright_red, action=unpause)
