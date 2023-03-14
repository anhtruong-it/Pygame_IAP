import pygame
import random
import time

vec = pygame.math.Vector2


class Objects:
    def __init__(self, pos, color, wall):
        self.pos = pos
        self.color = color
        self.wall = wall
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(pos, (100, 100))
        self.rect_center = 100 / 2
        self.rect.center = 640 // 2, 480 // 2

    def update(self, collided):
        new_pos = self.pos.copy()
        if self.wall[0][0] + self.rect_center <= new_pos[0] <= self.wall[0][1] - self.rect_center and \
                self.wall[1][0] + self.rect_center <= new_pos[1] <= self.wall[1][1] - self.rect_center:
            self.pos = new_pos

        if collided:
            x = random.randint(0, 600)
            y = random.randint(0, 450)
            self.pos = [x, y]
        return new_pos

    def draw(self, screen):
        rect = pygame.Rect(self.pos, (100, 100))
        result_collision = pygame.draw.rect(screen, self.color, rect)
        return [result_collision, [rect.x, rect.y]]

