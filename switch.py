import pygame
from objects import *
vec = pygame.math.Vector2


class SwitchAndLEDs:
    def __init__(self, pos, radius, center, color, image_path):
        # circle components
        self.pos = pos
        self.radius = radius
        self.center = center
        self.color = color

        # add image to circle
        self.image_path = image_path
        self.image_surface = pygame.image.load(image_path)
        self.scaled_image_surface = pygame.transform.scale(self.image_surface, (radius * 2, radius * 2))
        self.image_rect = self.scaled_image_surface.get_rect()
        self.image_rect.center = center

    def draw_switch(self, screen):
        # draw circle
        result_collision = pygame.draw.circle(screen, self.color, self.pos, self.radius)
        screen.blit(self.scaled_image_surface, self.image_rect)
        return result_collision







