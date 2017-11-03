import pygame

# Castle hit
castle_hit = pygame.mixer.Sound('soundEffects/CrowdCryOut2.wav')
castle_hit.set_volume(.8)


# Tower build/sell
build_tower_sound = pygame.mixer.Sound('soundEffects/TowerConstruct.wav')
build_tower_sound.set_volume(0.05)

sell_tower_sound = pygame.mixer.Sound('soundEffects/TowerSell.wav')
sell_tower_sound.set_volume(0.75)

# Deaths
spider_death_sound = pygame.mixer.Sound('soundEffects/Deaths/SpiderDeath.wav')
spider_death_sound.set_volume(0.5)

wolf_death_sound = pygame.mixer.Sound('soundEffects/Deaths/WolfDeath.wav')
wolf_death_sound.set_volume(0.7)

turtle_death_sound = pygame.mixer.Sound('soundEffects/Deaths/TurtleDeath2.wav')
turtle_death_sound.set_volume(1)

dragon_death_sound = pygame.mixer.Sound('soundEffects/Deaths/DragonDeath.wav')
dragon_death_sound.set_volume(0.7)

orc_death_sound = pygame.mixer.Sound('soundEffects/Deaths/OrcDeath.wav')
orc_death_sound.set_volume(0.7)

lizard_death_sound = pygame.mixer.Sound('soundEffects/Deaths/LizardDeath.wav')
lizard_death_sound.set_volume(0.7)

