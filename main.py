import pygame

pygame.init()

# set the window size
width = 640
height = 480
size = (width, height)

# create a window
screen = pygame.display.set_mode(size)

# set the window title
pygame.display.set_caption("The first test")

# set the background color
background_color = (255, 255, 255)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # clear the screen with the background color
    screen.fill(background_color)

    # update the display
    pygame.display.update()
