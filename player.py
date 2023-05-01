import random

from objects import *
from switch import *
#import RPi.GPIO as GPIO


class Player:
    def __init__(self, pos, radius, center, color, wall, image_path):
        # circle components
        self.pos = pos
        self.radius = radius
        self.center = center
        self.color = color
        self.speed = 10
        self.wall = wall

        # add image to circle
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image_surface = self.image.convert_alpha()
        self.image_surface.fill((0, 0, 0, 0))
        self.scaled_image_surface = pygame.transform.scale(self.image_surface, (radius * 2, radius * 2))
        self.image_rect = self.scaled_image_surface.get_rect()
        self.image_rect.center = center

        self.free_move = True
        self.keys = False

        # Set up GPIO
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(25, GPIO.IN)
        # GPIO.setup(23, GPIO.IN)
        # GPIO.setup(24, GPIO.IN)
        # GPIO.setup(17, GPIO.IN)

    def update(self, key_pressed):
        # moving circle by keyboard
        new_pos = self.pos.copy()
        # Set up GPIO
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(25, GPIO.IN)
        # GPIO.setup(23, GPIO.IN)
        # GPIO.setup(24, GPIO.IN)
        # GPIO.setup(17, GPIO.IN)
        if self.free_move:
            if key_pressed[pygame.K_UP]:
                new_pos[1] -= self.speed
            elif key_pressed[pygame.K_DOWN]:
                new_pos[1] += self.speed
            elif key_pressed[pygame.K_LEFT]:
                new_pos[0] -= self.speed
            elif key_pressed[pygame.K_RIGHT]:
                new_pos[0] += self.speed
            # print("not GPIO.input(BUTTON_UP)",not GPIO.input(BUTTON_UP))
            # print("not GPIO.input(BUTTON_DOWN)",not GPIO.input(BUTTON_DOWN))
            # print("not GPIO.input(BUTTON_LEFT)",not GPIO.input(BUTTON_LEFT))
            # print("not GPIO.input(BUTTON_RIGHT)",not GPIO.input(BUTTON_RIGHT))
            # Check for button presses

            # if GPIO.input(17) == GPIO.HIGH:
            #     new_pos[0] += self.speed
            #     print("move right")
            # if GPIO.input(23) == GPIO.HIGH:
            #     new_pos[1] += self.speed
            #     print("move down")
            # if GPIO.input(24) == GPIO.HIGH:
            #     new_pos[0] -= self.speed
            #     print("move left")
            # if GPIO.input(25) == GPIO.HIGH:
            #     new_pos[1] -= self.speed
            #     print("move up")

        else:
            # if GPIO.input(25) == GPIO.HIGH:
            #     if 200 <= new_pos[0] <= 400 and 385 <= new_pos[1] <= 395:
            #         new_pos[1] = 390
            #     else:
            #         new_pos[1] -= self.speed
            # elif GPIO.input(23) == GPIO.HIGH:
            #     if 200 <= new_pos[0] <= 400 and 195 <= new_pos[1] <= 220:
            #         new_pos[1] = 210
            #         # self.stop = False
            #     else:
            #         new_pos[1] += self.speed
            #
            # elif GPIO.input(24) == GPIO.HIGH:
            #     if 390 <= new_pos[0] <= 400 and 195 <= new_pos[1] <= 385:
            #         new_pos[0] = 400
            #     else:
            #         new_pos[0] -= self.speed
            #
            # elif GPIO.input(17) == GPIO.HIGH:
            #     if 200 <= new_pos[0] <= 206 and 195 <= new_pos[1] <= 385:
            #         new_pos[0] = 205
            #     else:
            #         new_pos[0] += self.speed

            if key_pressed[pygame.K_UP]:
                if 200 <= new_pos[0] <= 400 and 385 <= new_pos[1] <= 395:
                    new_pos[1] = 390
                else:
                    new_pos[1] -= self.speed

            elif key_pressed[pygame.K_DOWN]:
                if 200 <= new_pos[0] <= 400 and 195 <= new_pos[1] <= 220:
                    new_pos[1] = 210
                    self.stop = False
                else:
                    new_pos[1] += self.speed

            elif key_pressed[pygame.K_LEFT]:
                if 390 <= new_pos[0] <= 400 and 195 <= new_pos[1] <= 385:
                    new_pos[0] = 400
                else:
                    new_pos[0] -= self.speed

            elif key_pressed[pygame.K_RIGHT]:
                if 200 <= new_pos[0] <= 206 and 195 <= new_pos[1] <= 385:
                    new_pos[0] = 205
                else:
                    new_pos[0] += self.speed

        if self.wall[0][0] + self.radius <= new_pos[0] <= self.wall[0][1] - self.radius and \
                self.wall[1][0] + self.radius <= new_pos[1] <= self.wall[1][1] - self.radius:
            self.pos = new_pos

        self.image_rect.center = new_pos
        return [new_pos]

    def draw(self, screen):
        # draw circle
        result_collision = pygame.draw.circle(screen, self.color, self.pos, self.radius)
        screen.blit(self.scaled_image_surface, self.image_rect)
        return result_collision

    def restart_default_player(self):
        self.pos = [100, 100]

    def restart_random_player(self):
        x = random.choice([i for i in range(100, 600) if i < 190 or 390 < i < 400 or i > 550])
        y = random.choice([i for i in range(200, 400) if i < 300 or i > 390])
        self.pos = [x, y]






