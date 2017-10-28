import random

import pygame

from Enemies.orc.orcPics import orc_list, orcdead
from Enemies.spider.spiderPics import spider_list, spiderdead
from Enemies.turtle.turtlePics import turtle_list, turtledead
from Enemies.wolf.wolfPics import wolf_list, wolfdead
from Enemies.dragon.dragonPics import dragon_list, dragondead
from Enemies.lizard.lizardPics import lizard_list, lizarddead
from definitions import *
from gameParameters import gameDisplay
from lists import *
from towers.towerPics import fire_pic, ice_pic, poison_list, stun_list


class Orc:
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        # Position and movement
        self.x, self.y = location
        self.base_speed = 1
        self.speed = self.base_speed
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.next_node = next_node  # see lists.py
        self.node = 0
        self.stationary = stationary

        # Image manipulation
        self.image = orc_list[0][0]
        self.image_width = 60
        self.image_height = 60
        self.initial_frames_to_picswap = 8
        self.frames_to_picswap = 8
        self.frame_counter = 0
        self.direction = 2
        self.frame = 0

        # Interaction with other objects
        self.radius = 5
        self.initial_fire_radius = 30
        self.fire_radius = 30

        # hp manipulation
        self.max_hp = 800
        self.hp = 800
        self.armor = 20

        # Death and destruction ;-)
        self.destroy = destroy  # Removes body until respawn timer returns to play
        self.dead = False  # Used to return cash and money
        self.points = 5
        self.cash = 75
        self.respawn_timer = random.randint(5 * seconds, 6.75 * seconds)
        self.respawn_countdown = self.respawn_timer
        self.lives = 2  # start dead, need 1 more than that
        self.added_to_list = False
        self.dead_image = orcdead
        self.dead_image_timer = 4 * seconds
        self.dead_image_countdown = 0
        self.dead_x = 0
        self.dead_y = 0
        self.dead_font = pygame.font.SysFont("Comic Sans MS", 14, bold=True)

        # Ice specialties
        self.ice_loc = ((-18, 10), (-18, 10), (-18, 10),
                        (-18, 10), (-18, 3))
        self.ice1 = False
        self.ice2 = False
        self.ice_counter = 2.5 * seconds
        self.ice1_countdown = self.ice_counter
        self.ice2_countdown = self.ice_counter

        # Fire specialties
        self.fire_loc = (-10, -50)
        self.fireball1 = 0
        self.fireball2 = 0
        self.fire1 = None
        self.fire2 = None
        self.burned_counter = 0
        self.fire_countdown = 1 * seconds

        # Poison specialties
        self.poison_loc = ((-27, -45), (-36, -57), (-51, -40),
                           (-45, -9), (-27, -3))
        self.stun_loc = ((-10, -40), (-5, -50), (-5, -50),
                         (-5, -50), (-10, -50))
        self.poison1 = None
        self.poison2 = None
        self.poison_tick = 0
        self.poison_countdown = 0
        self.poison_charges = 0
        self.stun = False
        self.stun_duration = 0.75 * seconds
        self.stun_duration_countdown = 0.75 * seconds
        self.stun_frameswap_rate = 10
        self.stun_frame = 0
        self.stun_framecounter = 0

        # Dark specialties
        self.dark_loc = ()
        self.dark = False
        self.dark_timer = .5 * seconds

    def move(self):

        if not self.destroy:
            if not self.stun:
                if not self.stationary:
                    # Move towards node by self.speed.
                    if self.x < self.next_node[0] - 5:
                        self.x += self.speed
                        self.right = True
                    if self.x > self.next_node[0] + 5:
                        self.x -= self.speed
                        self.left = True
                    if self.y < self.next_node[1] - 5:
                        self.y += self.speed
                        self.down = True
                    if self.y > self.next_node[1] + 5:
                        self.y -= self.speed
                        self.up = True

                # Change walking frame if frame_counter reaches 0
                if self.frame_counter < 1:
                    # Determine direction
                    self.direction = 2  # Default is right
                    if self.down and not self.right:
                        self.direction = 0
                    if self.down and self.right:
                        self.direction = 1
                    if self.right and not (self.up or self.down):
                        self.direction = 2
                    if self.up and self.right:
                        self.direction = 3
                    if self.up and not self.right:
                        self.direction = 4

                    self.walk()
                    self.frame_counter = self.frames_to_picswap
                if self.frame_counter > 0:
                    self.frame_counter -= self.speed

            if self.stun:
                if self.stun_duration_countdown == 0:
                    self.stun = False
                if self.stun_duration_countdown > 0:
                    self.stun_duration_countdown -= 1

            # Check for special attributes
            if self.ice1 or self.ice2:
                self.iced()
            if self.poison2:
                self.poisoned(self.poison2)
            if self.poison1 and not self.poison2:
                self.poisoned(self.poison1)
            if self.fire1 or self.fire2:
                self.burning()
            if self.fireball1 > 0:
                self.fireball1 -= 1
            if self.fireball2 > 0:
                self.fireball2 -= 1
            else:
                self.fire_radius = self.initial_fire_radius

            # Show
            self.show()

            # Switch to next node in path if at current node goal
            if self.next_node[0] - 10 < self.x < self.next_node[0] + 10:
                if self.next_node[1] - 10 < self.y < self.next_node[1] + 10:
                    if self.node < len(path_nodes) - 2:
                        self.node += 1
                        node_x, node_y = path_nodes[self.node]  # see lists.py
                        # Introduce some randomness to node locations
                        node_x += random.randrange(-10, 10)
                        node_y += random.randrange(-15, 15)
                        self.next_node = (node_x, node_y)  # See lists
                    else:
                        # Destroy and remove all affects, move to start of path
                        self.destroy = True
                        self.poison1 = None
                        self.poison2 = None
                        self.poison_tick = 0
                        self.poison_countdown = 0
                        self.poison_charges = 0
                        self.ice1 = False
                        self.ice2 = False
                        self.speed = self.base_speed
                        self.fire1 = None
                        self.fire2 = None
                        self.fireball1 = 0
                        self.fireball2 = 0
                        self.dark = False
                        self.x, self.y = path_nodes[0]
                        # Return damage to castle
                        return 1

        # If enemy is dead
        if self.destroy:
            # Show body
            if self.dead_image_countdown > 0:
                gameDisplay.blit(
                    self.dead_image, (self.dead_x - self.image_width // 2,
                                      self.dead_y - self.image_height // 2))
                self.dead_image_countdown -= 1
            # Show money earned
            if self.dead_image_countdown > 3 * seconds:
                text_surface = self.dead_font.render(
                    "${}".format(self.cash), True, yellow)
                text_rect = text_surface.get_rect()
                text_rect.center = (self.dead_x, self.dead_y-30)
                gameDisplay.blit(text_surface, text_rect)

            # Start respawn timer countdown
            if self.respawn_countdown > 0:
                self.respawn_countdown -= 1
            # If respawn timer reaches 0, respawn enemy and reset timer
            elif self.respawn_countdown <= 0:
                self.lives -= 1
                self.poison1 = None
                self.poison2 = None
                self.poison_tick = 0
                self.poison_countdown = 0
                self.poison_charges = 0
                self.fire1 = None
                self.fire2 = None
                self.fireball1 = 0
                self.fireball2 = 0
                self.burned_counter = 0
                self.ice1 = False
                self.ice2 = False
                self.speed = self.base_speed
                self.dark = False
                self.destroy = False
                self.x, self.y = path_nodes[0]
                self.node = 0
                self.next_node = path_nodes[0]
                self.hp = self.max_hp
                self.respawn_countdown = self.respawn_timer

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def walk(self):
        # Change walking frame in direction
        self.image = orc_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(orc_list[0]) - 1:
            self.frame = 0

    def show(self):
        if not self.destroy:
            if self.poison1 or self.poison2:
                self.show_poison()
            if self.fire1 or self.fire2:
                self.show_fire()
            if self.stun:
                self.show_stun()
            if self.ice1 or self.ice2:
                self.show_ice()

            gameDisplay.blit(self.image, (self.x - self.image_width // 2,
                                          self.y - self.image_height // 2))
            self.health_bar()

    def show_poison(self):
        gameDisplay.blit(
            poison_list[self.direction][0],
            (self.x + self.poison_loc[self.direction][0],
             self.y + self.poison_loc[self.direction][1]))

    def show_stun(self):
        gameDisplay.blit(
            stun_list[self.stun_frame][0],
            (self.x + self.stun_loc[self.direction][0],
             self.y + self.stun_loc[self.direction][1]))

        self.stun_framecounter -= 1
        if self.stun_framecounter < 1:
            self.stun_framecounter = self.stun_frameswap_rate
            self.stun_frame += 1
            if self.stun_frame == len(stun_list[0]):
                self.stun_frame = 0

    def show_fire(self):
        gameDisplay.blit(
            fire_pic[0], (self.x + self.fire_loc[0],
                          self.y + self.fire_loc[1]))

    def show_ice(self):
        gameDisplay.blit(
            ice_pic[0], (self.x + self.ice_loc[self.direction][0],
                         self.y + self.ice_loc[self.direction][1]))

    def take_damage(self, damage, armor_shred=False):
        if self.hp > 0:
            damage_reduced = (100 - self.armor) / 100
            if not armor_shred:
                self.hp -= damage * damage_reduced
            if armor_shred:
                self.hp -= damage

        if self.hp <= 0:
            self.dead_x = self.x
            self.dead_y = self.y
            self.dead_image_countdown = self.dead_image_timer
            self.dead = True
            self.destroy = True

    def health_bar(self):
        max_width = self.image_width // 2
        if self.hp >= 0:
            damage_width = int(max_width * self.hp // self.max_hp)
        else:
            damage_width = 0
        height = 4
        back_color = red
        front_color = green
        x = self.x - self.image_width // 4
        y = self.y - self.image_height * 3 // 4

        pygame.draw.rect(gameDisplay, back_color,
                         (x, y, max_width, height))
        if damage_width:
            pygame.draw.rect(gameDisplay, front_color,
                             (x, y, damage_width, height))

    def iced(self):
        if self.ice1_countdown > 0:
            self.ice1_countdown -= 1
        else:
            self.ice1 = False
        if self.ice2_countdown > 0:
            self.ice2_countdown -= 1
        else:
            self.ice2 = False
        multiplier = 1
        if self.ice2:
            multiplier = .4
        if self.ice1 and not self.ice2:
            multiplier = .7
        if not (self.ice1 or self.ice2):
            self.speed = self.base_speed
            self.frames_to_picswap = self.initial_frames_to_picswap
        else:
            self.speed = self.base_speed * multiplier
            self.frames_to_picswap = int(
                self.initial_frames_to_picswap * 1/multiplier)

    def burning(self):
        if self.burned_counter > 0:
            if self.fire_countdown == 0:
                if self.fire2:
                    self.take_damage(self.fire2)
                if self.fire1 and not self.fire2:
                    self.take_damage(self.fire1)
                self.fire_countdown = 1 * seconds
                self.burned_counter -= 1
            else:
                self.fire_countdown -= 1
        else:
            self.fire1 = None
            self.fire2 = None

    def poisoned(self, percent_hp):
        # Stun
        if self.poison_charges == 2 and self.poison_tick == 0:
            if self.poison2:
                self.stun_duration_countdown = self.stun_duration * 2
            if self.poison1 and not self.poison2:
                self.stun_duration_countdown = self.stun_duration
            self.stun = True

        poison_damage = percent_hp * self.hp
        if self.poison1:
            if poison_damage < 15:
                poison_damage = 15
        if self.poison2:
            if poison_damage < 22.5:
                poison_damage = 22.5
        if self.poison_charges > 0:
            # 50% armor shred
            if self.poison_tick == 0:
                self.take_damage(poison_damage/2, True)
                self.take_damage(poison_damage/2, False)
                self.poison_tick = 2 * seconds
                self.poison_charges -= 1
            else:
                self.poison_tick -= 1
        else:
            self.poison1 = None
            self.poison2 = None

    def check_death(self):
        if self.dead:
            self.dead = False
            return self.points, self.cash
        else:
            return None
    
    def hit(self, damage, specialty):
        if specialty == "basic":
            self.take_damage(damage)
        if specialty == "ice1":
            self.take_damage(damage)
            self.ice1 = True
            self.ice1_countdown = self.ice_counter
        if specialty == "ice2":
            self.take_damage(damage)
            self.ice2 = True
            self.ice2_countdown = self.ice_counter
        if specialty == "fire1":
            self.fireball1 = int(0.05 * seconds)
            self.fire1 = damage
            self.burned_counter = 3
        if specialty == "fire2":
            self.fireball2 = int(2.9 * seconds)
            self.fire_radius = self.initial_fire_radius * 2
            self.fire2 = damage
            self.burned_counter = 3
        if specialty == "poison1":
            self.poison1 = damage
            self.poison_charges = 5
        if specialty == "poison2":
            self.poison2 = damage
            self.poison_charges = 5
        if specialty == "dark1":
            self.take_damage(damage)
            self.take_damage(damage, True)
        if specialty == "dark2":
            self.take_damage(damage, True)


class Spider(Orc):
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = spider_list[0][0]
        self.image_width = 30
        self.image_height = 30
        self.frames_to_picswap = 6
        # Damage locations
        self.ice_loc = ((-25, 0), (-25, 0), (-25, -5),
                        (-25, 0), (-25, 0))
        self.fire_loc = (-20, -45)
        self.poison_loc = ((-30, -60), (-54, -60), (-60, -36),
                           (-54, -6), (-30, -3))
        self.stun_loc = ((-14, -38), (-14, -38), (-14, -38),
                         (-14, -38), (-14, -38))
        # hp manipulation
        self.max_hp = 100
        self.hp = 100
        self.armor = 0
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 8
        self.dead_image = spiderdead

    def walk(self):
        # Change walking frame in direction
        self.image = spider_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(spider_list[0]) - 1:
            self.frame = 0


class Wolf(Orc):
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = wolf_list[0][0]
        self.image_width = 50
        self.image_height = 50
        self.frames_to_picswap = 10
        # Damage locations
        self.ice_loc = ((-18, 15), (-18, 10), (-18, -10),
                        (-18, 10), (-18, 3))
        self.poison_loc = ((-20, -45), (-40, -40), (-51, -44),
                           (-45, -9), (-23, -3))
        self.stun_loc = ((-5, -40), (-5, -40), (-5, -40),
                         (-5, -40), (-5, -50))
        # hp manipulation
        self.max_hp = 240
        self.hp = 240
        self.armor = 20
        # Position and movement
        self.base_speed = 2
        self.speed = self.base_speed
        # Death
        self.cash = 50
        self.dead_image = wolfdead

    def walk(self):
        # Change walking frame in direction
        self.image = wolf_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(wolf_list[0]) - 1:
            self.frame = 0


class Turtle(Orc):
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = turtle_list[0][0]
        self.image_width = 44
        self.image_height = 44
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-22, 10), (-22, 10), (-25, 10),
                        (-22, 10), (-22, 12))
        self.poison_loc = ((-27, -60), (-52, -52), (-65, -35),
                           (-45, -9), (-27, 5))
        self.stun_loc = ((-10, -45), (-10, -40), (-10, -45),
                         (-10, -45), (-10, -45))
        # hp manipulation
        self.max_hp = 200
        self.hp = 200
        self.armor = 90
        # Position and movement
        self.base_speed = .8
        self.speed = self.base_speed
        # Death
        self.cash = 75
        self.dead_image = turtledead

    def walk(self):
        # Change walking frame in direction
        self.image = turtle_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(turtle_list[0]) - 1:
            self.frame = 0


class Lizard(Orc):
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = lizard_list[0][0]
        self.image_width = 60
        self.image_height = 60
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-25, 10), (-25, 10), (-25, 5),
                        (-22, 10), (-30, 10))
        self.poison_loc = ((-40, -80), (-52, -52), (-80, -40),
                           (-65, -5), (-30, 5))
        self.stun_loc = ((-15, -60), (-15, -60), (-10, -55),
                         (-15, -65), (-15, -60))
        self.fire_loc = (-20, -65)

        # hp manipulation
        self.max_hp = 300
        self.hp = 300
        self.armor = 50
        # Position and movement
        self.base_speed = 1.2
        self.speed = self.base_speed
        # Death
        self.cash = 50
        self.dead_image = lizarddead

    def walk(self):
        # Change walking frame in direction
        self.image = lizard_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(lizard_list[0]) - 1:
            self.frame = 0


class Dragon(Orc):
    def __init__(self, location=path_nodes[0], next_node=path_nodes[0],
                 stationary=False, destroy=True):
        super().__init__(location=location, next_node=next_node,
                         stationary=stationary, destroy=destroy)
        # Image manipulation
        self.image = dragon_list[0][0]
        self.image_width = 150
        self.image_height = 150
        self.frames_to_picswap = 8

        # Damage locations
        self.ice_loc = ((-5, 30), (-22, 10), (-25, 10),
                        (-22, 10), (-5, 30))
        self.poison_loc = ((-15, -80), (-52, -52), (-65, -60),
                           (-65, -20), (-15, 15))
        self.stun_loc = ((10, -75), (30, -70), (30, -85),
                         (30, -85), (0, -95))
        self.fire_loc = (0, -100)

        # hp manipulation
        self.max_hp = 2000
        self.hp = 2000
        self.armor = 75
        # Position and movement
        self.base_speed = .6
        self.speed = self.base_speed
        # Death
        self.cash = 750
        self.dead_image = dragondead

    def walk(self):
        # Change walking frame in direction
        self.image = dragon_list[self.direction][self.frame]
        self.frame += 1
        if self.frame > len(dragon_list[0]) - 1:
            self.frame = 0