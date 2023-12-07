import pygame
import sys
import random

pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")

game_font = pygame.font.Font(r'.\Assets\DinoGame\PressStart2P-Regular.ttf', 24)

# Classes


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x -= 1


class Dino(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\dinosaur0.png'), (80, 86)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\dinosaur1.png'), (80, 86)))

        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\dinosaur3.png'), (110, 52)))
        self.ducking_sprites.append(pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\dinosaur4.png'), (110, 52)))

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 40
        self.gravity = 3
        self.ducking = False

    def jump(self):
        jump_sfx.play()
        if self.rect.centery >= 340:
            while self.rect.centery - self.velocity > 30:
                self.rect.centery -= 1

    def duck(self):
        self.ducking = True
        self.rect.centery = 370

    def unduck(self):
        self.ducking = False
        self.rect.centery = 340

    def apply_gravity(self):
        if self.rect.centery <= 340:
            self.rect.centery += self.gravity

    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0

        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        else:
            self.image = self.running_sprites[int(self.current_image)]


class Cactus(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        for i in range(0, 7):
            current_sprite = pygame.transform.scale2x(pygame.image.load(rf'.\Assets\DinoGame\assets\cactus{i}.png'))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))


class Ptero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 1300
        self.y_pos = random.choice([260, 295, 350])
        self.sprites = []
        self.sprites.append(
            pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\Ptero1.png'), (84, 62)))
        self.sprites.append(
            pygame.transform.scale(pygame.image.load(r'.\Assets\DinoGame\assets\Ptero2.png'), (84, 62)))
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def animate(self):
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]

# Variables


game_speed = 4
jump_count = 10
player_score = 0
player_high_score = 0
game_over = False
obstacle_timer = 0
obstacle_spawn = False
obstacle_cooldown = 1200

# Surfaces

ground = pygame.image.load(r'.\Assets\DinoGame\assets\ground.png')
ground = pygame.transform.scale(ground, (1284, 24))
ground_x = 0
ground_rect = ground.get_rect(center=(640, 400))
cloud = pygame.image.load(r'.\Assets\DinoGame\assets\cloud.png')
cloud = pygame.transform.scale(cloud, (200, 80))

# Groups

cloud_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
dino_group = pygame.sprite.GroupSingle()
ptero_group = pygame.sprite.Group()

# Objects
dinosaur = Dino(50, 340)
dino_group.add(dinosaur)

# Sounds
death_sfx = pygame.mixer.Sound(r'.\Assets\DinoGame\sound\lose.mp3')
points_sfx = pygame.mixer.Sound(r'.\Assets\DinoGame\sound\100points.mp3')
jump_sfx = pygame.mixer.Sound(r'.\Assets\DinoGame\sound\jump.mp3')

# Events
CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT, 3000)

# Functions
def inistart():
    global player_score, player_high_score
    game_speed = 4
    player_score = 0
    screen.blit(pygame.transform.scale2x(pygame.image.load(r'.\Assets\DinoGame\assets\dinosaur2.png')),(10,300))
    text = game_font.render("Press Space or Up to start",1, (0, 0, 0))
    screen.blit(text, (1280 // 2 - text.get_width() // 2, 720 // 2 - text.get_height() // 2))
    score = game_font.render(str(int(player_score)), True, ("black"))
    screen.blit(score, (1150, 10))
    high_score = game_font.render(f'HI {int(player_high_score)}', True, ("red"))
    screen.blit(high_score, (900, 10))
    screen.blit(ground, (ground_x, 360))
  
class Dino_game():
    @staticmethod   
    def start():
        global game_over, game_speed, player_score, player_high_score, obstacle_timer, obstacle_spawn, obstacle_random, ground_x
        run=True
        game_over=False
        started=False          
        while run:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                dinosaur.duck()
            else:
                if dinosaur.ducking:
                    dinosaur.unduck()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                    pygame.quit()
                    sys.exit()
                if event.type == CLOUD_EVENT:
                    current_cloud_y = random.randint(50, 300)
                    current_cloud = Cloud(cloud, 1380, current_cloud_y)
                    cloud_group.add(current_cloud)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        started=True
                        dinosaur.jump()
                        if game_over:                            
                            game_over = False
                            game_speed = 4
                            player_score = 0
                    if event.key==pygame.K_ESCAPE:
                        run=False
                        started=False     
            
            screen.fill("white")
            # Collisions
            if pygame.sprite.spritecollide(dino_group.sprite, obstacle_group, False):
                game_over = True
                death_sfx.play()
            if game_over:         
                cloud_group.empty()
                obstacle_group.empty()
                game_over = False
                run=False
            if not started:
                inistart()
            if not game_over and started:
                game_speed += 0.00025
                if round(player_score, 1) % 100 == 0 and int(player_score) > 0:
                    points_sfx.play()

                if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
                    obstacle_spawn = True
                score = game_font.render(str(int(player_score)), True, ("black"))
                screen.blit(score, (1150, 10))
                high_score = game_font.render(f'HI {int(player_high_score)}', True, ("red"))
                screen.blit(high_score, (900, 10))
                if player_score>player_high_score:
                    player_high_score=player_score
                if obstacle_spawn:
                    obstacle_random = random.randint(1, 50)
                    if obstacle_random in range(1, 7):
                        new_obstacle = Cactus(1280, 340)
                        obstacle_group.add(new_obstacle)
                        obstacle_timer = pygame.time.get_ticks()
                        obstacle_spawn = False
                    elif obstacle_random in range(7, 10):
                        new_obstacle = Ptero()
                        obstacle_group.add(new_obstacle)
                        obstacle_timer = pygame.time.get_ticks()
                        obstacle_spawn = False

                player_score += 0.05
                

                ptero_group.update()
                ptero_group.draw(screen)

                dino_group.update()
                dino_group.draw(screen)

                obstacle_group.update()
                obstacle_group.draw(screen)

                ground_x -= game_speed


                screen.blit(ground, (ground_x, 360))
                screen.blit(ground, (ground_x + 1284, 360))
                if ground_x <= -1284:
                    ground_x = 0

            clock.tick(120)
            pygame.display.update()
        return player_score