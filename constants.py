import pygame
import graphics_elements as ge

# Path: constants.py
# Constants for the game
# Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Backgrounds
pygame.image.load("./assets/bg/grassland.png")
grassland_long = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
grassland_medium = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
grassland_short = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 250, 1000)
forest_long = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
forest_medium = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
forest_short = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 210, 250, 1000)
sunset_long = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
sunset_medium = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
sunset_short = ge.Background(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 250, 1000)

# character sets
#set 1 - medieval
archer = [pygame.image.load(f"./assets/char/medieval/archer/run_{i}.png") for i in range(1,9)]
knight_red = [pygame.image.load(f"./assets/char/medieval/knight_red/run_{i}.png") for i in range(1,8)]
commander = [pygame.image.load(f"./assets/char/medieval/commander/run_{i}.png") for i in range(1,9)]
knight_blue = [pygame.image.load(f"./assets/char/medieval/knight_blue/run_{i}.png") for i in range(1,8)]
samurai = [pygame.image.load(f"./assets/char/medieval/samurai/run_{i}.png") for i in range(1,8)]
archer_idle = [pygame.image.load(f"./assets/char/medieval/archer/idle_{i}.png") for i in range(1,10)]
knight_red_idle = [pygame.image.load(f"./assets/char/medieval/knight_red/idle_{i}.png") for i in range(1,5)]
commander_idle = [pygame.image.load(f"./assets/char/medieval/commander/idle_{i}.png") for i in range(1,6)]
knight_blue_idle = [pygame.image.load(f"./assets/char/medieval/knight_blue/idle_{i}.png") for i in range(1,5)]
samurai_idle = [pygame.image.load(f"./assets/char/medieval/samurai/idle_{i}.png") for i in range(1,7)]
#medieval_set contains the medieval images and the size(width) of the medieval
medieval_set = [archer, knight_red, commander, knight_blue, samurai, archer_idle, knight_red_idle, commander_idle, knight_blue_idle, samurai_idle, 64]

#set 2 - Robot
robot_1 = [pygame.image.load(f"./assets/char/robot/2/Walk_{i}.png") for i in range(1,7)]
robot_2 = [pygame.image.load(f"./assets/char/robot/3/Walk_{i}.png") for i in range(1,7)]
robot_3 = [pygame.image.load(f"./assets/char/robot/Destroyer/Walk_{i}.png") for i in range(1,9)]
robot_4 = [pygame.image.load(f"./assets/char/robot/Infantryman/Walk_{i}.png") for i in range(1,7)]
robot_5 = [pygame.image.load(f"./assets/char/robot/Swordsman/Walk_{i}.png") for i in range(1,9)]
robot_1_idle = [pygame.image.load(f"./assets/char/robot/2/Idle_{i}.png") for i in range(1,5)]
robot_2_idle = [pygame.image.load(f"./assets/char/robot/3/Idle_{i}.png") for i in range(1,5)]
robot_3_idle = [pygame.image.load(f"./assets/char/robot/Destroyer/Idle_{i}.png") for i in range(1,6)]
robot_4_idle = [pygame.image.load(f"./assets/char/robot/Infantryman/Idle_{i}.png") for i in range(1,7)]
robot_5_idle = [pygame.image.load(f"./assets/char/robot/Swordsman/Idle_{i}.png") for i in range(1,6)]
#robot_set contains the robot images and the size(width) of the robot
robot_set = [robot_1, robot_2, robot_3, robot_4, robot_5, robot_1_idle, robot_2_idle, robot_3_idle, robot_4_idle, robot_5_idle, 64]

#set 3 - Animal
bird = [pygame.image.load(f"./assets/char/Animal/Bird/Fly_{i}.png") for i in range(1,7)]
cat = [pygame.image.load(f"./assets/char/Animal/Cat/Walk_{i}.png") for i in range(1,7)]
dog = [pygame.image.load(f"./assets/char/Animal/Dog/Walk_{i}.png") for i in range(1,7)]
rat = [pygame.image.load(f"./assets/char/Animal/Rat/Walk_{i}.png") for i in range(1,5)]
fox = [pygame.image.load(f"./assets/char/Animal/fox/run_{i}.png") for i in range(1,5)]
bird_idle = [pygame.image.load(f"./assets/char/Animal/Bird/Idle_{i}.png") for i in range(1,5)]
cat_idle = [pygame.image.load(f"./assets/char/Animal/Cat/Idle_{i}.png") for i in range(1,5)]
dog_idle = [pygame.image.load(f"./assets/char/Animal/Dog/Idle_{i}.png") for i in range(1,5)]
rat_idle = [pygame.image.load(f"./assets/char/Animal/Rat/Idle_{i}.png") for i in range(1,5)]
fox_idle = [pygame.image.load(f"./assets/char/Animal/fox/idle_{i}.png") for i in range(1,5)]
#animal_set contains the animal images and the size(width) of the animal
animal_set = [bird, cat, dog, rat, fox, bird_idle, cat_idle, dog_idle, rat_idle, fox_idle, 64]

#set 4 - chibi
archer = [pygame.image.load(f"./assets/char/chibi/Archer/Run_{i}.png") for i in range(1,9)]
enchantress = [pygame.image.load(f"./assets/char/chibi/Enchantress/Run_{i}.png") for i in range(1,9)]
knight = [pygame.image.load(f"./assets/char/chibi/Knight/Run_{i}.png") for i in range(1,8)]
swordsman = [pygame.image.load(f"./assets/char/chibi/Swordsman/Run_{i}.png") for i in range(1,9)]
wizard = [pygame.image.load(f"./assets/char/chibi/Knight/Run_{i}.png") for i in range(1,8)]
archer_idle = [pygame.image.load(f"./assets/char/chibi/Archer/Idle_{i}.png") for i in range(1,5)]
enchantress_idle = [pygame.image.load(f"./assets/char/chibi/Enchantress/Idle_{i}.png") for i in range(1,6)]
knight_idle = [pygame.image.load(f"./assets/char/chibi/Knight/Idle_{i}.png") for i in range(1,7)]
swordsman_idle = [pygame.image.load(f"./assets/char/chibi/Swordsman/Idle_{i}.png") for i in range(1,4)]
wizard_idle = [pygame.image.load(f"./assets/char/chibi/Knight/Idle_{i}.png") for i in range(1,6)]
#chibi_set contains the chibi images and the size(width) of the chibi
chibi_set = [archer, enchantress, knight, swordsman, wizard, archer_idle, enchantress_idle, knight_idle, swordsman_idle, wizard_idle, 64]

#set 5 - monster
karasu_tengu = [pygame.image.load(f"./assets/char/monster/Karasu_tengu/Run_{i}.png") for i in range(1,9)]
kitsune = [pygame.image.load(f"./assets/char/monster/Kitsune/Run_{i}.png") for i in range(1,9)]
ogre = [pygame.image.load(f"./assets/char/monster/ogre/Run_{i}.png") for i in range(1,8)]
yamabushi_tengu = [pygame.image.load(f"./assets/char/monster/Yamabushi_tengu/Run_{i}.png") for i in range(1,9)]
yurei = [pygame.image.load(f"./assets/char/monster/yurei/Run_{i}.png") for i in range(1,6)]
karasu_tengu_idle = [pygame.image.load(f"./assets/char/monster/Karasu_tengu/Idle_{i}.png") for i in range(1,6)]
kitsune_idle = [pygame.image.load(f"./assets/char/monster/Kitsune/Idle_{i}.png") for i in range(1,7)]
ogre_idle = [pygame.image.load(f"./assets/char/monster/ogre/Idle_{i}.png") for i in range(1,7)]
yamabushi_tengu_idle = [pygame.image.load(f"./assets/char/monster/Yamabushi_tengu/Idle_{i}.png") for i in range(1,6)]
yurei_idle = [pygame.image.load(f"./assets/char/monster/yurei/Idle_{i}.png") for i in range(1,6)]
#monster_set contains the monster images and the size(width) of the monster
monster_set = [karasu_tengu, kitsune, ogre, yamabushi_tengu, yurei, karasu_tengu_idle, kitsune_idle, ogre_idle, yamabushi_tengu_idle, yurei_idle, 64]

#set 6 - car
car_1 = [pygame.image.load(f"./assets/char/car/1.png")]
car_2 = [pygame.image.load(f"./assets/char/car/2.png")]
car_3 = [pygame.image.load(f"./assets/char/car/3.png")]
car_4 = [pygame.image.load(f"./assets/char/car/4.png")]
car_5 = [pygame.image.load(f"./assets/char/car/5.png")]
car_1_idle = [pygame.image.load(f"./assets/char/car/1.png")]
car_2_idle = [pygame.image.load(f"./assets/char/car/2.png")]
car_3_idle = [pygame.image.load(f"./assets/char/car/3.png")]
car_4_idle = [pygame.image.load(f"./assets/char/car/4.png")]
car_5_idle = [pygame.image.load(f"./assets/char/car/5.png")]
#car_set contains the car images and the size(width) of the car
car_set = [car_1, car_2, car_3, car_4, car_5, car_1_idle, car_2_idle, car_3_idle, car_4_idle, car_5_idle, 128]

#Spells
#spells effects
spell_effect_size = (32, 32)
stun_effect = pygame.transform.scale(pygame.image.load('./assets/spells/stun_effect.png'), (64, 64))
speed_effect = pygame.transform.scale(pygame.image.load('./assets/spells/speed_effect.png'), spell_effect_size)
slow_effect = pygame.transform.scale(pygame.image.load('./assets/spells/slow_effect.png'), spell_effect_size)
winner_crown = pygame.transform.scale(pygame.image.load('./assets/spells/winner_crown.png'), (32, 32))