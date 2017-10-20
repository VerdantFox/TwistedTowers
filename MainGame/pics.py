import pygame


basicTower1 = pygame.image.load('3DBasicTower3.png'), 50, 80

fire_pic = pygame.image.load('Enemies/effects/fire40.png'), 32, 40
ice_pic = pygame.image.load('Enemies/effects/ice50.png'), 50, 20
poison_pic = pygame.image.load('Enemies/effects/poisoncloud60.png'), 60, 24

# Orc down
orcdown1 = pygame.image.load('Enemies/orc/sionDOWN1.png'), 60, 60
orcdown2 = pygame.image.load('Enemies/orc/sionDOWN2.png'), 60, 60
orcdown3 = pygame.image.load('Enemies/orc/sionDOWN3.png'), 60, 60
orcdown4 = pygame.image.load('Enemies/orc/sionDOWN4.png'), 60, 60
orcdown5 = pygame.image.load('Enemies/orc/sionDOWN5.png'), 60, 60
orcdown6 = pygame.image.load('Enemies/orc/sionDOWN6.png'), 60, 60
orcdown7 = pygame.image.load('Enemies/orc/sionDOWN7.png'), 60, 60
orcdown8 = pygame.image.load('Enemies/orc/sionDOWN8.png'), 60, 60
orcdown9 = pygame.image.load('Enemies/orc/sionDOWN9.png'), 60, 60

# orc down_right
orcdownright1 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT1.png'), 60, 60
orcdownright2 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT2.png'), 60, 60
orcdownright3 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT3.png'), 60, 60
orcdownright4 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT4.png'), 60, 60
orcdownright5 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT5.png'), 60, 60
orcdownright6 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT6.png'), 60, 60
orcdownright7 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT7.png'), 60, 60
orcdownright8 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT8.png'), 60, 60
orcdownright9 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT9.png'), 60, 60

# orc right
orcright1 = pygame.image.load('Enemies/orc/sionRIGHT1.png'), 60, 60
orcright2 = pygame.image.load('Enemies/orc/sionRIGHT2.png'), 60, 60
orcright3 = pygame.image.load('Enemies/orc/sionRIGHT3.png'), 60, 60
orcright4 = pygame.image.load('Enemies/orc/sionRIGHT4.png'), 60, 60
orcright5 = pygame.image.load('Enemies/orc/sionRIGHT5.png'), 60, 60
orcright6 = pygame.image.load('Enemies/orc/sionRIGHT6.png'), 60, 60
orcright7 = pygame.image.load('Enemies/orc/sionRIGHT7.png'), 60, 60
orcright8 = pygame.image.load('Enemies/orc/sionRIGHT8.png'), 60, 60
orcright9 = pygame.image.load('Enemies/orc/sionRIGHT9.png'), 60, 60

# orc up_right
orcupright1 = pygame.image.load('Enemies/orc/sionUP_RIGHT1.png'), 60, 60
orcupright2 = pygame.image.load('Enemies/orc/sionUP_RIGHT2.png'), 60, 60
orcupright3 = pygame.image.load('Enemies/orc/sionUP_RIGHT3.png'), 60, 60
orcupright4 = pygame.image.load('Enemies/orc/sionUP_RIGHT4.png'), 60, 60
orcupright5 = pygame.image.load('Enemies/orc/sionUP_RIGHT5.png'), 60, 60
orcupright6 = pygame.image.load('Enemies/orc/sionUP_RIGHT6.png'), 60, 60
orcupright7 = pygame.image.load('Enemies/orc/sionUP_RIGHT7.png'), 60, 60
orcupright8 = pygame.image.load('Enemies/orc/sionUP_RIGHT8.png'), 60, 60
orcupright9 = pygame.image.load('Enemies/orc/sionUP_RIGHT9.png'), 60, 60

# orc up
orcup1 = pygame.image.load('Enemies/orc/sionUP1.png'), 60, 60
orcup2 = pygame.image.load('Enemies/orc/sionUP2.png'), 60, 60
orcup3 = pygame.image.load('Enemies/orc/sionUP3.png'), 60, 60
orcup4 = pygame.image.load('Enemies/orc/sionUP4.png'), 60, 60
orcup5 = pygame.image.load('Enemies/orc/sionUP5.png'), 60, 60
orcup6 = pygame.image.load('Enemies/orc/sionUP6.png'), 60, 60
orcup7 = pygame.image.load('Enemies/orc/sionUP7.png'), 60, 60
orcup8 = pygame.image.load('Enemies/orc/sionUP8.png'), 60, 60
orcup9 = pygame.image.load('Enemies/orc/sionUP9.png'), 60, 60

orc_list = [
    # down = 0
    [orcdown1, orcdown2, orcdown3, orcdown4, orcdown5,
     orcdown6, orcdown7, orcdown8, orcdown9],
    # down right = 1
    [orcdownright1, orcdownright2, orcdownright3, orcdownright4, orcdownright5,
     orcdownright6, orcdownright7, orcdownright8, orcdownright9],
    # right = 2
    [orcright1, orcright2, orcright3, orcright4, orcright5,
     orcright6, orcright7, orcright8, orcright9],
    # up right = 3
    [orcupright1, orcupright2, orcupright3, orcupright4, orcupright5,
     orcupright6, orcupright7, orcupright8, orcupright9],
    # up = 4
    [orcup1, orcup2, orcup3, orcup4, orcup5,
     orcup6, orcup7, orcup8, orcup9]
]
