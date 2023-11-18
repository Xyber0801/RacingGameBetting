import pygame
import pygame_textinput
from coregame import CoreGame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Racing")

textinput = pygame_textinput.TextInputVisualizer()

pygame.key.set_repeat(200, 25)

def __main__():
    CoreGame.start(screen, clock, textinput)

if __name__ == '__main__':
    __main__()