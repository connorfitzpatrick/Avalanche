from platforms import Platform
from level import Level
from avalanche import Avalanche
from constants import *
import random
import pygame


# Create platforms for the level
class Level02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load(PATH_TO_IMAGES /
                                            "mountain_background_2.png"
                                            ).convert()
        self.background.set_colorkey(WHITE)

        level = []
        platform_height = 300

        # create random floor types
        for i in range(0, 20):
            level_type = random.randint(0, 2)
            if level_type == 0:
                # create floor with only one opening
                opening_start = random.randint(0, 400)
                level.append([opening_start, 25, 0, platform_height])
                level.append([SCREEN_WIDTH - (opening_start + OPENING_WIDTH),
                              25, opening_start + OPENING_WIDTH,
                              platform_height])

            else:
                # create floor with two openings
                first_opening_start = random.randint(0, 200)
                first_opening_end = first_opening_start + OPENING_WIDTH
                second_opening_start = random.randint(first_opening_start +
                                                      OPENING_WIDTH + 100, 400)
                second_opening_end = second_opening_start + OPENING_WIDTH

                level.append([first_opening_start, 25, 0, platform_height])
                level.append([second_opening_start - first_opening_end, 25,
                              first_opening_end, platform_height])
                level.append([SCREEN_WIDTH - second_opening_end, 25,
                              second_opening_end, platform_height])

            platform_height += 150

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1], BLACK)
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Create last floor
        end_floor = Platform(SCREEN_WIDTH, 25, GOLD)
        end_floor.rect.x = 0
        end_floor.rect.y = platform_height
        self.platform_list.add(end_floor)

        # Set level_limit equal to the lowermost floor
        self.level_limit = -platform_height

        # Add custom avalanche
        self.avalanche = Avalanche()
        self.avalanche.rect.x = 0
        self.avalanche.rect.y = -SCREEN_HEIGHT
        self.avalanche.boundary_bottom = 2000
        self.avalanche.change_y = 3
        self.avalanche.player = self.player
        self.avalanche.level = self
        self.platform_list.add(self.avalanche)
