# In enemies.mage
mage_speech1 = [
    "!!!!!!",
    "Oh my, this is worse than I had imagined...",
    "Hm... how to proceed...",
    "Ah yes, I've thought of just the thing...",
    "The Crystal of Arcane Destruction!",
    "Been waiting ages to use this thing!",
    "Now... what were the incantations again? Hmmm...",
    "Ah, yes! ** incoherent mumbling ** ... ",
    "That should do the trick...",
    "Well... Here goes nothing!"
]
# In enemies.mage
mage_speech2 = [
    "Oooo... That was fun!",
    "And don't come back you hellish vermin!",
    "And to you! Yes, you...",
    "That was some defense you put up until I got here!",
    "Well done kiddo! Congratulations on not dying!",
    "The citizens of StoneBorn Castle owe you their lives!",
    "And it will be a long time before Lord Darken...",
    "will have the power to try another attack like that one.",
    "What a day... I think I'm going to go take a nap...",
    "I suggest you do the same!"
]

# in tower_cost_display()
tower_costs = "Tower costs:\n" \
              "Tier 1: $100\n" \
              "Tier 2: Tier 1 + $125\n" \
              "Tier 3: Tier 2 + $150"

# In intro_loop()
intro_text = "The time to act is now! Lord Darken has set his armies of " \
             "the damned upon the innocents within StoneBorn Castle. As " \
             "general of the Resistance Army it is your duty to direct the " \
             "building of our static tower defenses. Enlist the help of " \
             "our builders and the magician, Braum, in order to erect " \
             "magical towers to keep our enemies at bay. Our fighters within " \
             "the castle can hold off only a limited number of enemies " \
             "before the castle falls. A raven has been sent to the " \
             "Archmage, Jorah Stormbender. If we can just hold long enough " \
             "I know he can save us..."
title = "Twisted Towers!"

# In tower_info_loop()
basic_tower_text = "Basic Tower (Tier 1 Tower):\n" \
                   "\nTier 1 tower, does normal damage." \
                   "\nDamage:            50 per hit" \
                   "\nRate of fire:       every other second" \
                   "\nCost: $100" \
                   "\nSells for: $75" \
                   "\nSpecial attributes: None"
ice1_text = "Rank 1 Ice Tower (Tier 2 Tower):\n" \
            "\nDoes normal damage and slows 30%." \
            "\nDamage:         37.5 damage per hit" \
            "\nRate of fire:    Once per second" \
            "\nCost:            Basic Tower + $125 ($225 total)" \
            "\nSells for:        $170" \
            "\nRecommend: Pair with dark towers for extra hits."
ice2_text = "Rank 2 Ice Tower (Tier 3 Tower):\n" \
            "\n1.5x rank1 damage, double slow (60%)." \
            "\nDamage:        56.25 damage per hit" \
            "\nRate of fire:   Once per second" \
            "\nCost:           Rank 1 + $150 ($375 total)" \
            "\nSells for:       $280" \
            "\nRecommend: Pair with dark towers for extra hits."
fire1_text = "Rank 1 Fire  (Tier 2 Tower):\n" \
             "\nDoes damage over time in area of effect." \
             "\nDamage:         75 damage over 3 seconds" \
             "\nRate of fire:    Once per 3 seconds" \
             "\nCost:            Basic Tower + $125 ($225 total)" \
             "\nSells for:        $170" \
             "\nRecommend: vs. bunched enemies (spiders)."
fire2_text = "Rank 2 Fire Tower (Tier3 tower):\n" \
             "\n1.5x rank1 damage, 1st target catches other enemies " \
             "aflame in larger area." \
             "\nDamage:        112.5 damage over 3 seconds" \
             "\nRate of fire:   Once per 3 seconds" \
             "\nCost:           Rank 1 + $150 ($375 total)" \
             "\nSells for:       $280" \
             "\nRecommend: vs. bunched enemies (spiders)."
poison1_text = "Rank 1 Poison Tower (Tier2 tower) :\n" \
               "\nDoes % current hp over time, 50% armor shred, stuns " \
               "for 0.75 seconds at last damage tic." \
               "\nDamage:        ~22% current hp over 10 seconds" \
               "\nRate of fire:    Once per 3 seconds" \
               "\nCost:            Basic Tower + $125 ($225 total)" \
               "\nSells for:        $170" \
               "\nRecommend: vs high hp enemies (Orc, Dragon)."
poison2_text = "Rank 2 Poison Tower (Tier3 tower):\n" \
               "\n1.5x rank1 damage, double stun (1.5 seconds)." \
               "\nDamage:        ~41% current hp over 10 seconds" \
               "\nRate of fire:   Once per 3 seconds" \
               "\nCost:           Rank 1 + $150 ($375 total)" \
               "\nSells for:       $280" \
               "\nRecommend: vs high hp enemies (Orc, Dragon)."
dark1_text = "Rank 1 Dark Tower (Tier2 tower) :\n" \
             "\nDoes damage on hit, ignoring 50% of enemy armor." \
             "\nDamage:        75 damage per hit" \
             "\nRate of fire:    Every other second" \
             "\nCost:            Basic Tower + $125 ($225 total)" \
             "\nSells for:        $170" \
             "\nRecommend: vs. high armor enemies (Spiker, Dragon)."
dark2_text = "Rank 2 Dark Tower (Tier3 tower):\n" \
             "\n1.5x rank1 damage, ignoring 100% of enemy armor." \
             "\nDamage:        112.5 damage per hit" \
             "\nRate of fire:   Every other second" \
             "\nCost:           Rank 1 + $150 ($375 total)" \
             "\nSells for:       $280" \
             "\nRecommend: vs. high armor enemies (Spiker, Dragon)."

# In enemy_info_loop()
spider_text = "Spider\n" \
              "\nIndividually weak but forms large groups" \
              "\nHealth:     100" \
              "\nArmor:      0 (0% reduced damage)" \
              "\nSpeed:      1.2" \
              "\nKill value:   $8" \
              "\nTower damage: 1" \
              "\nRecommend: Fire towers most effective."
lizard_text = "Lizard Men\n" \
              "\nWell rounded foot soldier" \
              "\nHealth:     300" \
              "\nArmor:      50 (50% reduced damage)" \
              "\nSpeed:      1.2" \
              "\nKill value:   $50" \
              "\nTower damage: 2" \
              "\nRecommend: All towers fairly equally effective."
wolf_text = "Demon Wolf\n" \
            "\nNot particularly strong, but very fast" \
            "\nHealth:     240" \
            "\nArmor:      20 (20% reduced damage)" \
            "\nSpeed:      2" \
            "\nKill value:   $50" \
            "\nTower damage: 2" \
            "\nRecommend: Numerous and well spaced towers."
turtle_text = "Spikers\n" \
              "\nSlow, but highly armored enemy with low health" \
              "\nHealth:     200" \
              "\nArmor:      90 (90% reduced damage)" \
              "\nSpeed:      0.8" \
              "\nKill value:   $75" \
              "\nTower damage: 3" \
              "\nRecommend: Dark towers most effective."
orc_text = "Orc\n" \
           "\nFairly slow, low armor, but high health" \
           "\nHealth:      800" \
           "\nArmor:      20 (20% reduced damage)" \
           "\nSpeed:      1" \
           "\nKill value:   $75" \
           "\nTower damage: 3" \
           "\nRecommend: Early poison towers."
dragon_text = "Dragon\n" \
              "\nThe big one! Slow, with HIGH health and armor" \
              "\nHealth:      2000" \
              "\nArmor:      75 (75% reduced damage)" \
              "\nSpeed:      0.6" \
              "\nKill value:   $750" \
              "\nTower damage: 6" \
              "\nRecommend: Poison, and dark + ice tower combos. "

# Settings_loop
easy_text = "Slower spawning, easier enemies, " \
            "passive gold generation up, higher starting gold."
medium_text = "Normal enemy spawn rate and difficulty, gold generation, " \
              "and starting gold."
hard_text = "Fastest spawn rate and difficulty ramp up, reduced gold " \
            "generation, lower starting gold."
