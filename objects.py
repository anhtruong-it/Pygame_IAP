import pygame

vec = pygame.math.Vector2

class Objects():
    def __init__(self, pos, color, wall):
        self.pos = pos
        self.color = color
        self.wall = wall
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect((200, 200), (100, 100))
        self.rect_center = 100/2


    def update(self):
        new_pos = self.pos.copy()
        if self.wall[0][0] + self.rect_center <= new_pos[0] <= self.wall[0][1] - self.rect_center and \
                self.wall[1][0] + self.rect_center <= new_pos[1] <= self.wall[1][1] - self.rect_center:
            self.pos = new_pos
        return new_pos

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        return [self.rect.x, self.rect.y]

    #def destroy_Rect(self):



