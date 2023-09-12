import pygame

WINDOW_NAME = "Zombie Killer Game - Creator: Hieu (Toni) github:tovanhieu "
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True


# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
ZOMBIES_SIZES = (50, 38)
ZOMBIE_SIZE_RANDOMIZE = (1,2) # for each new zombie, it will multiply the size with an random value between X and Y
ANGEL_SIZES = (50, 50)
ANGEL_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 3 # the frame of the zombies will change every X sec

# difficulty
GAME_DURATION = 60 # the game will last X sec
ZOMBIES_SPAWN_TIME = 1
ZOMBIES_MOVE_SPEED = {"min": 0.5, "max": 2}
ANGEL_PENALITY = 1 # will remove X of the score of the player (if you kills a angel)

# colors
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.4 # value between 0 and 1
SOUNDS_VOLUME = 5

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 30)
FONTS["medium"] = pygame.font.Font(None, 40)
FONTS["big"] = pygame.font.Font(None, 60)
