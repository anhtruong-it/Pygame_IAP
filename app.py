import pygame

from player import *
from objects import *
from menu_game import *
from switch import *
from math import *
from pygame.mixer import Sound

wall = ((0, 640), (0, 480))

# pre defined
width = 640
height = 480


pygame.mixer.init()


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.caption = pygame.display.set_caption("The first test")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "The first game"
        self.call_state = "menu"
        #self.state_app = "menu"
        #self.state_app = "practice"
        #self.state_app = "LED"
        self.background_color = (255, 255, 255)
        self.image_path = 'dolphin.jpg'
        self.image_path_SWON = 'switch_ON.jpg'
        self.image_path_SWOFF = 'switch_OFF.png'
        self.image_path_LEDOFF = 'LED_ON.jpg'
        self.image_path_LEDON = 'LED_OFF.png'
        self.switch_ON = SwitchAndLEDs([500, 100], 50, (500, 100), (0, 255, 0), self.image_path_SWON)
        self.switch_OFF = SwitchAndLEDs([500, 100], 50, (500, 100), (0, 255, 0), self.image_path_SWOFF)
        self.LED_ON = SwitchAndLEDs([300, 300], 50, (300, 300), (0, 255, 0), self.image_path_LEDON)
        self.LED_OFF = SwitchAndLEDs([300, 300], 50, (300, 300), (0, 255, 0), self.image_path_LEDOFF)
        self.circle = Player([100, 100], 50, (100, 100), (0, 255, 0), wall, self.image_path)
        self.rect = Objects([250, 300], (100, 100), (0, 0, 255), wall)
        self.change_color_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.change_color_event, 1000)
        self.color_index = 0
        self.colors = [(0, 0, 255), (0, 200, 0)]

        self.button_width = 120
        self.button_height = 50
        self.button_padding = 20

        button_name = ["Practice", "Games", "Basketball", "Water", "Feed", "LEDs", "Setting"]
        button_x = 100
        button_y = [50, 100, 150, 200, 250, 300, 350]
        self.button_practice = Menu(button_x,button_y[0], self.button_width, self.button_height, button_name[0], self)
        self.button_game = Menu(button_x, button_y[1], self.button_width, self.button_height, button_name[1], self)
        self.button_basketball = Menu(button_x, button_y[2], self.button_width, self.button_height, button_name[2], self)
        self.button_water = Menu(button_x,button_y[3], self.button_width, self.button_height, button_name[3], self)
        self.button_feed = Menu(button_x, button_y[4], self.button_width, self.button_height, button_name[4], self)
        self.button_LED = Menu(button_x, button_y[5], self.button_width, self.button_height, button_name[5], self)
        self.button_setting = Menu(button_x, button_y[6], self.button_width, self.button_height, button_name[6], self)

        self.button_return = Menu(0, 0, self.button_width, self.button_height, "menu", self)

    def win_game(self):
        # notification of the first test
        font = pygame.font.Font(None, 100)
        text_surface = font.render("You Win!", True, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (width // 2, height // 2)
        self.screen.blit(text_surface, text_rect)



    def run(self):
        hit = 0
        while self.running:

            if self.call_state == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2

                    a = self.button_practice.handle_event(event)
                    b = self.button_game.handle_event(event)
                    c = self.button_basketball.handle_event(event)
                    d = self.button_water.handle_event(event)
                    e = self.button_feed.handle_event(event)
                    g = self.button_LED.handle_event(event)
                    h = self.button_setting.handle_event(event)

                # clear the screen with the background color
                self.screen.fill((0, 0, 0))

                self.button_practice.draw_button(self.screen)
                self.button_game.draw_button(self.screen)
                self.button_basketball.draw_button(self.screen)
                self.button_water.draw_button(self.screen)
                self.button_feed.draw_button(self.screen)
                self.button_LED.draw_button(self.screen)
                self.button_setting.draw_button(self.screen)
                pygame.display.update()

            elif self.call_state == "Practice":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2
                        self.rect.color = self.colors[self.color_index]

                # clear the screen with the background color
                self.screen.fill(self.background_color)

                # draw return button
                self.button_return.draw_button(self.screen)
                a = self.button_return.handle_event(event)
                if a == "menu":
                    self.call_state = "menu"

                # draw circle
                keys_pressed = pygame.key.get_pressed()
                self.circle.update(keys_pressed,)
                circle = self.circle.draw(self.screen)

                # draw rect
                self.rect.update(False)
                rect = self.rect.draw(self.screen)[0]

                # check circle hit rect
                if circle.colliderect(rect) and hit < 5:
                    print("circle hit rect")
                    hit += 1
                    print(hit)
                    pygame.time.wait(100)
                    self.rect.update(True)

                # display notification
                if hit == 5:
                    self.win_game()
                pygame.display.update()

            elif self.call_state == "LEDs":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2
                        self.rect.color = self.colors[self.color_index]





                # clear the screen with the background color
                self.screen.fill(self.background_color)

                # draw return button
                self.button_return.draw_button(self.screen)
                self.button_return.handle_event(event)

                if event.type == pygame.KEYDOWN:
                    print("any key pressed")
                    switch_ON = self.switch_ON.draw_switch((self.screen))
                    LED_ON = self.LED_ON.draw_switch(self.screen)

                else:

                    # draw circle
                    keys_pressed = pygame.key.get_pressed()
                    self.circle.update(keys_pressed, )
                    circle = self.circle.draw(self.screen)

                    # draw switch OFF
                    switch_OFF = self.switch_OFF.draw_switch((self.screen))

                    # draw LED OFF
                    LED_OFF = self.LED_OFF.draw_switch(self.screen)

                    if circle.colliderect(switch_OFF):
                        # draw switch ON
                        switch_ON = self.switch_ON.draw_switch((self.screen))
                        LED_ON = self.LED_ON.draw_switch(self.screen)



                pygame.display.update()

            elif self.call_state == "Games":
                pass
                self.call_state = "menu"
            elif self.call_state == "Basketball":
                print("pass")
                self.call_state = "menu"
            elif self.call_state == "Water":
                print("pass")
                self.call_state = "menu"
            elif self.call_state == "Feed":
                print("pass")
                self.call_state = "menu"
            elif self.call_state == "Setting":
                print("pass")
                self.call_state = "menu"
            else:
                print("pass")
                self.call_state = "menu"

            # update the display
            pygame.display.update()
            self.clock.tick(60)
