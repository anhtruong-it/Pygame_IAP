import pygame

vec = pygame.math.Vector2

class Player():
    def __init__(self, pos, radius, color, wall):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.speed = 2
        self.wall = wall


    def update(self, key_pressed):
        new_pos = self.pos.copy()
        #self.pos = new_pos
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
        return [new_pos, old_pos]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


