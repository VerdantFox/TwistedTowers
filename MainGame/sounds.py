import pygame

# Castle hit
castle_hit = pygame.mixer.Sound('soundEffects/CrowdCryOut.wav')
castle_hit.set_volume(.5)


# Tower build/sell
build_tower_sound = pygame.mixer.Sound('soundEffects/TowerConstruct.wav')
build_tower_sound.set_volume(0.2)

sell_tower_sound = pygame.mixer.Sound('soundEffects/TowerSell.wav')
sell_tower_sound.set_volume(0.8)

# Mage
mage_spell_sound = pygame.mixer.Sound('soundEffects/MageSpell.wav')
mage_spell_sound.set_volume(0.75)

grumbling_sound = pygame.mixer.Sound('soundEffects/OldManGrumbling2.wav')
mage_spell_sound.set_volume(1)

# Deaths
spider_death_sound = pygame.mixer.Sound('soundEffects/Deaths/SpiderDeath.wav')
spider_death_sound.set_volume(0.8)

wolf_death_sound = pygame.mixer.Sound('soundEffects/Deaths/WolfDeath.wav')
wolf_death_sound.set_volume(0.7)

turtle_death_sound = pygame.mixer.Sound('soundEffects/Deaths/TurtleDeath.wav')
turtle_death_sound.set_volume(1)

dragon_death_sound = pygame.mixer.Sound('soundEffects/Deaths/DragonDeath.wav')
dragon_death_sound.set_volume(0.7)

orc_death_sound = pygame.mixer.Sound('soundEffects/Deaths/OrcDeath.wav')
orc_death_sound.set_volume(0.7)

lizard_death_sound = pygame.mixer.Sound('soundEffects/Deaths/LizardDeath.wav')
lizard_death_sound.set_volume(0.7)

# Tower shots
tower_shoot_sound = pygame.mixer.Sound('soundEffects/TowerShots/Shooting.wav')
tower_shoot_sound.set_volume(.1)

basic_hit_sound = pygame.mixer.Sound('soundEffects/TowerShots/Basic.wav')
basic_hit_sound.set_volume(.2)

ice_hit_sound = pygame.mixer.Sound('soundEffects/TowerShots/Ice.wav')
ice_hit_sound.set_volume(.6)

fire_hit_sound = pygame.mixer.Sound('soundEffects/TowerShots/Fire.wav')
fire_hit_sound.set_volume(.75)

poison_hit_sound = pygame.mixer.Sound('soundEffects/TowerShots/Poison.wav')
poison_hit_sound.set_volume(.4)

dark_hit_sound = pygame.mixer.Sound('soundEffects/TowerShots/Dark.wav')
dark_hit_sound.set_volume(.6)
