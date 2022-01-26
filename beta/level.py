from constants import *
import pygame


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    platform_list = None
    snow_list = None

    player = None

    Avalanche = None

    # How far this world has been scrolled down
    world_shift = 0

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.snow_list = pygame.sprite.Group()
        self.player = player

        # Background Image
        self.background = None

    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(LIGHT_BLUE)
        screen.blit(self.background, (0, self.world_shift // 3))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def shift_world_y(self, shift_y):
        """ Scrolls everything up when the player moves down"""

        # Keep track of the shift amount
        self.world_shift += shift_y

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.y += shift_y
