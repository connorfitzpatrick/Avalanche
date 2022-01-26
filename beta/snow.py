import pygame
from constants import *
import random


class Snow(pygame.sprite.Sprite):
    """ Class that creates small snow particles for decorative effect"""
    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([2, 2])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)

    def update(self):
        """Updates location of snow particle"""
        self.rect.x += 1
        self.rect.y += 1

        # If snowflake wanders off right side of screen, respawn on the left
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0

        # If snowflake wanders off bottom side of screen, respawn on the top
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
