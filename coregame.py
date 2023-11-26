import pygame
import random
import math
from minigame import Minigame
import graphics_elements

class CoreGame:
    running = False

    events = None
    dt = 0
    background = None
    char_set = None
    screen = None

    @staticmethod
    def start(screen, clock, textinput, background, char_set):
        running = True
        dt = 0
        CoreGame.background = background
        CoreGame.char_set = char_set
        CoreGame.screen = screen

        GameManager.init()

        print("start coregame")
        while running:
            current_time = pygame.time.get_ticks() / 1000
            CoreGame.events = pygame.event.get()

            screen.fill((255,255,255))

            if GameManager.state == 'betting':
                GameManager.betting_screen(screen, textinput)
            elif GameManager.state == 'racing':
                GameManager.racing_screen(dt, current_time, screen)
            elif GameManager.state == 'postgame':
                GameManager.postgame(screen)
            elif GameManager.state == 'minigame':
                GameManager.minigame(screen)
            
            GameManager.update(screen)

            for event in CoreGame.events:
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            dt = clock.tick(60) / 1000

class GameManager:
    # 4 states: 'betting', 'racing', 'postgame', 'minigame'
    state = None

    player = None

    # A group of all the racers
    racers = pygame.sprite.Group()
    racers_showcase = pygame.sprite.Group()
    finished_racers = pygame.sprite.Group()

    @staticmethod
    def init():
        '''Initialize the game'''        
        GameManager.generate_racers(CoreGame.char_set)
        GameManager.player = Gambler(1000, 'Player')
        GameManager.state = 'betting'

    @staticmethod
    def update(screen):
        Gui.update_buttons(screen)  
     
    def betting_screen(screen, textinput):
        '''Displays and handles the betting screen'''
        Gui.reset_elements()

        if GameManager.player.money < 100:
            GameManager.state = 'minigame'
            return
        else:
            GameManager.state = 'betting'

        #betting texts
        font = pygame.font.Font(None, 32)
        bet_amount_text = font.render("Bet Amount:", True, pygame.Color('black'))
        bet_amount_text_pos = (100, 600)
        bet_on_who_text = font.render(f"Bet on racer: {(UserInput.bet_racer_index + 1) if UserInput.bet_racer_index != None else 'Not selected yet'}", True, pygame.Color('black'))
        bet_on_who_text_pos = (100, 650)
        player_money_text = font.render("Player's Money: $" + str(GameManager.player.money), True, pygame.Color('black'))

        #display racers
        if not GameManager.racers_showcase.sprites():
            for i in range(5):
                racer = Racer(50 + i * 250, 100, CoreGame.char_set, i)
                racer.add(GameManager.racers_showcase)
        else:
            for racer in GameManager.racers:
                racer.update_image()
            GameManager.racers_showcase.draw(screen)

        #betting buttons
        for i in range(5):
            button = graphics_elements.Button(50 + i * 250, 300, 100, 80, (255, 255, 255), f"Bet on {i + 1}")
            Gui.buttons.append(button)
        
        textinput.update(CoreGame.events)

        #display all elements
        screen.blit(textinput.surface, (100 + bet_amount_text.get_width(), 600))
        screen.blit(bet_amount_text, bet_amount_text_pos)
        screen.blit(bet_on_who_text, bet_on_who_text_pos)
        screen.blit(player_money_text, (0, 0))

        UserInput.handle_betting_input(textinput)

    def racing_screen(dt, current_time, screen):
        '''Displays and handles the racing screen'''
        Gui.reset_elements()

        CoreGame.screen.blit(CoreGame.background.image, (0, 0))
        SpellManager.update(screen)
        GameManager.racers.update(dt, current_time, GameManager.state == 'racing')     
        GameManager.racers.draw(screen)
        #display player's money
        font = pygame.font.Font(None, 32)
        player_money_text = font.render("Player's Money: $" + str(GameManager.player.money), True, pygame.Color('black'))
        player_money_text_pos = (0, 0)
        screen.blit(player_money_text, player_money_text_pos)

        print(GameManager.check_end_game())
        if GameManager.check_end_game():
            GameManager.state = 'postgame'
        
    def postgame(screen):
        '''Displays and handles the postgame screen'''
        Gui.reset_elements()

        screen.blit(CoreGame.background.image, (0, 0))

        for racer in GameManager.racers:
            racer.update_image()
            screen.blit(racer.image, racer.rect)

        #display player's money
        font = pygame.font.Font(None, 32)
        player_money_text = font.render("Player's Money: $" + str(GameManager.player.money), True, pygame.Color('black'))
        screen.blit(player_money_text, (0, 0))

        Bookmaker.give_money(GameManager.finished_racers.sprites()[0])

        GameManager.racers.draw(screen)

        restart_button = graphics_elements.Button(300, 650, 400, 50, (255, 0, 0), "Restart", GameManager.reset)
        Gui.buttons.append(restart_button)  
    
    def minigame(screen):
        '''Displays and handles the minigame screen'''
        Gui.reset_elements()
        if GameManager.player.money >= 100:
            GameManager.state = 'betting'
            return

        #display player's money
        font = pygame.font.Font(None, 32)
        player_money_text = font.render("Player's Money: $" + str(GameManager.player.money), True, pygame.Color('black'))
        screen.blit(player_money_text, (400, 400))
        text = font.render("You don't have enough money to bet, play a minigame to get more money", True, pygame.Color('black'))
        screen.blit(text, (100, 450))

        #Minigame button
        minigame_button = graphics_elements.Button(300, 650, 400, 50, (255, 0, 0), "Minigame", Minigame.start)
        Gui.buttons.append(minigame_button)

    @staticmethod
    def start_game():
        '''Starts racing'''
        GameManager.state = "racing"
        BotManager.add_bots(random.randint(4, 10))
        SpellManager.generate_spells(random.randint(3, 5))
    
    @staticmethod
    def generate_racers(char_set):
        '''Generate 5 racers, each on their seperate lane'''
        for i in range(5):
            racer = Racer(CoreGame.background.start_point, CoreGame.background.first_lane_y_pos + i * 84, char_set, i)
            racer.add(GameManager.racers)        

    def countdown():
        '''Countdown from 3 to 1'''
        font = pygame.font.Font(None, 100)
        countdown_event = pygame.USEREVENT + 100000
        pygame.time.set_timer(countdown_event, 1000)  # Trigger the countdown event every second

        countdown_number = 3
        
        for event in CoreGame.events:
            if event.type == countdown_event:
                CoreGame.screen.blit(CoreGame.background.image, (0, 0))
                text = font.render(str(countdown_number), True, pygame.Color('white'))
                CoreGame.screen.blit(text, (CoreGame.background.width // 2, CoreGame.background.height // 2))
                pygame.display.update()
                countdown_number -= 1

        pygame.time.set_timer(countdown_event, 0)  # Stop the timer
        if countdown_number == 0:
            GameManager.racing = True

    @staticmethod
    def check_end_game():
        """Check if every racer has finished the race, if so, return true, else return false"""
        print(str(len(GameManager.finished_racers)) + ' ' + str(len(GameManager.racers)))

        if len(GameManager.finished_racers) == len(GameManager.racers) and len(GameManager.finished_racers) != 0:
            return True

    @staticmethod
    def reset():
        GameManager.racers.empty()
        GameManager.racers_showcase.empty()
        GameManager.finished_racers.empty()
        GameManager.state = 'betting'
        GameManager.generate_racers(CoreGame.char_set)
        GameManager.player.reset()

        BotManager.reset()

        Bookmaker.reset()
        
        UserInput.clicked_racer = None

class Spell(pygame.sprite.Sprite):
    hidden_spell_sprite = pygame.image.load("./Assets/Spells/hidden_spell.png")

    def __init__(self, pos, effect, id) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.effect = effect
        self.image = Spell.hidden_spell_sprite
        
        # Create a custom event to hide the spell after 1 second
        # Id is used to differentiate between the different spells (so that they don't all hide at the same time)
        self.hide_event = pygame.USEREVENT + id

    def update(self):
        # Check for the hide event
        for event in CoreGame.events:
            if event.type == self.hide_event:
                self.kill()
                pygame.time.set_timer(self.hide_event, 0)  # Stop the timer

    def apply(self, racer):
        self.effect(racer)

    def reveal(self):
        self.image = pygame.transform.scale(pygame.Surface.convert_alpha(pygame.image.load(f"./Assets/Spells/{self.effect.__name__}.png")), (32, 32))

        pygame.time.set_timer(self.hide_event, 500)  # 500 milliseconds

class SpellManager:
    spells = pygame.sprite.Group()

    start_spawning_spell_offset = 100
    stop_spawning_spell_offset = 100
    @staticmethod
    def generate_spells(num_spells):
        '''Generate @num_spells spells on each lane'''
        for lane in range(5):
            lane_y_pos = CoreGame.background.first_lane_y_pos + 128 - 35 + lane * 84
            #possible positions for spells to spawn, each 50px away from eachother
            possible_positions = list(range(CoreGame.background.start_point + SpellManager.start_spawning_spell_offset, CoreGame.background.end_point - SpellManager.stop_spawning_spell_offset, 50))
            for spell_index in range(num_spells):
                if not possible_positions:
                    break
                spell_x_pos = random.choice(possible_positions)
                possible_positions.remove(spell_x_pos)
                spell = Spell((spell_x_pos, lane_y_pos), SpellManager.pick_random_spell(), 10*lane + spell_index)     
                spell.add(SpellManager.spells)

    def update(screen):
        for spell in SpellManager.spells:
            spell.update()
            screen.blit(spell.image, spell.pos)

    @staticmethod
    def reset():
        SpellManager.spells.empty()

    @staticmethod
    def slow(racer):
        racer.speed_modifier -= 0.5

    @staticmethod
    def speed(racer):
        racer.speed_modifier += 0.8

    @staticmethod
    def flash(racer):
        '''Teleport the racer to a random position 100px around the racer's current position. This new pos should be at least 50px from current pos'''
        new_pos = random.randint(racer.rect.x - 100, racer.rect.x + 100)
        while abs(new_pos - racer.rect.x) < 50:
            new_pos = random.randint(racer.rect.x - 100, racer.rect.x + 100)
        racer.rect.x = new_pos

    def stun(racer):
        pygame.time.set_timer(racer.stun_event, 2000)
        racer.stunned = True

    def turnaround(racer):
        pygame.time.set_timer(racer.turnaround_event, 1000)
        racer.facing_right = False

    def tp_start(racer):
        racer.rect.x = CoreGame.background.start_point

    def tp_end(racer):
        racer.rect.x = CoreGame.background.end_point - racer.rect.width

    spell_effects =      [slow, speed, flash, stun, turnaround, tp_start, tp_end]
    spells_probability = [0.25, 0.25,  0.2,  0.149, 0.149,      0.001,    0.001]

    def pick_random_spell():
        return random.choices(SpellManager.spell_effects, weights=SpellManager.spells_probability)[0]

class Gui:
    buttons = []
    texts = []

    def reset_elements():
        Gui.buttons = []
        Gui.texts = []

    @staticmethod
    def update_buttons(screen):
        for button in Gui.buttons:
            screen.blit(button.image, button.rect)
            for event in CoreGame.events:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:            
                    mouse_pos = event.pos          
                    if button.rect.collidepoint(mouse_pos):
                        button.click()
                        #minigame button, on minigame finished we will add the money to the player
                        if button.text == 'Minigame':
                            GameManager.player.money += button.action_return_value

    def delete_button(button):
        Gui.buttons.remove(button)

class Bookmaker:
    total_money_bet = 0
    gave_money = False
    min_betting_amount = 100

    #Fair Share of Winning Money = (Amount Bet by the Gambler / Total Amount Bet on the Winning Racer) * Total Amount Bet by Losing Gamblers
    @staticmethod
    def give_money(winner_racer):
        if (Bookmaker.gave_money):
            return
        Bookmaker.gave_money = True
        money_bet_by_losing_gamblers = (Bookmaker.total_money_bet - winner_racer.get_total_money_bet())
        for (gambler, amount) in winner_racer.gambled_gamblers:
            gambler.money += amount + int((amount / winner_racer.get_total_money_bet()) * money_bet_by_losing_gamblers)

    def reset():
        Bookmaker.total_money_bet = 0
        Bookmaker.gave_money = False

class BotManager:
    bots = []

    @staticmethod
    def add_bots(num_bots):
        for i in range(num_bots):
            bot = Gambler(1000, 'Bot ' + str(i))
            bot.place_bet(GameManager.racers.sprites()[random.randint(0, len(GameManager.racers)-1)], random.randint(100, 300))
            BotManager.bots.append(bot)

    @staticmethod
    def print_all_bots_money():
        for bot in BotManager.bots:
            bot.print_money()

    @staticmethod
    def reset():
        BotManager.bots = []

class Racer(pygame.sprite.Sprite):
    def __init__(self, x, y, charset, lane) -> None:    
        pygame.sprite.Sprite.__init__(self)   

        self.walking_sprites = charset[lane]
        self.idle_sprites = charset[lane + 5]
        self.sprite_index = 0
        self.idle_sprite_index = 0         
        self.lane = lane

        self.image = self.idle_sprites[0]
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        if (self.rect.width > 64):
            self.rect.width = 64
        self.collide_rect = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.width, self.rect.height - 64)
        self.facing_right = True

        self.speed = 0
        self.speed_modifier = 1
        self.generate_speed_function()
        self.stunned = False
        self.stun_event = pygame.USEREVENT + self.rect.y

        self.turnaround_event = pygame.USEREVENT + 10 * self.rect.y

        #TODO: perk system
        #self.perk = perk
        # a list of (gambler, money_bet) tuples
        self.gambled_gamblers = []

        self.affected_spells = pygame.sprite.Group()

        self.running = False
        self.finished_race = False

    def update(self, dt, current_time, racing):
        self.check_if_finished()

        self.update_speed(current_time)

        self.collide_rect = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.width, self.rect.height - 64)

        for event in CoreGame.events:
            if event.type == self.stun_event:
                    self.stunned = False
                    pygame.time.set_timer(self.stun_event, 0)  # Stop the timer
            if event.type == self.turnaround_event:
                    self.facing_right = True
                    pygame.time.set_timer(self.turnaround_event, 0)  # Stop the timer

        #Check for collision with spells
        for spell in SpellManager.spells:
            if self.collide_rect.collidepoint(spell.pos):
                if not spell in self.affected_spells:
                    self.affected_spells.add(spell)
                    spell.apply(self)
                    spell.reveal()
                
        if racing and not self.finished_race:
            self.move(dt)
            
        self.update_image()

    def check_if_finished(self):
        if self.rect.x + self.rect.width >= CoreGame.background.end_point:
            print(str(self.lane) + " finished")
            self.finished_race = True
            self.running = False
            self.add(GameManager.finished_racers)

    # speed(t) = 3 + cos(at) + sin(bt) + sin(at)cos(bt)
    def generate_speed_function(self):
        self.speed_func_a = random.randint(-10, 10)
        self.speed_func_b = random.randint(-10, 10)
        
    def update_speed(self, current_time):
        # if the speed_modifier is less than 1, gradually change it to 1
        if self.speed_modifier < 1:
            self.speed_modifier += 0.005
        elif self.speed_modifier > 1:
            self.speed_modifier -= 0.005

        # speed = speed_modifier * 20 * (3 + cos(at) + sin(bt) + sin(at)cos(bt))
        # * 20 because the speed is too slow
        self.speed = self.speed_modifier * 20 * (3 + math.cos(self.speed_func_a * current_time) + math.sin(self.speed_func_b * current_time) + math.sin(self.speed_func_a * current_time) * math.cos(self.speed_func_b * current_time))

    def move(self, dt):
        if self.stunned:
            return
        
        if self.rect.x + self.rect.width >= CoreGame.background.end_point:
            self.rect.x = CoreGame.background.end_point - self.rect.width
        if self.rect.x <= CoreGame.background.start_point:
            self.rect.x = CoreGame.background.start_point

        self.running = True
        if self.facing_right:
            self.rect.x += self.speed * dt
        else:
            self.rect.x -= self.speed * dt

    def update_racing_sprites(self):
        current_frame = self.walking_sprites[self.sprite_index//10]
        self.image = current_frame

        self.sprite_index += 1
        if self.sprite_index >= len(self.walking_sprites) * 10:
            self.sprite_index = 0

    def update_idle_sprites(self):
        current_frame = self.idle_sprites[self.idle_sprite_index//15]
        self.image = current_frame

        self.idle_sprite_index += 1
        if self.idle_sprite_index >= len(self.idle_sprites) * 15:
            self.idle_sprite_index = 0

    def update_image(self):
        if self.running:
            self.update_racing_sprites()
        else:
            self.update_idle_sprites()

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            
    def get_total_money_bet(self):
        return sum([gambler[1] for gambler in self.gambled_gamblers])
    
class Gambler:
    '''A gambler is a person who bets on a racer'''
    def __init__(self, money, name = 'lol') -> None:
        self.name = name
        self.money = money
        self.bet_on_who = None

    def place_bet(self, racer, amount):
        if amount < 100:
            return False
        
        if (amount > self.money):
            print("You don't have enough money to bet that much")
            return False
        else:
            self.money -= amount
            racer.gambled_gamblers.append((self, amount))
            Bookmaker.total_money_bet += amount
            self.bet_on_who = racer
            return True
    
    def print_money(self):
        print(self.name + f"(who bet on racer {GameManager.racers.sprites().index(self.bet_on_who) + 1}) has $" + str(self.money))

    def reset(self):
        self.bet_on_who = None
        
class UserInput:
    bet_racer_index = None

    @staticmethod
    def handle_betting_input(textinput):
        for event in CoreGame.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if UserInput.bet_racer_index != None:
                    if GameManager.player.place_bet(GameManager.racers.sprites()[UserInput.bet_racer_index], int(textinput.value)):
                        GameManager.start_game()
                    
            #left click    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:            
                mouse_pos = event.pos          
                for button in Gui.buttons:          
                    if button.rect.collidepoint(mouse_pos):                    
                        UserInput.bet_racer_index = int(button.text[-1]) - 1