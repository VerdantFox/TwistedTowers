import pygame


basicTower1 = pygame.image.load('towers/3DBasicTower3.png'), 50, 80
iceTower1 = pygame.image.load('towers/Icetower3.png'), 50, 80
fireTower1 = pygame.image.load('towers/firewand1.png'), 50, 80
poisonTower1 = pygame.image.load('towers/planttower1.png'), 50, 80
darkTower1 = pygame.image.load('towers/darktower1.png'), 50, 80

fire_pic = pygame.image.load('Enemies/effects/fire40.png'), 32, 40
ice_pic = pygame.image.load('Enemies/effects/ice50.png'), 50, 20
poison_pic = pygame.image.load('Enemies/effects/poisoncloud60.png'), 60, 24

# Orc down
orcdown1 = pygame.image.load('Enemies/orc/sionDOWN1.png')
orcdown2 = pygame.image.load('Enemies/orc/sionDOWN2.png')
orcdown3 = pygame.image.load('Enemies/orc/sionDOWN3.png')
orcdown4 = pygame.image.load('Enemies/orc/sionDOWN4.png')
orcdown5 = pygame.image.load('Enemies/orc/sionDOWN5.png')
orcdown6 = pygame.image.load('Enemies/orc/sionDOWN6.png')
orcdown7 = pygame.image.load('Enemies/orc/sionDOWN7.png')
orcdown8 = pygame.image.load('Enemies/orc/sionDOWN8.png')
orcdown9 = pygame.image.load('Enemies/orc/sionDOWN9.png')

# orc down_right
orcdownright1 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT1.png')
orcdownright2 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT2.png')
orcdownright3 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT3.png')
orcdownright4 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT4.png')
orcdownright5 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT5.png')
orcdownright6 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT6.png')
orcdownright7 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT7.png')
orcdownright8 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT8.png')
orcdownright9 = pygame.image.load('Enemies/orc/sionDOWN_RIGHT9.png')

# orc right
orcright1 = pygame.image.load('Enemies/orc/sionRIGHT1.png')
orcright2 = pygame.image.load('Enemies/orc/sionRIGHT2.png')
orcright3 = pygame.image.load('Enemies/orc/sionRIGHT3.png')
orcright4 = pygame.image.load('Enemies/orc/sionRIGHT4.png')
orcright5 = pygame.image.load('Enemies/orc/sionRIGHT5.png')
orcright6 = pygame.image.load('Enemies/orc/sionRIGHT6.png')
orcright7 = pygame.image.load('Enemies/orc/sionRIGHT7.png')
orcright8 = pygame.image.load('Enemies/orc/sionRIGHT8.png')
orcright9 = pygame.image.load('Enemies/orc/sionRIGHT9.png')

# orc up_right
orcupright1 = pygame.image.load('Enemies/orc/sionUP_RIGHT1.png')
orcupright2 = pygame.image.load('Enemies/orc/sionUP_RIGHT2.png')
orcupright3 = pygame.image.load('Enemies/orc/sionUP_RIGHT3.png')
orcupright4 = pygame.image.load('Enemies/orc/sionUP_RIGHT4.png')
orcupright5 = pygame.image.load('Enemies/orc/sionUP_RIGHT5.png')
orcupright6 = pygame.image.load('Enemies/orc/sionUP_RIGHT6.png')
orcupright7 = pygame.image.load('Enemies/orc/sionUP_RIGHT7.png')
orcupright8 = pygame.image.load('Enemies/orc/sionUP_RIGHT8.png')
orcupright9 = pygame.image.load('Enemies/orc/sionUP_RIGHT9.png')

# orc up
orcup1 = pygame.image.load('Enemies/orc/sionUP1.png')
orcup2 = pygame.image.load('Enemies/orc/sionUP2.png')
orcup3 = pygame.image.load('Enemies/orc/sionUP3.png')
orcup4 = pygame.image.load('Enemies/orc/sionUP4.png')
orcup5 = pygame.image.load('Enemies/orc/sionUP5.png')
orcup6 = pygame.image.load('Enemies/orc/sionUP6.png')
orcup7 = pygame.image.load('Enemies/orc/sionUP7.png')
orcup8 = pygame.image.load('Enemies/orc/sionUP8.png')
orcup9 = pygame.image.load('Enemies/orc/sionUP9.png')

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
