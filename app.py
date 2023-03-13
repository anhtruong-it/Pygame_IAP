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
        self.rect = Objects([100, 100], (0, 0, 255), wall)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            # draw player
            keys_pressed = pygame.key.get_pressed()
            self.circle.update(keys_pressed)

            # clear the screen with the background color
            self.screen.fill(self.background_color)

            self.circle.draw(self.screen)

            self.rect.draw(self.screen)


            if self.circle.update(keys_pressed)[0] != self.circle.update(keys_pressed)[1]:
                print(self.circle.update(keys_pressed)[0], self.circle.update(keys_pressed)[1], self.rect.update())

            if self.circle.update(keys_pressed)[0] == self.rect.update():
                print("ok")


           # print(self.rect.draw(self.screen))







            # update the display
            pygame.display.update()


            self.clock.tick(60)