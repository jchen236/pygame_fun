import pygame
import random
from settings import *


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


running = True
while running:
    # keep loop running at right FPS
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for window close
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
 
pygame.quit()
