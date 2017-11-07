import pygame


# Taken from pygame library and altered
def collision(object1, object2):
    """detect collision between two objects using circles

    Tests for collision between two objects by testing whether two circles
    centered on the objects overlap. Objects must have a
    a "radius" attribute, which is used to create the circle.

    Args:
        object1: First object for collision detection
        object2: Second object for collision detection

    Returns:
        bool: True if objects' circles (defined by their radius) overlap
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
def blit_text(surface, text, pos, font, color=pygame.Color('black'), margin=0):
    """Writes one or more lines of text to the game screen

    Splits words by ' ' creating a list of words split by lines. Finds the
    width of the display and writes words from a given x, y coordinate to the
    edge of display minus a specified margin, breaking to new line if edge
    reached or end character found. Then renders text as specified.

    Args:
        surface (obj): The display of your game
        text (str): The text to be displayed
        pos (tuple, int): The x, y coordinates text should start at
        font (obj): Pygame font object (takes font, font-size, bold)
        color (tuple, int): Color of the text to be displayed
        margin (int): Distance from screen's end to start text-wrapping
    """
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
            if x + word_width >= max_width - margin:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
