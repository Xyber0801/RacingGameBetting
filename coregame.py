import pygame
import random
import math
from minigame import Minigame
import graphics_elements
import utils
import constants as c
import gettext
import game_text_sources as gts
_ = gettext.gettext

class CoreGame:
    running = False

    events = None
    dt = 0
    background = None
    charset = None
    screen = None
    clock = None
    textinput = None

    @staticmethod
    def start(screen, clock, textinput, background, charset):
        '''Start the game'''
        locale = 'en_US' if gts.lg_count == 1 else 'vi_VN'
        I18N.change_locale(locale)

        CoreGame.background = background
        CoreGame.charset = charset
        CoreGame.screen = screen
        CoreGame.clock = clock
        CoreGame.textinput = textinput

        GameManager.init()

        print("start coregame")
        CoreGame.gameloop()
        

    def gameloop():
        running = True
        dt = 0
        while running:
            current_time = pygame.time.get_ticks() / 1000
            CoreGame.events = pygame.event.get()

            CoreGame.screen.fill((255,255,255))

            if GameManager.state == 'betting':
                GameManager.betting_screen(CoreGame.screen, CoreGame.textinput)
            elif GameManager.state == 'racing':
                GameManager.racing_screen(dt, current_time, CoreGame.screen)
            elif GameManager.state == 'postgame':
                GameManager.postgame(CoreGame.screen)
            elif GameManager.state == 'minigame':
                GameManager.minigame(CoreGame.screen)
            
            GameManager.update(CoreGame.screen)

            for event in CoreGame.events:
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            dt = CoreGame.clock.tick(60) / 1000
class GameManager:
    # 4 states: 'betting', 'racing', 'postgame', 'minigame'
    state = None

    player = None
    player_bet_amount = 0
    renaming = False
    renaming_who = None

    # A group of all the racers
    racers = pygame.sprite.Group()
    racers_showcase = pygame.sprite.Group()
    finished_racers = pygame.sprite.Group()

    @staticmethod
    def init():
        '''Initialize the game'''        
        GameManager.generate_racers(CoreGame.charset)
        GameManager.player = Gambler(c.money, 'Player')
        GameManager.state = 'betting'

    @staticmethod
    def update(screen):
        Gui.update_all_elements(screen)  
        if GameManager.finished_racers.sprites():
            GameManager.finished_racers.sprites()[0].winner = True
            winner_crown_pos = (GameManager.finished_racers.sprites()[0].headpos[0] - 16, GameManager.finished_racers.sprites()[0].headpos[1] - 32)
            CoreGame.screen.blit(c.winner_crown, winner_crown_pos)
     
    def betting_screen(screen, textinput):
        """Displays and handles the betting screen"""

        def rename(racer):
            GameManager.renaming = True
            GameManager.renaming_who = racer

        screen.blit(c.menu_background, (0, 0))

        if GameManager.renaming:
            for event in CoreGame.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Update racer's name on Enter key press
                        GameManager.renaming_who.name = textinput.value
                        textinput.value = ""
                        GameManager.renaming = False
                        break
                    elif event.key == pygame.K_ESCAPE:  # Cancel renaming on Escape key press
                        GameManager.renaming = False
                        break

            # Update text input with CoreGame events
            textinput.update(CoreGame.events)
            screen.blit(textinput.surface, (400, 600))

        def select_racer(racer):
            GameManager.player.bet_on_who = racer

        Gui.reset_elements()

        if GameManager.player.money < 100:
            GameManager.state = 'minigame'
            return
        else:
            GameManager.state = 'betting'

        #betting texts
        font = pygame.font.Font(None, 32)
        bet_amount_text = font.render(_("Bet Amount: {}").format(GameManager.player_bet_amount), True, pygame.Color('white'))
        bet_amount_text_pos = (100, 600)
        # Render the text
        bet_on_who_text = font.render(
            _("Bet on racer: {}").format(GameManager.player.bet_on_who.name if GameManager.player.bet_on_who is not None else _("Not selected yet")),
            True,
            pygame.Color('white')
        )
        bet_on_who_text_pos = (100, 650)
        player_money_text = font.render(
            _("Player's Money: ${}").format(GameManager.player.money),
            True,
            pygame.Color('white')
        )

        #display racers name
        for i in range(5):
            racer_name_text = font.render(
                GameManager.racers.sprites()[i].name,
                True,
                pygame.Color('white')
            )
            racer_name_text_pos = (50 + i * 250, 50)
            screen.blit(racer_name_text, racer_name_text_pos)

        #display racers
        if not GameManager.racers_showcase.sprites():
            for i in range(5):
                racer = Racer(50 + i * 250, 50, CoreGame.charset, i)
                racer.add(GameManager.racers_showcase)
        else:
            for racer in GameManager.racers_showcase:
                racer.update_image()
            GameManager.racers_showcase.draw(screen)

        #betting buttons and rename buttons
        for i in range(5):
            betting_button = graphics_elements.Button(50 + i * 250, 350, 100, 80, (255, 255, 255), f"Bet on {i + 1}", select_racer, GameManager.racers.sprites()[i])
            Gui.buttons.append(betting_button)

            # Create rename button
            rename_button = graphics_elements.Button(50 + i * 250, 450, 100, 80, (255, 255, 255), f"Rename {i + 1}", rename, GameManager.racers.sprites()[i])
            # Set button action to rename racer
            Gui.buttons.append(rename_button)
        
        #inscrease/decrease bet amount buttons
        increase_bet_amount_button = graphics_elements.Button(300, 575, 50, 50, (255, 255, 255), "+50", GameManager.increase_bet, 50)
        Gui.buttons.append(increase_bet_amount_button)
        decrease_bet_amount_button = graphics_elements.Button(350, 575, 50, 50, (255, 255, 255), "-50", GameManager.increase_bet, -50)
        Gui.buttons.append(decrease_bet_amount_button)

        #What others have bet
        if not BotManager.bots:
            BotManager.add_bots(random.randint(1, 4))

        if not Gui.infoboxes:
            for i in range(5):
                racer = GameManager.racers.sprites()[i]
                bet_amount_for_racer_infobox = graphics_elements.InfoBox(50 + i * 250, 200, 200, 150, _("Other gamblers have bet \n ${} on this racer.").format(racer.get_total_money_bet()))
                Gui.infoboxes.append(bet_amount_for_racer_infobox)

            # font = pygame.font.SysFont("Constantia", 15)
            # utils.renderTextCenteredAt(
            #     _("Other gamblers have bet \n ${} on this racer.").format(racer.get_total_money_bet()),
            #     font,
            #     pygame.Color("white"),
            #     100 + i * 250,
            #     200,
            #     CoreGame.screen,
            #     100
            # )

        #start button
        start_button = graphics_elements.Button(900, 650, 200, 50, (255, 0, 0), _("Start"), GameManager.start_game)
        Gui.buttons.append(start_button)

        #display all elements
        screen.blit(bet_amount_text, bet_amount_text_pos)
        screen.blit(bet_on_who_text, bet_on_who_text_pos)
        screen.blit(player_money_text, (0, 0))

    def racing_screen(dt, current_time, screen):
        '''Displays and handles the racing screen'''
        Gui.reset_elements()

        CoreGame.screen.blit(CoreGame.background.image, (0, 0))
        SpellManager.update(screen)
        GameManager.racers.update(dt, current_time, GameManager.state == 'racing')     
        #draw racers
        GameManager.racers.draw(screen)
        for racer in GameManager.racers:
            racer.draw_status_effect_sprite()
        
        #display player's money
        font = pygame.font.Font(None, 32)
        player_money_text = font.render(
            _("Player's Money: ${}").format(GameManager.player.money),
            True,
            pygame.Color('white')
        )
        player_money_text_pos = (0, 0)
        screen.blit(player_money_text, player_money_text_pos)

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
        player_money_text = font.render(
            _("Player's Money: ${}").format(GameManager.player.money),
            True,
            pygame.Color('white')
        )
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
        # Display player's money
        font = pygame.font.Font(None, 32)
        player_money_text = font.render(_("Player's Money: ${}").format(GameManager.player.money), True, pygame.Color('white'))
        screen.blit(player_money_text, (400, 400))

        text = font.render(_("You don't have enough money to bet, play a minigame to get more money"), True, pygame.Color('white'))
        screen.blit(text, (100, 450))

        # Minigame button
        minigame_button = graphics_elements.Button(300, 650, 400, 50, (255, 0, 0), _("Minigame"), Minigame.start)
        Gui.buttons.append(minigame_button)

    @staticmethod
    def start_game():
        '''Starts racing'''
        if (not GameManager.player.bet_on_who == None and GameManager.player.place_bet(GameManager.player.bet_on_who, GameManager.player_bet_amount)):
            GameManager.state = "racing"
            SpellManager.generate_spells(random.randint(3, 5))
    
    @staticmethod
    def generate_racers(charset):
        '''Generate 5 racers, each on their seperate lane'''
        for i in range(5):
            print(CoreGame.background)
            racer = Racer(CoreGame.background.start_point, CoreGame.background.first_lane_y_pos + i * 84, charset, i)
            racer.add(GameManager.racers)        

    @staticmethod
    def increase_bet(amount):
        GameManager.player_bet_amount += amount

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
        if len(GameManager.finished_racers) == len(GameManager.racers) and len(GameManager.finished_racers) != 0:
            return True

    @staticmethod
    def reset():
        GameManager.racers.empty()
        GameManager.racers_showcase.empty()
        GameManager.finished_racers.empty()
        GameManager.state = 'betting'
        GameManager.generate_racers(CoreGame.charset)
        GameManager.player.reset()

        BotManager.reset()

        Bookmaker.reset()


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
        racer.flat_speed_modifier -= 35

    @staticmethod
    def speed(racer):
        racer.flat_speed_modifier += 35

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
    bad_spells = [slow, stun, turnaround, tp_start]

    def pick_random_spell():
        return random.choices(SpellManager.spell_effects, weights=SpellManager.spells_probability)[0]

class BuffManager():
    def speed_buff(racer):
        '''Increase racer's speed by 10%'''
        racer.multiple_speed_modifier += 0.1

    def headstart(racer):
        '''Give the racer a headstart of 100px'''
        racer.rect.x += 100    

    def negate_bad_spell(racer):
        '''Negate the 1st bad spell that hits the racer'''
        racer.can_negate_bad_spell = True

    def fast_or_slow(racer):
        '''Increase or decrease the racer's speed by 10%'''
        if random.random() < 0.5:
            racer.multiple_speed_modifier += 0.1
        else:
            racer.multiple_speed_modifier -= 0.1
            
class Gui:
    buttons = []
    infoboxes = []

    def reset_elements():
        Gui.buttons = []
        Gui.infoboxes = []

    def update_all_elements(screen):
        Gui.update_buttons(screen)
        Gui.update_infoboxes(screen)

    def update_infoboxes(screen):
        for infobox in Gui.infoboxes:
            infobox.draw(screen)

    @staticmethod
    def update_buttons(screen):
        for button in Gui.buttons:
            button.update_image()
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
    def add_bots(num_extra_bots):
        #Place a bet on every racer (so that no racer have $0 bet on them)
        for i in range(5):
            bot = Gambler(1000, 'Bot ' + str(i))
            bot.place_bet(GameManager.racers.sprites()[i], random.randint(100, 300))
            BotManager.bots.append(bot)
        #Randomly places bet on racers
        for i in range(num_extra_bots):
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
        '''@charset: a list of 10 images, 5 for walking and 5 for idle
           @lane: the lane the racer is in, 0 is the first lane, 4 is the last lane
           @headpos: the position of the racer's head, used to put the crown on his head
        '''
        
        pygame.sprite.Sprite.__init__(self)   

        self.name = "Racer " + str(lane + 1) 

        self.walking_sprites = charset[lane]
        self.idle_sprites = charset[lane + 5]
        self.celebrate_sprites = charset[lane + 10]
        self.sprite_index = 0
        self.idle_sprite_index = 0         
        self.celebrate_sprites_index = 0
        self.lane = lane
        
        self.image = self.idle_sprites[0]
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        self.headpos_offset = charset[16+lane]       
        self.headpos = (self.rect.x + self.headpos_offset[0], self.rect.y + self.headpos_offset[1])
        self.rect.width = charset[15]
        self.collide_rect = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.width, self.rect.height - 64)
        self.facing_right = True

        self.speed = 0
        self.flat_speed_modifier = 0
        self.multiple_speed_modifier = 1
        self.generate_speed_function()

        #effects
        self.stunned = False
        self.stun_event = pygame.USEREVENT + self.rect.y
        self.can_negate_bad_spell = False

        self.turnaround_event = pygame.USEREVENT + 10 * self.rect.y

        #TODO: perk system
        #self.perk = perk
        # a list of (gambler, money_bet) tuples
        self.gambled_gamblers = []

        self.affected_spells = pygame.sprite.Group()

        self.running = False
        self.finished_race = False
        self.winner = False

    def update(self, dt, current_time, racing):
        self.check_if_finished()

        self.update_speed(current_time)

        self.collide_rect = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.width, self.rect.height - 64)
        
        if self.facing_right:
            self.headpos = (self.rect.x + self.headpos_offset[0], self.rect.y + self.headpos_offset[1])
        else:
            self.headpos = (self.rect.x + self.rect.width - self.headpos_offset[0], self.rect.y + self.headpos_offset[1])

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
                    if (spell.effect in SpellManager.bad_spells and self.can_negate_bad_spell):
                        self.can_negate_bad_spell = False
                    else:
                        self.affected_spells.add(spell)
                        spell.apply(self)
                    spell.reveal()
                
        if racing and not self.finished_race:
            self.move(dt)
                    
        self.update_image()

    def check_if_finished(self):
        if self.rect.x + self.rect.width >= CoreGame.background.end_point:
            self.finished_race = True
            self.running = False
            self.add(GameManager.finished_racers)

    # speed(t) = 3 + cos(at) + sin(bt) + sin(at)cos(bt)
    def generate_speed_function(self):
        self.speed_func_a = random.randint(-10, 10)
        self.speed_func_b = random.randint(-10, 10)
        
    def update_speed(self, current_time):
        if self.flat_speed_modifier < 0:      
            self.flat_speed_modifier += 0.25 
        elif self.flat_speed_modifier > 0:
            self.flat_speed_modifier -= 0.25 #

        # speed = multiple_speed_modifier(flat_speed_modifier + 20 * (3 + cos(at) + sin(bt) + sin(at)cos(bt)))
        # * 20 because the speed is too slow
        self.speed = self.multiple_speed_modifier * (self.flat_speed_modifier + 20 * (3 + math.cos(self.speed_func_a * current_time) + math.sin(self.speed_func_b * current_time) + math.sin(self.speed_func_a * current_time) * math.cos(self.speed_func_b * current_time)))

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
        current_frame = self.walking_sprites[self.sprite_index // 15]
        self.image = current_frame

        self.sprite_index += 1
        if self.sprite_index >= 15 * len(self.walking_sprites):  
            self.sprite_index = 0

    def update_idle_sprites(self):
        current_frame = self.idle_sprites[self.idle_sprite_index // 15]
        self.image = current_frame

        self.idle_sprite_index += 1
        if self.idle_sprite_index >= 15 * len(self.idle_sprites):
            self.idle_sprite_index = 0

    def update_celebration_sprites(self):
        current_frame = self.celebrate_sprites[self.celebrate_sprites_index // 15]
        self.image = current_frame

        self.celebrate_sprites_index += 1
        if self.celebrate_sprites_index >= 15 * len(self.celebrate_sprites):
            self.celebrate_sprites_index = 0

    def update_image(self):
        if self.running:
            self.update_racing_sprites()
        elif self.winner:
            self.facing_right = False
            self.update_celebration_sprites()
        else:
            self.update_idle_sprites()

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def draw_status_effect_sprite(self):
        if self.stunned:
            CoreGame.screen.blit(c.stun_effect, (self.headpos[0]-32, self.headpos[1]-32))
            return            

        if self.flat_speed_modifier > 0:
            CoreGame.screen.blit(c.speed_effect, (self.headpos[0] + 10, self.headpos[1]-32))
        elif self.flat_speed_modifier < 0:
            CoreGame.screen.blit(c.slow_effect, (self.headpos[0] + 10, self.headpos[1]-32))

    def get_total_money_bet(self):
        return sum([gambler[1] for gambler in self.gambled_gamblers])
    
class Gambler:
    '''A gambler is a person who bets on a racer'''
    def __init__(self, money, name = 'lol') -> None:
        self.name = name
        self.money = money
        self.bet_on_who = None

    def place_bet(self, racer, amount):
        '''Place a bet on a racer, return true if the bet is successful, else return false'''
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

class I18N:
    @staticmethod
    def change_locale(locale):
        global _
        locale_path = "./locales"
        translation = gettext.translation('base', locale_path, languages=[locale])
        translation.install()

        _ = translation.gettext