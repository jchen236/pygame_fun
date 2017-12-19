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
lead_y_change = 0
FPS = 60
clock = pygame.time.Clock()

GAME_EXIT = False


while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         lead_x_change = 0
    if lead_x >= 800 or lead_x < 0 or lead_x >= 600 or lead_y < 0:
        GAME_EXIT = True
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, 10, 10])
    pygame.display.update()
    clock.tick(FPS)
        #print(event)

pygame.quit()
quit()
