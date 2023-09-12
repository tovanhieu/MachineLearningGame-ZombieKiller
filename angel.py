import pygame
import random
import image
from settings import *
from zombie import Zombie

class Angel(Zombie):
    def __init__(self):
        #size
        random_size_value = random.uniform(ANGEL_SIZE_RANDOMIZE[0], ANGEL_SIZE_RANDOMIZE[1])
        size = (int(ANGEL_SIZES[0] * random_size_value), int(ANGEL_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        # self.images = [image.load(f"Assets/angel/{nb}.png", size=size, flip=moving_direction=="right") for nb in range(1, 7)] # load the ima0ges
        self.images = [image.load(f"Assets/angel/angel.png", size=size, flip=moving_direction=="right")] # load the image
        self.current_frame = 0
        self.animation_timer = 0
        

    def kill(self, zombies): # remove the zombie from the list
        zombies.remove(self)
        return -ANGEL_PENALITY
