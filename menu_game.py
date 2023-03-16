import pygame

pygame.init()
pygame.mixer.init()

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menu_items = ["Practice", "Games", "Setting", "Basketball", "Water", "Feed", "LEDs"]
        self.menu_font = pygame.font.Font(None, 50)
        self.menu_item_pos = [(100, 50), (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350)]

    def draw_menu(self):
        # display menu
        for i in range(len(self.menu_items)):
            text = self.menu_font.render(self.menu_items[i], True, (0, 255, 0))
            self.screen.blit(text, self.menu_item_pos[i])

