import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up assets
game_folder = os.path.dirname("/Users/jimmychen/Desktop/Cornell_2017-2018_Fall/WinterWork/pygames/platform_game/")
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p2_stand.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()

