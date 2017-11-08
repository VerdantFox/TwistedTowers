import pygame

# Credit all images to Riot Games, League of Legends
# https://na.leagueoflegends.com/en/

# Wolf dead
wolfdead = pygame.image.load('Enemies/wolf/wwDEAD.png')

# wolf down
wolfdown1 = pygame.image.load('Enemies/wolf/wwDOWN1.png')
wolfdown2 = pygame.image.load('Enemies/wolf/wwDOWN2.png')
wolfdown3 = pygame.image.load('Enemies/wolf/wwDOWN3.png')
wolfdown4 = pygame.image.load('Enemies/wolf/wwDOWN4.png')
wolfdown5 = pygame.image.load('Enemies/wolf/wwDOWN5.png')
wolfdown6 = pygame.image.load('Enemies/wolf/wwDOWN6.png')
wolfdown7 = pygame.image.load('Enemies/wolf/wwDOWN7.png')
wolfdown8 = pygame.image.load('Enemies/wolf/wwDOWN8.png')

# wolf down_right
wolfdownright1 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT1.png')
wolfdownright2 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT2.png')
wolfdownright3 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT3.png')
wolfdownright4 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT4.png')
wolfdownright5 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT5.png')
wolfdownright6 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT6.png')
wolfdownright7 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT7.png')
wolfdownright8 = pygame.image.load('Enemies/wolf/wwDOWN_RIGHT8.png')

# wolf right
wolfright1 = pygame.image.load('Enemies/wolf/wwRIGHT1.png')
wolfright2 = pygame.image.load('Enemies/wolf/wwRIGHT2.png')
wolfright3 = pygame.image.load('Enemies/wolf/wwRIGHT3.png')
wolfright4 = pygame.image.load('Enemies/wolf/wwRIGHT4.png')
wolfright5 = pygame.image.load('Enemies/wolf/wwRIGHT5.png')
wolfright6 = pygame.image.load('Enemies/wolf/wwRIGHT6.png')
wolfright7 = pygame.image.load('Enemies/wolf/wwRIGHT7.png')
wolfright8 = pygame.image.load('Enemies/wolf/wwRIGHT8.png')

# wolf up_right
wolfupright1 = pygame.image.load('Enemies/wolf/wwUP_RIGHT1.png')
wolfupright2 = pygame.image.load('Enemies/wolf/wwUP_RIGHT2.png')
wolfupright3 = pygame.image.load('Enemies/wolf/wwUP_RIGHT3.png')
wolfupright4 = pygame.image.load('Enemies/wolf/wwUP_RIGHT4.png')
wolfupright5 = pygame.image.load('Enemies/wolf/wwUP_RIGHT5.png')
wolfupright6 = pygame.image.load('Enemies/wolf/wwUP_RIGHT6.png')
wolfupright7 = pygame.image.load('Enemies/wolf/wwUP_RIGHT7.png')
wolfupright8 = pygame.image.load('Enemies/wolf/wwUP_RIGHT8.png')

# wolf up
wolfup1 = pygame.image.load('Enemies/wolf/wwUP1.png')
wolfup2 = pygame.image.load('Enemies/wolf/wwUP2.png')
wolfup3 = pygame.image.load('Enemies/wolf/wwUP3.png')
wolfup4 = pygame.image.load('Enemies/wolf/wwUP4.png')
wolfup5 = pygame.image.load('Enemies/wolf/wwUP5.png')
wolfup6 = pygame.image.load('Enemies/wolf/wwUP6.png')
wolfup7 = pygame.image.load('Enemies/wolf/wwUP7.png')
wolfup8 = pygame.image.load('Enemies/wolf/wwUP8.png')

wolf_list = [
    # down = 0
    [wolfdown1, wolfdown2, wolfdown3, wolfdown4, wolfdown5,
     wolfdown6, wolfdown7, wolfdown8],
    # down right = 1
    [wolfdownright1, wolfdownright2, wolfdownright3, wolfdownright4,
     wolfdownright5, wolfdownright6, wolfdownright7, wolfdownright8],
    # right = 2
    [wolfright1, wolfright2, wolfright3, wolfright4, wolfright5,
     wolfright6, wolfright7, wolfright8],
    # up right = 3
    [wolfupright1, wolfupright2, wolfupright3, wolfupright4,
     wolfupright5, wolfupright6, wolfupright7, wolfupright8],
    # up = 4
    [wolfup1, wolfup2, wolfup3, wolfup4, wolfup5,
     wolfup6, wolfup7, wolfup8]
]
