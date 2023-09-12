import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assets/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False
        #self.hand_tracking = HandTracking()


    def follow_mouse(self): # change the hand pos center at the mouse pos
        self.rect.center = pygame.mouse.get_pos()
        # self.hand_tracking.display_hand()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def on_animator(self, animators): # return a list with all animations that collide with the hand hitbox
        return [animator for animator in animators if self.rect.colliderect(animator.rect)]


    def kill_animators(self, animators, score, sounds): # will kill the animators that collide with the hand when the left mouse button is pressed
        if self.left_click: # if left click
            for animator in self.on_animator(animators):
                animator_score = animator.kill(animators)
                score += animator_score
                sounds["slap"].play()
                if animator_score < 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
