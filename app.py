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

pygame.init()
pygame.mixer.init()


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.caption = pygame.display.set_caption("The first test")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "The first game"
        #self.state_app = "practice"
        self.state_app = "LED"
        self.background_color = (255, 255, 255)
        self.image_path = 'dolphin.jpg'
        self.image_path_SWON = 'switch_ON.jpg'
        self.image_path_SWOFF = 'switch_OFF.png'
        self.image_path_LEDON = 'LED_ON.png'
        self.image_path_LEDOFF = 'LED_OFF.jpg'
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
        self.menu = Menu(width, height)

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
            if self.state_app == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2


                button_practice = self.menu.draw_button(self.menu.menu_item_pos[0], self.menu.menu_items[0])
                button_game = self.menu.draw_button(self.menu.menu_item_pos[1], self.menu.menu_items[1])
                button_basketball = self.menu.draw_button(self.menu.menu_item_pos[2], self.menu.menu_items[2])
                button_water = self.menu.draw_button(self.menu.menu_item_pos[3], self.menu.menu_items[3])
                button_feed = self.menu.draw_button(self.menu.menu_item_pos[4], self.menu.menu_items[4])
                button_LED = self.menu.draw_button(self.menu.menu_item_pos[5], self.menu.menu_items[5])
                button_setting = self.menu.draw_button(self.menu.menu_item_pos[6], self.menu.menu_items[6])

            elif self.state_app == "practice":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2
                        self.rect.color = self.colors[self.color_index]

                # clear the screen with the background color
                self.screen.fill(self.background_color)



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

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == self.change_color_event:
                        self.color_index = (self.color_index + 1) % 2
                        self.rect.color = self.colors[self.color_index]

                    # clear the screen with the background color
                self.screen.fill(self.background_color)

                # draw circle
                keys_pressed = pygame.key.get_pressed()
                self.circle.update(keys_pressed, )
                circle = self.circle.draw(self.screen)

                # draw switch OFF
                switch_OFF = self.switch_ON.draw_switch((self.screen))

                # draw LED OFF
                LED_OFF = self.LED_OFF.draw_switch(self.screen)

                if circle.colliderect(switch_OFF):
                    # draw switch ON
                    switch_ON = self.switch_OFF.draw_switch((self.screen))
                    LED_ON = self.LED_ON.draw_switch(self.screen)

            # update the display
            pygame.display.update()
            self.clock.tick(60)
