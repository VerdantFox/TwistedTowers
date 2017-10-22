import pygame

basicTower1 = pygame.image.load('towers/3DBasicTower3.png'), 50, 80
iceTower1 = pygame.image.load('towers/Icetower3.png'), 50, 80
fireTower1 = pygame.image.load('towers/firewand1.png'), 50, 80
poisonTower1 = pygame.image.load('towers/planttower1.png'), 50, 80
darkTower1 = pygame.image.load('towers/darktower1.png'), 50, 80

fire_pic = pygame.image.load('Enemies/effects/fire40.png'), 32, 40
ice_pic = pygame.image.load('Enemies/effects/ice50.png'), 50, 20
poisonDown_pic = pygame.image.load(
    'Enemies/effects/poisoncloudDOWN.png'), 60, 60
poisonDownRight_pic = pygame.image.load(
    'Enemies/effects/poisoncloudDOWN_RIGHT.png'), 60, 60
poisonRight_pic = pygame.image.load(
    'Enemies/effects/poisoncloudRIGHT.png'), 60, 60
poisonUpRight_pic = pygame.image.load(
    'Enemies/effects/poisoncloudUP_RIGHT.png'), 60, 60
poisonUp_pic = pygame.image.load(
    'Enemies/effects/poisoncloudUP.png'), 60, 60

poison_list = [poisonDown_pic, poisonDownRight_pic, poisonRight_pic,
               poisonUpRight_pic, poisonUp_pic]
