import pygame

pygame.init()
pygame.mixer.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Menu:
    def __init__(self, x, y, width, height, text, app):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 50)
        self.text_color = (0, 255, 0)
        self.hover_color = (0, 0, 255)
        self.surface = self.font.render(self.text, True, self.text_color)
        self.app = app

    def draw_button(self, screen):
        screen.blit(self.surface, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.surface = self.font.render(self.text, True, self.hover_color)
            else:
                self.surface = self.font.render(self.text, True, self.text_color)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.text != "restart":
                    self.app.call_state = self.text
                else:
                    self.app.call_in_game = self.text




