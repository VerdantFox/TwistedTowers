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


# https://stackoverflow.com/questions/42014195/
# rendering-text-with-multiple-lines-in-pygame
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    word_height = 0
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
