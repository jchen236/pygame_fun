# Game options/settings
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player props
PLAYER_ACC = 1.3
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 1.4
PLAYER_JUMP = 25

# Starting platforms
PLATFORM_LIST= [(0, HEIGHT - 40, WIDTH, 40),
                (WIDTH/2 - 50, HEIGHT * 3 / 4, 100, 20),
                (125, HEIGHT - 350, 100, 20),
                (250, 200, 100, 20),
                (175, 100, 50, 20)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE