import pygame

pygame.init()
pygame.mixer.init()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menu_items = ["Practice", "Games", "Basketball", "Water", "Feed", "LEDs", "Setting"]
        self.menu_font = pygame.font.Font(None, 50)
        self.menu_item_pos = [(100, 50), (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350)]

    def create_button(self, pos, label):
        button_rect = pygame.Rect(pos, (50, 50))
        font = pygame.font.Font(None, 50)
        label_surf = font.render(label, True, GREEN)
        label_rect = label_surf.get_rect()
        label_rect.center = button_rect.center
        label_color = GREEN
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if button_rect.collidepoint(event.pos):
                        return True
                elif event.type == pygame.MOUSEMOTION:
                    if button_rect.collidepoint(event.pos):
                        label_color = BLUE
                    else:
                        label_color = GREEN

            pygame.draw.rect(self.screen, BLACK, button_rect)
            label_surf = font.render(label, True, label_color)
            self.screen.blit(label_surf, label_rect)

            pygame.display.flip()
    def draw_button(self, pos, name):
        self.draw_button(pos, name)



