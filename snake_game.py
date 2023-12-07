import pygame as pg
import sys
from random import randrange

vec2 = pg.math.Vector2
score = 0
run = True
class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.range = (self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size)
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100  # milliseconds
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
        
    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and self.directions[pg.K_UP]:
                self.direction = vec2(0, -self.size)
                self.directions = {pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}

            if event.key == pg.K_DOWN and self.directions[pg.K_DOWN]:
                self.direction = vec2(0, self.size)
                self.directions = {pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

            if event.key == pg.K_LEFT and self.directions[pg.K_LEFT]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}

            if event.key == pg.K_RIGHT and self.directions[pg.K_RIGHT]:
                self.direction = vec2(self.size, 0)
                self.directions = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}

    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def get_random_position(self):
        return [randrange(*self.range), randrange(*self.range)]

    def check_borders(self):
        global run, score
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
            run = False
        
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()
            run = False

    def check_food(self):
        global score
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1
            score += 10

    def check_selfeating(self):
        global run, score
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()
            run = False

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        [pg.draw.rect(self.game.screen, 'green', segment) for segment in self.segments]


class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_position()

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', self.rect)


class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 720
        self.TILE_SIZE = 30
        self.font = pg.font.SysFont('Constantia',30)
        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.new_game()

    def draw_grid(self):
        [pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
                                             for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
                                             for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def new_game(self):
        global run, score
        self.snake = Snake(self)
        self.food = Food(self)
        run = False

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(60)

    def draw(self):
        global score
        self.screen.fill('black')
        self.draw_grid()
        self.food.draw()
        self.snake.draw()
        text = self.font.render('Press arrow key to play!', True, (255,0,0))
        text_rect = text.get_rect(center=(150,15))
        self.screen.blit(text,text_rect)
        score_text = self.font.render(f'Score: {score}', True, (255,0,0))
        score_text_rect = score_text.get_rect(center=(600,15))
        self.screen.blit(score_text,score_text_rect)

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # snake control
            self.snake.control(event)

    def run(self):
        global run, score
        run = True
        score = 0
        while run:
            self.check_event()
            self.update()
            self.draw()
        return score
class Snake_game():
    def start():
        game = Game()
        game.run()
        print(score)
        return score