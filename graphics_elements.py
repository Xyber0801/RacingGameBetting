import pygame
import utils
# Global variable to track if hover sound has been played
global hover_sound_played

class Button(pygame.sprite.Sprite):
    button_sprites = [pygame.image.load(f"./Assets/UI/Button/UI_Flat_Button_Large_Lock_01a{i}.png") for i in range(1, 5)]

    def __init__(self, x, y, width, height, color, text, action=None, arg=None):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height
        self.color = color
        self.text = text

        self.normal_image = pygame.transform.scale(self.button_sprites[0], (self.width, self.height))
        self.hover_image = pygame.transform.scale(self.button_sprites[1], (self.width, self.height))
        self.click_image = pygame.transform.scale(self.button_sprites[2], (self.width, self.height))
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.played_hover_sound = False
        self.played_click_sound = False

        self.font = pygame.font.SysFont("Constantia", 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.width // 2, self.height // 2)
        self.image.blit(self.text_surface, self.text_rect)

        self.action = action
        self.arg = arg
        self.action_return_value = None

    def update_image(self):
        global hover_sound_played
        is_hovering = self.rect.collidepoint(pygame.mouse.get_pos())
        if is_hovering:
            if pygame.mouse.get_pressed()[0]:
                self.image = self.click_image
            else:
                self.image = self.hover_image
        else:
            hover_sound_played = False

        self.font = pygame.font.SysFont("Constantia", 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.width // 2, self.height // 2)
        self.image.blit(self.text_surface, self.text_rect)

    #when button is clicked, call the action function
    def click(self):
        if self.action is not None:
            self.action_return_value = self.action(self.arg) if self.arg is not None else self.action()

class InfoBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('./assets/Menu_Background/query_frame.png'), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.padding = 15

        self.font = pygame.font.SysFont("Constantia", 20)
        self.text = text
        self.center_x = (self.x + self.width // 2, self.y + self.padding)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        utils.renderTextCenteredAt(self.text, self.font, pygame.Color("white"), self.center_x[0], self.center_x[1], screen, self.width-self.padding*2)
class Title:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.transform.scale(pygame.image.load('./assets/Menu_Background/title_frame0.png'), (self.width, self.height))
        self.font = pygame.font.SysFont("Constantia", 35)
        self.text = text
        self.center_x = (self.x + self.width // 2, self.y + self.height // 2)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #utils.renderTextCenteredAt(self.text, self.font, pygame.Color("black"), self.center_x[0], self.y, screen, self.width)
        text_surface = self.font.render(self.text, True, pygame.Color("black"))
        screen.blit(text_surface, (self.center_x[0] - text_surface.get_width() // 2, self.y + self.height // 4))

class Background():
    def __init__(self, name, width, height, image, first_lane_y_pos, start_point, end_point):
        self.name = name
        self.width = width
        self.height = height
        self.first_lane_y_pos = first_lane_y_pos
        self.start_point = start_point
        self.end_point = end_point

        self.image = pygame.transform.scale(image, (self.width, self.height))