import pygame
import pygame_textinput
from coregame import CoreGame
import constants as c


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Racing")

textinput = pygame_textinput.TextInputVisualizer()

pygame.key.set_repeat(200, 25)

def __main__():
    CoreGame.start(screen, clock, textinput, c.grassland_long, c.car_set)

if __name__ == '__main__':
    __main__()