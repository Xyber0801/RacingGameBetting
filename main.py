import pygame
pygame.init()

from coregame import CoreGame
import constants as c
from menu import menu
from Login import Logingin

clock = pygame.time.Clock()
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pygame.display.set_caption("Racing")

pygame.key.set_repeat(200, 25)

def __main__():
    if (not Logingin()):
        pygame.quit()
        quit()
        
    while True:
        menu()
        CoreGame.start(screen, clock)

if __name__ == '__main__':
    __main__()