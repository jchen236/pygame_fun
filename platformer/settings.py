# Game options/settings
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 600
FPS = 30
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 1.3 
PLAYER_FRICTION = -0.15
PLAYER_GRAV = 1.4
PLAYER_JUMP = 30

# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2

# Starting platforms
PLATFORM_LIST= [(0, HEIGHT - 60),
                (WIDTH/2 - 50, HEIGHT * 3 / 4),
                (125, HEIGHT - 350),
                (250, 200),
                (175, 100)]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE