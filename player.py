import pygame
from objects import *
vec = pygame.math.Vector2


class Player:
    def __init__(self, pos, radius, center, color, wall, image_path):
        # circle components
        self.pos = pos
        self.radius = radius
        self.center = center
        self.color = color
        self.speed = 5
        self.wall = wall

        # add image to circle
        self.image_path = image_path
        self.image_surface = pygame.image.load(image_path)
        self.scaled_image_surface = pygame.transform.scale(self.image_surface, (radius * 2, radius * 2))
        self.image_rect = self.scaled_image_surface.get_rect()
        self.image_rect.center = center

    def update(self, key_pressed):
        # moving circle by keyboard
        new_pos = self.pos.copy()
        old_pos = new_pos
        if key_pressed[pygame.K_UP]:
            old_pos[1] = new_pos[1]
            old_pos[0] = new_pos[0]
            new_pos[1] -= self.speed
        elif key_pressed[pygame.K_DOWN]:
            old_pos[1] = new_pos[1]
            old_pos[0] = new_pos[0]
            new_pos[1] += self.speed
        elif key_pressed[pygame.K_LEFT]:
            old_pos[0] = new_pos[0]
            old_pos[1] = new_pos[1]
            new_pos[0] -= self.speed
        elif key_pressed[pygame.K_RIGHT]:
            old_pos[0] = new_pos[0]
            old_pos[1] = new_pos[1]
            new_pos[0] += self.speed

        if self.wall[0][0] + self.radius <= new_pos[0] <= self.wall[0][1] - self.radius and \
                self.wall[1][0] + self.radius <= new_pos[1] <= self.wall[1][1] - self.radius:
            self.pos = new_pos

        self.image_rect.center = new_pos
        return [new_pos, old_pos]

    def draw(self, screen):
        # draw circle
        result_collision = pygame.draw.circle(screen, self.color, self.pos, self.radius)
        screen.blit(self.scaled_image_surface, self.image_rect)
        return result_collision




