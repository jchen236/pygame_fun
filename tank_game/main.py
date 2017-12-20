import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 10

gameDisplay = pygame.display.set_mode((800, 600))

gameDisplay.fill(BLUE)

pix = pygame.PixelArray(gameDisplay)
pix[10][10] = GREEN

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(FPS)