import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
pygame.display.update()
GAME_EXIT = False

while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True

    gameDisplay.fill(WHITE)
    pygame.display.update()
        #print(event)

pygame.quit()
quit()
