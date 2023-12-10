import pygame
import graphics_elements as ge

# Path: constants.py
# Constants for the game
# Screen size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Race setup variable
background_setup = None
character_setup = None
money = 300

#back button shananigans
go_to_distance_selection = False

# Backgrounds
menu_background = pygame.transform.scale(pygame.image.load("./assets/Menu_Background/Menu0.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
#race backgrounds are stored in a list, each background contains the image, the first lane y position, the start point and the end point
grassland_long = ge.Background('grassland_long', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
grassland_medium = ge.Background('grassland_medium', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
grassland_short = ge.Background('grassland_short', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/grassland_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 250, 1000)
forest_long = ge.Background('forest_long', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
forest_medium = ge.Background('forest_medium', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
forest_short = ge.Background('forest_short', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/forest_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 210, 250, 1000)
sunset_long = ge.Background('sunset_long', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_long.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 50, 1216)
sunset_medium = ge.Background('sunset_medium', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_medium.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 150, 1100)
sunset_short = ge.Background('sunset_short', SCREEN_WIDTH, SCREEN_HEIGHT, pygame.transform.scale(pygame.image.load("./assets/bg/sunset_short.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)), 230, 250, 1000)

# character sets
#set 1 - medieval
archer_sprites = [pygame.image.load(f"./assets/char/medieval/archer/run_{i}.png") for i in range(1,9)]
knight_red_sprites = [pygame.image.load(f"./assets/char/medieval/knight_red/run_{i}.png") for i in range(1,8)]
commander_sprites = [pygame.image.load(f"./assets/char/medieval/commander/run_{i}.png") for i in range(1,9)]
knight_blue_sprites = [pygame.image.load(f"./assets/char/medieval/knight_blue/run_{i}.png") for i in range(1,8)]
samurai_sprites = [pygame.image.load(f"./assets/char/medieval/samurai/run_{i}.png") for i in range(1,8)]
archer_idle_sprites = [pygame.image.load(f"./assets/char/medieval/archer/idle_{i}.png") for i in range(1,10)]
knight_red_idle_sprites = [pygame.image.load(f"./assets/char/medieval/knight_red/idle_{i}.png") for i in range(1,5)]
commander_idle_sprites = [pygame.image.load(f"./assets/char/medieval/commander/idle_{i}.png") for i in range(1,6)]
knight_blue_idle_sprites = [pygame.image.load(f"./assets/char/medieval/knight_blue/idle_{i}.png") for i in range(1,5)]
samurai_idle_sprites = [pygame.image.load(f"./assets/char/medieval/samurai/idle_{i}.png") for i in range(1,7)]
archer_celebrate_sprites = [pygame.image.load(f"./assets/char/medieval/archer/celebrate_{i}.png") for i in range(1,10)]
knight_red_celebrate_sprites = [pygame.image.load(f"./assets/char/medieval/knight_red/celebrate_{i}.png") for i in range(1,7)]
commander_celebrate_sprites = [pygame.image.load(f"./assets/char/medieval/commander/celebrate_{i}.png") for i in range(1,8)]
knight_blue_celebrate_sprites = [pygame.image.load(f"./assets/char/medieval/knight_blue/celebrate_{i}.png") for i in range(1,7)]
samurai_celebrate_sprites = [pygame.image.load(f"./assets/char/medieval/samurai/celebrate_{i}.png") for i in range(1,10)]
#medieval_set contains the medieval images, the size(width) of the medieval and the head position of the medieval character
medieval_set = [archer_sprites, knight_red_sprites, commander_sprites, knight_blue_sprites, samurai_sprites, archer_idle_sprites, knight_red_idle_sprites, commander_idle_sprites, knight_blue_idle_sprites, samurai_idle_sprites, archer_celebrate_sprites, knight_red_celebrate_sprites, commander_celebrate_sprites, knight_blue_celebrate_sprites, samurai_celebrate_sprites, 64, (32,64), (26,75), (32,68), (26,75), (32,68)]
                

#set 2 - Animal
bird_sprites = [pygame.image.load(f"./assets/char/Animal/Bird/Fly_{i}.png") for i in range(1,7)]
cat_sprites = [pygame.image.load(f"./assets/char/Animal/Cat/Walk_{i}.png") for i in range(1,7)]
dog_sprites = [pygame.image.load(f"./assets/char/Animal/Dog/run_{i}.png") for i in range(1,7)]
fox_sprites = [pygame.image.load(f"./assets/char/Animal/fox/run_{i}.png") for i in range(1,5)]
bear_sprites = [pygame.image.load(f"./assets/char/animal/bear/run_{i}.png") for i in range(1,7)]
bird_idle_sprites = [pygame.image.load(f"./assets/char/Animal/Bird/Idle_{i}.png") for i in range(1,5)]
cat_idle_sprites = [pygame.image.load(f"./assets/char/Animal/Cat/Idle_{i}.png") for i in range(1,5)]
dog_idle_sprites = [pygame.image.load(f"./assets/char/Animal/Dog/Idle_{i}.png") for i in range(1,5)]
fox_idle_sprites = [pygame.image.load(f"./assets/char/Animal/fox/idle_{i}.png") for i in range(1,5)]
bear_idle_sprites = [pygame.image.load(f"./assets/char/animal/bear/idle_{i}.png") for i in range(1,5)]
bird_celebrate_sprites = [pygame.image.load(f"./assets/char/Animal/Bird/celebrate_{i}.png") for i in range(1,4)]
cat_celebrate_sprites = [pygame.image.load(f"./assets/char/Animal/Cat/celebrate_{i}.png") for i in range(1,5)]
dog_celebrate_sprites = [pygame.image.load(f"./assets/char/Animal/Dog/celebrate_{i}.png") for i in range(1,5)]
fox_celebrate_sprites = [pygame.image.load(f"./assets/char/Animal/fox/celebrate_{i}.png") for i in range(1,4)]
bear_celebrate_sprites = [pygame.image.load(f"./assets/char/animal/bear/celebrate_{i}.png") for i in range(1,9)]
#animal_set contains the animal images, the size(width) of the animal and the head position of the animal character
animal_set = [bird_sprites, cat_sprites, dog_sprites, bear_sprites, fox_sprites, bird_idle_sprites, cat_idle_sprites, dog_idle_sprites, bear_idle_sprites, fox_idle_sprites, bird_celebrate_sprites, cat_celebrate_sprites, dog_celebrate_sprites, bear_celebrate_sprites, fox_celebrate_sprites, 64, (30,100), (40,98), (50,70), (50,110), (38,110)]

#set 3 - chibi
archer_sprites = [pygame.image.load(f"./assets/char/chibi/Archer/Run_{i}.png") for i in range(1,9)]
enchantress_sprites = [pygame.image.load(f"./assets/char/chibi/Enchantress/Run_{i}.png") for i in range(1,9)]
knight_sprites = [pygame.image.load(f"./assets/char/chibi/Knight/Run_{i}.png") for i in range(1,8)]
swordsman_sprites = [pygame.image.load(f"./assets/char/chibi/Swordsman/Run_{i}.png") for i in range(1,9)]
wizard_sprites = [pygame.image.load(f"./assets/char/chibi/Wizard/Run_{i}.png") for i in range(1,8)]
archer_idle_sprites = [pygame.image.load(f"./assets/char/chibi/Archer/Idle_{i}.png") for i in range(1,5)]
enchantress_idle_sprites = [pygame.image.load(f"./assets/char/chibi/Enchantress/Idle_{i}.png") for i in range(1,6)]
knight_idle_sprites = [pygame.image.load(f"./assets/char/chibi/Knight/Idle_{i}.png") for i in range(1,7)]
swordsman_idle_sprites = [pygame.image.load(f"./assets/char/chibi/Swordsman/Idle_{i}.png") for i in range(1,4)]
wizard_idle_sprites = [pygame.image.load(f"./assets/char/chibi/Wizard/Idle_{i}.png") for i in range(1,6)]
archer_celebrate_sprites = [pygame.image.load(f"./assets/char/chibi/Archer/Celebrate_{i}.png") for i in range(1,10)]
enchantress_celebrate_sprites = [pygame.image.load(f"./assets/char/chibi/Enchantress/Celebrate_{i}.png") for i in range(1,9)]
knight_celebrate_sprites = [pygame.image.load(f"./assets/char/chibi/Knight/Celebrate_{i}.png") for i in range(1,7)]
swordsman_celebrate_sprites = [pygame.image.load(f"./assets/char/chibi/Swordsman/Celebrate_{i}.png") for i in range(1,9)]
wizard_celebrate_sprites = [pygame.image.load(f"./assets/char/chibi/Wizard/Celebrate_{i}.png") for i in range(1,12)]
#chibi_set contains the chibi images, the size(width) of the chibi and the head position of the chibi character
chibi_set = [archer_sprites, enchantress_sprites, knight_sprites, swordsman_sprites, wizard_sprites, archer_idle_sprites, enchantress_idle_sprites, knight_idle_sprites, swordsman_idle_sprites, wizard_idle_sprites, archer_celebrate_sprites, enchantress_celebrate_sprites, knight_celebrate_sprites, swordsman_celebrate_sprites, wizard_celebrate_sprites, 64, (25, 70), (25, 70), (25, 70), (25, 70), (25, 70)]

#set 4 - monster
karasu_tengu_sprites = [pygame.image.load(f"./assets/char/monster/Karasu_tengu/Run_{i}.png") for i in range(1,9)]
kitsune_sprites = [pygame.image.load(f"./assets/char/monster/Kitsune/Run_{i}.png") for i in range(1,9)]
ogre_sprites = [pygame.image.load(f"./assets/char/monster/ogre/Run_{i}.png") for i in range(1,8)]
yamabushi_tengu_sprites = [pygame.image.load(f"./assets/char/monster/Yamabushi_tengu/Run_{i}.png") for i in range(1,9)]
yurei_sprites = [pygame.image.load(f"./assets/char/monster/yurei/Run_{i}.png") for i in range(1,6)]
karasu_tengu_idle_sprites = [pygame.image.load(f"./assets/char/monster/Karasu_tengu/Idle_{i}.png") for i in range(1,6)]
kitsune_idle_sprites = [pygame.image.load(f"./assets/char/monster/Kitsune/Idle_{i}.png") for i in range(1,7)]
ogre_idle_sprites = [pygame.image.load(f"./assets/char/monster/ogre/Idle_{i}.png") for i in range(1,7)]
yamabushi_tengu_idle_sprites = [pygame.image.load(f"./assets/char/monster/Yamabushi_tengu/Idle_{i}.png") for i in range(1,6)]
yurei_idle_sprites = [pygame.image.load(f"./assets/char/monster/yurei/Idle_{i}.png") for i in range(1,6)]
karasu_tengu_celebrate_sprites = [pygame.image.load(f"./assets/char/monster/Karasu_tengu/Celebrate_{i}.png") for i in range(1,16)]
kitsune_celebrate_sprites = [pygame.image.load(f"./assets/char/monster/Kitsune/Celebrate_{i}.png") for i in range(1,11)]
ogre_celebrate_sprites = [pygame.image.load(f"./assets/char/monster/ogre/Celebrate_{i}.png") for i in range(1,7)]
yamabushi_tengu_celebrate_sprites = [pygame.image.load(f"./assets/char/monster/Yamabushi_tengu/Celebrate_{i}.png") for i in range(1,16)]
yurei_celebrate_sprites = [pygame.image.load(f"./assets/char/monster/yurei/Celebrate_{i}.png") for i in range(1,5)]
#monster_set contains the monster images, the size(width) of the monster and the head position of the monster character
monster_set = [karasu_tengu_sprites, kitsune_sprites, ogre_sprites, yamabushi_tengu_sprites, yurei_sprites, karasu_tengu_idle_sprites, kitsune_idle_sprites, ogre_idle_sprites, yamabushi_tengu_idle_sprites, yurei_idle_sprites, karasu_tengu_celebrate_sprites, kitsune_celebrate_sprites, ogre_celebrate_sprites, yamabushi_tengu_celebrate_sprites, yurei_celebrate_sprites, 64, (45, 50), (25, 70), (25, 70), (45, 50), (25, 70)]

#set 5 - car
car_1_sprites = [pygame.image.load(f"./assets/char/car/1.png")]
car_2_sprites = [pygame.image.load(f"./assets/char/car/2.png")]
car_3_sprites = [pygame.image.load(f"./assets/char/car/3.png")]
car_4_sprites = [pygame.image.load(f"./assets/char/car/4.png")]
car_5_sprites = [pygame.image.load(f"./assets/char/car/5.png")]
car_1_celebrate_sprites = [pygame.image.load(f"./assets/char/car/1.png"), pygame.image.load(f"./assets/char/car/celebrate_1.png")]
car_2_celebrate_sprites = [pygame.image.load(f"./assets/char/car/2.png"), pygame.image.load(f"./assets/char/car/celebrate_2.png")]
car_3_celebrate_sprites = [pygame.image.load(f"./assets/char/car/3.png"), pygame.image.load(f"./assets/char/car/celebrate_3.png")]
car_4_celebrate_sprites = [pygame.image.load(f"./assets/char/car/4.png"), pygame.image.load(f"./assets/char/car/celebrate_4.png")]
car_5_celebrate_sprites = [pygame.image.load(f"./assets/char/car/5.png"), pygame.image.load(f"./assets/char/car/celebrate_5.png")]
#car_set contains the car images, the size(width) of the car and the head position of the car character
car_set = [car_1_sprites, car_2_sprites, car_3_sprites, car_4_sprites, car_5_sprites, car_1_sprites, car_2_sprites, car_3_sprites, car_4_sprites, car_5_sprites, car_1_celebrate_sprites, car_2_celebrate_sprites, car_3_celebrate_sprites, car_4_celebrate_sprites, car_5_celebrate_sprites, 128, (65, 95), (65, 95), (65, 95), (65, 95), (65, 95)]

#Spells
#spells effects
spell_effect_size = (32, 32)
stun_effect = pygame.transform.scale(pygame.image.load('./assets/spells/stun_effect.png'), (64, 64))
speed_effect = pygame.transform.scale(pygame.image.load('./assets/spells/speed_effect.png'), spell_effect_size)
slow_effect = pygame.transform.scale(pygame.image.load('./assets/spells/slow_effect.png'), spell_effect_size)
winner_crown = pygame.transform.scale(pygame.image.load('./assets/spells/winner_crown.png'), (32, 32))