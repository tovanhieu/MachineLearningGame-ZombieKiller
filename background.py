import pygame
import image
from settings import *

class Background:
    def __init__(self):
        self.image = image.load("Assets/background.jpg", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")


    def draw(self, surface):
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")
