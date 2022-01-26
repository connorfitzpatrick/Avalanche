from constants import *
from platforms import Platform
import pygame


class Avalanche(Platform):
    """ Avalanche above the player that they must avoid"""

    def __init__(self):
        """ Avalanche constructor."""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT + 100, WHITE)

        self.image = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.change_y = 4

        self.boundary_bottom = 0

        self.player = None
        self.level = None

    # update the position of the avalanche to simulate it falling
    def update(self):
        self.rect.y += self.change_y

    # stop the avalanche when player wins or loses the level
    def stop(self):
        self.change_y = 0

    # check if the avalanche collides into the player
    def is_hit(self):
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            return True
        return False
