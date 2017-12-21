import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


running = True
while running:
    # keep loop running at right FPS
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for window close
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)

    pygame.display.flip()

