import pygame


class Platform(pygame.sprite.Sprite):
    """ Platform the user can land on """

    def __init__(self, width, height, color):
        """ Platform constructor. Assumes constructed with user passing in
            an what's defined at the top of this code.
            """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
