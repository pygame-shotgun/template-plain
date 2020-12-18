import pygame

# Initialize Pygame subsystems
pygame.init()

print(pygame.font.get_fonts())

# Set screen size constants
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (500, 500)
FPS = 60  # Frames per second

# Default colors
BG_COLOR = pygame.Color("black")
FG_COLOR = pygame.Color("white")

# Setup screen and a clock
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("{{ title }}")
clock = pygame.time.Clock()

running = True

while running:
    # Get events
    events = pygame.event.get()
    # Check events (QUIT event)
    for event in events:
        if event.type == pygame.QUIT:
            # Clicked X from window title or closed otherwise.
            running = False
        if event.type == pygame.KEYDOWN:
            # Keypress events
            if event.key == pygame.K_q and event.mod & pygame.KMOD_CTRL:
                # CTRL-Q closes window.
                running = False

    # Wait for FPS to fill up. dt is frame time in seconds
    dt = clock.tick(FPS) / 1000.0

    # Clear screen
    screen.fill(BG_COLOR)

    # Copy hidden screen to visible screen
    pygame.display.flip()

pygame.quit()
