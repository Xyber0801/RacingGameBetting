import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text, action=None):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height
        self.color = color
        self.text = text

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.font = pygame.font.SysFont("Arial", 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.width // 2, self.height // 2)
        self.image.blit(self.text_surface, self.text_rect)

        self.action = action
        self.action_return_value = None

    #when button is clicked, call the action function
    def click(self):
        if self.action is not None:
            self.action_return_value = self.action()
            
