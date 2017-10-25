import pygame

basicTower1 = pygame.image.load('towers/basicTower.png'), 50, 80
iceTower1 = pygame.image.load('towers/iceTower1.png'), 50, 80
fireTower1 = pygame.image.load('towers/fireTower1.png'), 50, 80
poisonTower1 = pygame.image.load('towers/poisonTower1.png'), 50, 80
darkTower1 = pygame.image.load('towers/darkTower1.png'), 50, 80

fire_pic = pygame.image.load('effects/fire40.png'), 32, 40
ice_pic = pygame.image.load('effects/ice50.png'), 50, 20
poisonDown_pic = pygame.image.load(
    'effects/poisoncloudDOWN.png'), 60, 60
poisonDownRight_pic = pygame.image.load(
    'effects/poisoncloudDOWN_RIGHT.png'), 60, 60
poisonRight_pic = pygame.image.load(
    'effects/poisoncloudRIGHT.png'), 60, 60
poisonUpRight_pic = pygame.image.load(
    'effects/poisoncloudUP_RIGHT.png'), 60, 60
poisonUp_pic = pygame.image.load(
    'effects/poisoncloudUP.png'), 60, 60

poison_list = [poisonDown_pic, poisonDownRight_pic, poisonRight_pic,
               poisonUpRight_pic, poisonUp_pic]

stun1 = pygame.image.load(
    'effects/stun1.png'), 30, 30
stun2 = pygame.image.load(
    'effects/stun2.png'), 30, 30
stun3 = pygame.image.load(
    'effects/stun3.png'), 30, 30
stun4 = pygame.image.load(
    'effects/stun4.png'), 30, 30

stun_list = [stun1, stun2, stun3, stun4]

