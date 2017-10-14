import pygame
import generalClass
from definitions import *

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


resume_button = generalClass.Button(
    (20, 80), message="Resume", color1=red,
    color2=bright_red, action=unpause)


# Taken from pygame and altered
def collision(object1, object2):
    """detect collision between two objects using circles

    collide_circle(left, right): return bool

    Tests for collision between two objects by testing whether two circles
    centered on the objects overlap. Objects must have a
    a "radius" attribute, which is used to create the circle.
    """

    x_distance = object1.x - object2.x
    y_distance = object1.y - object2.y
    distance_squared = x_distance ** 2 + y_distance ** 2

    try:
        return distance_squared <= \
               (object1.fire_radius + object2.fire_radius) ** 2
    except AttributeError:
        return distance_squared <= (object1.radius + object2.radius) ** 2
