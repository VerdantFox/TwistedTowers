import pygame
import generalClass
from colors import *

pygame.init()
pause = False


def unpause():
    global pause
    pause = False


def pause_game():

    global pause
    pause = True
    # pygame.mixer.music.pause()
    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    unpause()
        resume_button.draw()
        pygame.display.update()


resume_button = generalClass.RectButton(
    20, 50, message="Resume", inactive_color=red,
    active_color=bright_red, action=unpause)


# def set_towers():
