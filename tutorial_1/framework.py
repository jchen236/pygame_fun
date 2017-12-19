import pygame
import time
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Snake Game")

FPS = 60
clock = pygame.time.Clock()
BLOCK_SIZE = 10

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH / 2, DISPLAY_WIDTH / 2])

def gameLoop():
    lead_x = DISPLAY_WIDTH / 2
    lead_y = DISPLAY_HEIGHT / 2
    lead_x_change = 0
    lead_y_change = 0
    rand_apple_x = random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE)
    rand_apple_y = random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE)
    gameExit = False
    gameOver = False
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(WHITE)
            message_to_screen("Game over, press C to play again or Q to quit", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         lead_x_change = 0
        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(WHITE)
        pygame.draw.rect(gameDisplay, RED, [rand_apple_x, rand_apple_y, BLOCK_SIZE, BLOCK_SIZE])
        pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, BLOCK_SIZE, BLOCK_SIZE])
        pygame.display.update()
        clock.tick(FPS)
            #print(event)
    pygame.quit()
    quit()

gameLoop()