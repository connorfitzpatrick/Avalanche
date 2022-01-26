from constants import *
from spritesheet_functions import SpriteSheet
import pygame


class Player(pygame.sprite.Sprite):
    """ This class represents the object that the player controls."""

    def __init__(self):
        """ Constructor function for player"""

        # Call the parent's constructor
        super().__init__()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # Load the falling sound
        self.FALLING_SOUND = pygame.mixer.Sound(PATH_TO_SOUNDS /
                                                "falling_effect.wav")

        self.can_move = True

        self.walking_frames_l = []
        self.walking_frames_r = []

        self.direction = "R"

        # List of sprites we can bump against
        self.level = None

        sprite_sheet = SpriteSheet(PATH_TO_IMAGES / "spritesheet_man.png")

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 3, 26, 89)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(74, 0, 44, 92)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(153, 5, 48, 86)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(230, 9, 52, 80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(318, 4, 29, 85)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(391, 0, 46, 89)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(472, 5, 47, 86)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(550, 10, 50, 82)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 3, 26, 89)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(74, 0, 44, 92)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(153, 5, 48, 86)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(230, 9, 52, 80)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(318, 4, 29, 85)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(391, 0, 46, 89)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(472, 5, 47, 86)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(550, 10, 50, 82)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        if self.can_move:
            self.calc_grav()

            # Move left/right
            self.rect.x += self.change_x

            if self.direction == "R":
                frame = (self.rect.x // 34) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (self.rect.x // 34) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

            # See if we hit anything
            block_hit_list = pygame.sprite.\
                spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # If we are moving right,
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

            # Move up/down
            self.rect.y += self.change_y

            # wrap-around to left side of screen if player goes off right side
            if self.rect.x > SCREEN_WIDTH:
                self.rect.x = -self.rect.width + 1

            # wrap-around to right side of screen if player goes off left side
            if self.rect.x < -self.rect.width + 1:
                self.rect.x = SCREEN_WIDTH - 1

            # Check and see if we hit anything
            block_hit_list = pygame.sprite.\
                spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:

                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top

                # Stop our vertical movement
                self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
            self.stop_falling_sound()
        else:
            self.change_y += .35
            self.play_falling_sound()

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def disable_movement(self):
        """ Stop the player from being able to move when they win/lose."""
        self.can_move = False

    def enable_movement(self):
        """ Allow for the player to move again when a new level starts."""
        self.can_move = True

    def play_falling_sound(self):
        """ Plays the falling sound when the player descends"""
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(self.FALLING_SOUND)

    @staticmethod
    def stop_falling_sound():
        """ Stop falling sound when the player lands onto some platform."""
        if pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).stop()
