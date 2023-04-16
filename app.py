import pygame

from player import *
from objects import *
from menu_game import *
from switch import *
from memory_game import *
import RPi.GPIO as GPIO
import pigpio

from math import *
from pygame.mixer import Sound

wall = ((0, 640), (0, 480))

# pre defined
width = 640
height = 480

# cups position in memory game
origin_y = 150
playing_y = 300

pygame.mixer.init()


def event_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.caption = pygame.display.set_caption("The first test")
        self.background_color = (255, 255, 255)
        self.background_image = pygame.image.load("background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.background_image_practice = pygame.image.load("practice_background.jpg").convert()
        self.background_image_practice = pygame.transform.scale(self.background_image_practice, (width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "The first game"
        self.call_state = "menu"
        self.call_in_game = ""
        self.playing = False

        # create switches on LEDs menu
        self.image_path = 'practice_ball.jpg'
        self.image_path_SWON = 'switch_ON.jpg'
        self.image_path_SWOFF = 'switch_OFF.png'
        self.image_path_LEDOFF = 'LED_ON.jpg'
        self.image_path_LEDON = 'LED_OFF.png'
        self.switch_ON = SwitchAndLEDs([500, 100], 50, (500, 100), (0, 255, 0), self.image_path_SWON)
        self.switch_OFF = SwitchAndLEDs([500, 100], 50, (500, 100), (0, 255, 0), self.image_path_SWOFF)
        self.LED_ON = SwitchAndLEDs([300, 300], 50, (300, 300), (0, 255, 0), self.image_path_LEDON)
        self.LED_OFF = SwitchAndLEDs([300, 300], 50, (300, 300), (0, 255, 0), self.image_path_LEDOFF)

        # create circle and rect items
        self.player_x = 100
        self.player_y = 100
        self.circle = Player([self.player_x, self.player_y], 50, (100, 100), (0, 0, 0), wall, self.image_path)
        self.rect = Objects([250, 300], (100, 100), (0, 0, 255), wall)

        # set changed color in rect item
        self.change_color_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.change_color_event, 1000)
        self.color_index = 0
        self.colors = [(0, 0, 255), (0, 200, 0)]

        # create menu list
        button_name = ["Practice", "Memory Game", "Basketball", "Water", "Feed", "LEDs", "Setting", "Quit"]
        button_x = 100
        button_y = [50, 100, 150, 200, 250, 300, 350, 400]
        self.button_width = 120
        self.button_height = 50
        self.button_padding = 20
        self.button_practice = Menu(button_x, button_y[0], self.button_width, self.button_height, button_name[0], self)
        self.button_game = Menu(button_x, button_y[1], self.button_width, self.button_height, button_name[1], self)
        self.button_basketball = Menu(button_x, button_y[2], self.button_width, self.button_height, button_name[2],
                                      self)
        self.button_water = Menu(button_x, button_y[3], self.button_width, self.button_height, button_name[3], self)
        self.button_feed = Menu(button_x, button_y[4], self.button_width, self.button_height, button_name[4], self)
        self.button_LED = Menu(button_x, button_y[5], self.button_width, self.button_height, button_name[5], self)
        self.button_setting = Menu(button_x, button_y[6], self.button_width, self.button_height, button_name[6], self)
        self.button_quit = Menu(button_x, button_y[7], self.button_width, self.button_height, button_name[7], self)

        # create a menu return button
        self.button_return = Menu(0, 0, self.button_width, self.button_height, "menu", self)

        # create restart button
        self.button_restart = Menu(150, 0, self.button_width, self.button_height, "restart", self)

        # create start button
        self.button_start = Menu(300, 0, self.button_width, self.button_height, "start", self)

        # create button move ball
        self.button_move_ball = Menu(450, 0, self.button_width, self.button_height, "move", self)

        # create memory game components
        self.image_path_cup = 'cups.jpeg'
        self.image_path_ball = 'ball.jpeg'

        # create origin cups
        self.origin_cup1 = MemoryGame([300, origin_y], 75, (300, origin_y), (0, 255, 0), self.image_path_cup)
        self.origin_cup2 = MemoryGame([100, origin_y], 75, (100, origin_y), (0, 255, 0), self.image_path_cup)
        self.origin_cup3 = MemoryGame([500, origin_y], 75, (500, origin_y), (0, 255, 0), self.image_path_cup)

        # create playing cup
        self.playing_cup1 = MemoryGame([300, playing_y], 75, (300, playing_y), (0, 255, 0), self.image_path_cup)
        self.playing_cup2 = MemoryGame([100, playing_y], 75, (100, playing_y), (0, 255, 0), self.image_path_cup)
        self.playing_cup3 = MemoryGame([500, playing_y], 75, (500, playing_y), (0, 255, 0), self.image_path_cup)

        # create ball
        self.ball = MemoryGame([300, playing_y], 50, (300, playing_y), (0, 255, 0), self.image_path_ball)

        # # set up GPIO pin for LED
        # self.button_pin = 15
        # self.led_pin2 = 18
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # GPIO.setup(self.led_pin2, GPIO.OUT)
        # GPIO.output(self.led_pin2, GPIO.LOW)

    def win_practice_game(self):
        # notification of the first test
        font = pygame.font.Font(None, 100)
        text_surface = font.render("You Win!", True, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (width // 2, height // 2)
        self.screen.blit(text_surface, text_rect)

    def menu_event(self):
        for event in pygame.event.get():
            event_quit(event)

            # button functions
            self.button_practice.handle_event(event)
            self.button_game.handle_event(event)
            self.button_basketball.handle_event(event)
            self.button_water.handle_event(event)
            self.button_feed.handle_event(event)
            self.button_LED.handle_event(event)
            self.button_setting.handle_event(event)
            self.button_quit.handle_event(event)

        # clear the screen with the background color
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image, (0,0))

        # draw menu buttons
        self.button_practice.draw_button(self.screen)
        self.button_game.draw_button(self.screen)
        self.button_basketball.draw_button(self.screen)
        self.button_water.draw_button(self.screen)
        self.button_feed.draw_button(self.screen)
        self.button_LED.draw_button(self.screen)
        self.button_setting.draw_button(self.screen)
        self.button_quit.draw_button(self.screen)

    def practice_event(self):
        self.circle.free_move = True
        for event in pygame.event.get():
            self.button_return.handle_event(event)
            self.button_restart.handle_event(event)
            event_quit(event)
            if event.type == self.change_color_event:
                self.color_index = (self.color_index + 1) % 2
                self.rect.color = self.colors[self.color_index]

        # clear the screen with the background color
        self.screen.fill(self.background_color)
        self.screen.blit(self.background_image_practice, (0, 0))

        # draw return button
        self.button_return.draw_button(self.screen)

        # draw restart button
        self.button_restart.draw_button(self.screen)

        # draw circle
        # keys_pressed = pygame.key.get_pressed()
        self.circle.update()
        circle = self.circle.draw(self.screen)

        # draw rect
        self.rect.update(False)
        rect = self.rect.draw(self.screen)[0]
        pygame.display.update()
        return [circle, rect]

    def hit(self, hit, circle, rect):
        if circle.colliderect(rect) and hit < 5:
            hit += 1
            print("circle hit rect = ", hit)
            pygame.time.wait(100)
            self.rect.update(True)
        elif hit == 5:
            self.win_practice_game()

        return hit

    def hit_leds(self, circle, rect):
        if circle.colliderect(rect):
            print("circle hit LEDs")
            self.circle.stop = True

    def led_event(self):
        self.circle.free_move = False
        for event in pygame.event.get():
            self.button_return.handle_event(event)
            self.button_restart.handle_event(event)
            event_quit(event)

        # clear the screen with the background color
        self.screen.fill(self.background_color)

        # draw return button
        self.button_return.draw_button(self.screen)

        # draw restart button
        self.button_restart.draw_button(self.screen)

        # draw circle
        # keys_pressed = pygame.key.get_pressed()
        self.circle.update()
        circle = self.circle.draw(self.screen)

        # draw switch OFF
        switch_OFF = self.switch_OFF.draw_switch(self.screen)

        # draw LED OFF
        LED_OFF = self.LED_OFF.draw_switch(self.screen)

        # Set pin numbering mode to BCM
        GPIO.setmode(GPIO.BCM)

        # Set up GPIO pins for output
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(25, GPIO.IN)

        # Set the output value to high (0.0V)
        GPIO.output(18, GPIO.LOW)

        if circle.colliderect(switch_OFF):
            # draw switch ON
            switch_ON = self.switch_ON.draw_switch(self.screen)
            LED_ON = self.LED_ON.draw_switch(self.screen)
            # Set the output value to high (3.3V)
            GPIO.output(18, GPIO.HIGH)

        if GPIO.input(25) == GPIO.HIGH:
            # Set the output value to high (3.3V)
            GPIO.output(18, GPIO.HIGH)

        if self.circle.keys:
            switch_ON = self.switch_ON.draw_switch(self.screen)
            LED_ON = self.LED_ON.draw_switch(self.screen)
            # GPIO.output(self.led_pin, GPIO.HIGH)

        self.hit_leds(circle, LED_OFF)

        pygame.display.update()

    def restart_event(self, hit):
        hit = 0
        self.call_in_game = ""
        print("restart")
        if self.call_state == "Practice":
            self.circle.restart_default_player()
        elif self.call_state == "LEDs":
            self.circle.restart_random_player()
            self.circle.stop = False
        elif self.call_state == "Memory Game":
            self.playing = False
        return hit

    def move_ball(self):
        self.call_in_game = ""
        print("ball moved")
        self.ball.update_ball(True)

    def cup_draw(self):
        for event in pygame.event.get():
            self.button_return.handle_event(event)
            self.button_restart.handle_event(event)
            self.button_start.handle_event(event)
            self.button_move_ball.handle_event(event)
            event_quit(event)

        # clear the screen with the background color
        self.screen.fill(self.background_color)

        # draw return button
        self.button_return.draw_button(self.screen)

        # draw restart button
        self.button_restart.draw_button(self.screen)

        # draw start button
        self.button_start.draw_button(self.screen)

        # draw move ball button
        self.button_move_ball.draw_button(self.screen)

        # draw ball
        self.ball.update_ball(False)
        self.ball.draw_cup_ball(self.screen)

        # draw cups
        if not self.playing:
            self.origin_cup1.draw_cup_ball(self.screen)
            self.origin_cup2.draw_cup_ball(self.screen)
            self.origin_cup3.draw_cup_ball(self.screen)
        else:
            self.playing_cup1.draw_cup_ball(self.screen)
            self.playing_cup2.draw_cup_ball(self.screen)
            self.playing_cup3.draw_cup_ball(self.screen)

    def run(self):
        # GPIO.add_event_detec(self.button_pin, GPIO.FALLING, callback=self.button_pressed, bouncetime=300)
        # GPIO.add_event_detec(self.button_pin, GPIO.RISING, callback=self.button_released, bouncetime=300)

        hit = 0
        while self.running:
            if self.call_state == "menu":
                GPIO.cleanup()
                self.menu_event()
                pygame.display.update()

            elif self.call_state == "Practice":
                if self.call_in_game == "restart":
                    hit = self.restart_event(hit)
                hits = self.practice_event()
                hit = self.hit(hit, hits[0], hits[1])

            elif self.call_state == "LEDs":
                if self.call_in_game == "restart":
                    self.restart_event(hit)
                self.led_event()
            elif self.call_state == "Memory Game":
                if self.call_in_game == "start":
                    self.playing = True
                if self.call_in_game == "restart":
                    self.restart_event(0)
                if self.call_in_game == "move":
                    self.move_ball()
                    print([self.ball.pos, self.ball.center, self.ball.image_rect.center])

                self.cup_draw()
            elif self.call_state == "Basketball":
                print("Basketball")
                self.call_state = "menu"
            elif self.call_state == "Water":
                print("Water")
                self.call_state = "menu"
            elif self.call_state == "Feed":
                print("Feed")
                self.call_state = "menu"
            elif self.call_state == "Setting":
                print("Setting")
                self.call_state = "menu"
            else:
                print("quit")
                GPIO.cleanup()
                self.running = False

            # update the display
            pygame.display.update()
            self.clock.tick(60)
