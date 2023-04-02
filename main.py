import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Moving Circle")

# Set the initial position and radius of the circle
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2
circle_radius = 20

# Set the speed at which the circle moves
circle_speed = 1

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the circle based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    elif keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    elif keys[pygame.K_UP]:
        circle_y -= circle_speed
    elif keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the circle on the screen
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
