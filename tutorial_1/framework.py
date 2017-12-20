import pygame
import time
import random

# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =  (255, 0, 0)
GREEN = (0, 155, 0)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
BLOCK_SIZE = 10
APPLE_THICKNESS = 30


# INITIALIZATION
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Snake Game")

img = pygame.image.load('./snakehead2.png')
font = pygame.font.SysFont(None, 25)
direction = "right"

def snake(snake_list):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    

    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))
    for xy in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, GREEN, [xy[0], xy[1], BLOCK_SIZE, BLOCK_SIZE])

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2 - screen_text.get_width()/2, DISPLAY_HEIGHT/2 - screen_text.get_height()/2])

def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    lead_x = DISPLAY_WIDTH / 2
    lead_y = DISPLAY_HEIGHT / 2
    lead_x_change = 10
    lead_y_change = 0
    rand_apple_x = round(random.randrange(0, DISPLAY_WIDTH - APPLE_THICKNESS))#/10.0) * 10.0
    rand_apple_y = round(random.randrange(0, DISPLAY_HEIGHT - APPLE_THICKNESS))#/10.0) * 10.0

    snake_list = []
    snake_length = 1

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(WHITE)
            message_to_screen("Game over, press C to play again or Q to quit", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
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
                    direction = "left"
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(WHITE)
        pygame.draw.rect(gameDisplay, RED, [rand_apple_x, rand_apple_y, APPLE_THICKNESS, APPLE_THICKNESS])
        
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_head:
                gameOver = True
        
        snake(snake_list)

        pygame.display.update()


        if lead_x > rand_apple_x - BLOCK_SIZE and lead_x < rand_apple_x + APPLE_THICKNESS and lead_y > rand_apple_y - BLOCK_SIZE and lead_y < rand_apple_y + APPLE_THICKNESS:
            rand_apple_x = round(random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE))
            rand_apple_y = round(random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE))
            snake_length += 1



        clock.tick(FPS)
            #print(event)
    pygame.quit()
    quit()



gameLoop()