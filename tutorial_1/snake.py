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
BLOCK_SIZE = 20
APPLE_THICKNESS = 30


# INITIALIZATION
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Snake Game")

# Graphics and Fonts
icon = pygame.image.load('./apple.png')
pygame.display.set_icon(icon)
img = pygame.image.load('./snakehead3.png')
apple_img = pygame.image.load('./apple.png')
small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 50)
large_font = pygame.font.SysFont("comicsansms", 75)

# Initialize Direction
direction = "right"

# Start Screen
def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(WHITE)
        message_to_screen("Welcome to Slither", GREEN, -100, size="large")
        message_to_screen("The objective of the game is to eat red apple", BLACK, -30)
        message_to_screen("The more apples you eat, the longer you get", BLACK, 10)
        message_to_screen("If you run into yourself or the eges, you die!", BLACK, 50)
        message_to_screen("Press C to play, P to pause, or Q to quit", BLACK, 180)
        pygame.display.update()
        clock.tick(10)

def score(score):
    text = small_font.render("Score: " + str(score), True, BLACK)
    gameDisplay.blit(text, [0,0])

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(WHITE)
        message_to_screen("Paused", BLACK, -100, size="large")
        message_to_screen("Press C to continue or Q to quit", BLACK, 25)
        pygame.display.update()
        clock.tick(10)

# Draws the apple
def rand_apple_gen():
    rand_apple_x = round(random.randrange(0, DISPLAY_WIDTH - APPLE_THICKNESS))#/10.0) * 10.0
    rand_apple_y = round(random.randrange(0, DISPLAY_HEIGHT - APPLE_THICKNESS))#/10.0) * 10.0
    return rand_apple_x, rand_apple_y

# Draws the snake
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

# Helper for drawing text to screen
def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Draws text to screen
def message_to_screen(msg, color, y_displace=0, size = "small"):
    if size == "small":
        screen_text = small_font.render(msg, True, color)
    elif size == "med":
        screen_text = med_font.render(msg, True, color)
    elif size == "large":
        screen_text = large_font.render(msg, True, color)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2 - screen_text.get_width()/2, DISPLAY_HEIGHT/2 - screen_text.get_height()/2 + y_displace])

# Main game loop
def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = DISPLAY_WIDTH / 2
    lead_y = DISPLAY_HEIGHT / 2
    lead_x_change = BLOCK_SIZE/2
    lead_y_change = 0

    rand_apple_x, rand_apple_y = rand_apple_gen()
    snake_list = []
    snake_length = 1

    while not gameExit:
        # Game over logic. Quit or start again.
        while gameOver == True:
            gameDisplay.fill(WHITE)
            message_to_screen("Game Over", RED, -50, size = "large")
            message_to_screen("Press C to play again or Q to quit", BLACK, 50, size = "med")
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
                        direction = "right"
                        gameLoop()
        
        # Main game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -BLOCK_SIZE/2
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = BLOCK_SIZE/2
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -BLOCK_SIZE/2
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = BLOCK_SIZE/2
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        # Off screen detection
        if lead_x >= DISPLAY_WIDTH or lead_x < 0 or lead_y >= DISPLAY_HEIGHT or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(WHITE)

        # Draw the apple
        gameDisplay.blit(apple_img, (rand_apple_x, rand_apple_y))

        # Change the snake
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        # Detects if snake runs into itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                gameOver = True
        
        snake(snake_list)
        score(snake_length - 1)
        pygame.display.update()

        # Apple collision
        if lead_x > rand_apple_x - BLOCK_SIZE and lead_x < rand_apple_x + APPLE_THICKNESS and lead_y > rand_apple_y - BLOCK_SIZE and lead_y < rand_apple_y + APPLE_THICKNESS:
            rand_apple_x, rand_apple_y = rand_apple_gen()
            snake_length += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()