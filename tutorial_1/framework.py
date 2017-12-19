import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
lead_x = 300
lead_y = 300
lead_x_change = 0
GAME_EXIT = False


while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
    lead_x += lead_x_change

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, 10, 10])
    pygame.display.update()
        #print(event)

pygame.quit()
quit()
