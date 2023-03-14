import pygame
from player import *
from objects import *
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
        self.background_color = (255, 255, 255)
        self.circle = Player([100, 100], 50, (0, 255, 0), wall)
        self.rect = Objects([250, 300], (0, 0, 255), wall)
        self.change_color_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.change_color_event, 1000)

        self.color_index = 0
        self.colors = [(0, 0, 255), (0, 200, 0)]

    def win_game(self):
        font = pygame.font.Font(None, 100)
        text_surface = font.render("You Win!", True, (0, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (width // 2, height // 2)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        hit = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == self.change_color_event:
                    self.color_index = (self.color_index + 1) % 2
                    self.rect.color = self.colors[self.color_index]

            # draw player
            keys_pressed = pygame.key.get_pressed()
            self.circle.update(keys_pressed)

            # clear the screen with the background color
            self.screen.fill(self.background_color)
            circle = self.circle.draw(self.screen)

            self.rect.update(False)
            rect = self.rect.draw(self.screen)[0]

            if circle.colliderect(rect) and hit < 5:
                print("circle hit rect")
                hit += 1
                print(hit)
                pygame.time.wait(100)
                self.rect.update(True)

            if hit == 5:
                self.win_game()

            if self.circle.update(keys_pressed)[0] != self.circle.update(keys_pressed)[1]:
                print(self.circle.update(keys_pressed)[0], self.circle.update(keys_pressed)[1], self.rect.update(False))

            # update the display
            pygame.display.update()

            self.clock.tick(60)
