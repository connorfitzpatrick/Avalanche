"""
    Avalanche By Connor Fitzpatrick

    Run this file to start game.

    Avalanche is a verical-scroller game. The player wins by dropping to the
    bottommost platform. They lose if the avalanche touches them.

    The game starts with a main menu from which you can either begin the
    game or view instructions.

    The platforms are generated within random locations, the screen scrolls
    vertically as the player descends. I included wraparound so that if a
    player wanders off screen, they will reappear on the opposite side of
    the screen, but still on the same floor. I also added in music,
    sound when falling, win/lose screens, snowfall, a second level,
    backgrounds, and running animations. A sound will play when the
    user beats or loses a level as well.
"""

from player import Player
from snow import Snow
from level_01 import Level01
from level_02 import Level02
from level_03 import Level03
from constants import *
import pygame


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Set gaming window caption
    pygame.display.set_caption("Avalanche!")

    # Text fonts
    title_font = pygame.font.SysFont('Calibri', 45, True, False)
    menu_font = pygame.font.SysFont('Calibri', 36, True, False)
    description_font = pygame.font.SysFont('Calibri', 20, True, False)

    # Create the player
    player = Player()

    # Create all the levels
    level_list = [Level01(player), Level02(player), Level03(player)]

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    # Set player's spawning location and add it to the sprite list
    player.rect.x = 100
    player.rect.y = 299
    active_sprite_list.add(player)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Load music and play it continuously
    pygame.mixer.music.load(PATH_TO_SOUNDS / "background_music.wav")
    pygame.mixer.music.play(-1)

    # Loop until the user clicks the close button.
    done = False
    show_main = True
    show_instructions = False

    # group to store snowflakes for snowfall effect
    snow_list = pygame.sprite.Group()

    # generate and store snowflakes for snowfall effect
    for i in range(0, 50):
        snow = Snow()
        snow_list.add(snow)

    while not done and show_main:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_main = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Enter game loop if 'Start Game' text is clicked
                if SCREEN_WIDTH / 2 - 60 <= mouse[0] <= SCREEN_WIDTH / 2 \
                        + 60 and SCREEN_HEIGHT / 2 - 100 <= mouse[1] \
                        <= SCREEN_HEIGHT / 2 - 60:
                    show_main = False

                # Show instructions if 'Instructions' text is clicked
                if SCREEN_WIDTH / 2 - 150 <= mouse[0] <= SCREEN_WIDTH / 2 + \
                        150 and SCREEN_HEIGHT / 2 <= mouse[1] <= \
                        SCREEN_HEIGHT / 2 + 40:
                    show_instructions = True

                # If instructions are shown and the '<-- Back' text is
                # clicked, return to menu
                if show_instructions and 8 <= mouse[0] <= 200 and 648 \
                        <= mouse[1] <= 699:
                    show_instructions = False

                # End the game if 'Quit' text is clicked
                if SCREEN_WIDTH / 2 - 45 <= mouse[0] <= SCREEN_WIDTH / 2 + \
                        45 and SCREEN_HEIGHT / 2 + 100 <= mouse[1] \
                        <= SCREEN_HEIGHT / 2 + 140:
                    pygame.quit()

        screen.fill(LIGHT_BLUE)
        text = title_font.render("AVALANCHE!", False, WHITE)
        screen.blit(text, [100, 100])

        # Show instructions
        if show_instructions:
            text = description_font. \
                render("An avalanche is descending down "
                       "on your", False, WHITE)
            screen.blit(text, (10, 200))
            text = description_font. \
                render("position! Press the left and right "
                       "arrow", False, WHITE)
            screen.blit(text, (10, 225))
            text = description_font. \
                render("keys to move in the corresponding "
                       "direction.", False, WHITE)
            screen.blit(text, (10, 250))

            text = description_font. \
                render("Use the openings in each floor to descend",
                       False, WHITE)
            screen.blit(text, (10, 300))
            text = description_font. \
                render("the mountain before the avalanche reaches",
                       False, WHITE)
            screen.blit(text, (10, 325))
            text = description_font.render("you!", False, WHITE)
            screen.blit(text, (10, 350))

            # Render text as orange when mouse hovers over it
            if 8 <= mouse[0] <= 200 and 648 <= mouse[1] <= 699:
                text = menu_font.render("<-- Back", False, ORANGE)
            # Render text as white when mouse is not hovering over it
            else:
                text = menu_font.render("<-- Back", False, WHITE)

            screen.blit(text, (10, 650))

        # Return to main menu from instructions screen
        else:
            # Render text as orange when mouse hovers over it
            if SCREEN_WIDTH / 2 - 60 <= mouse[0] <= SCREEN_WIDTH / 2 + \
                    60 and SCREEN_HEIGHT / 2 - 100 <= mouse[
                    1] <= SCREEN_HEIGHT / 2 - 60:
                text = menu_font.render("START", False, ORANGE)
            # Render text as white when mouse isn't hovering over text
            else:
                text = menu_font.render("START", False, WHITE)
            screen.blit(text, (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 - 100))

            # Render text as orange when mouse hovers over it
            if show_instructions or SCREEN_WIDTH / 2 - 150 <= mouse[
                0] <= SCREEN_WIDTH / 2 + 150 and SCREEN_HEIGHT / \
                    2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40:
                text = menu_font.render("INSTRUCTIONS", False, ORANGE)
            # Render text as white when mouse isn't hovering over text
            else:
                text = menu_font.render("INSTRUCTIONS", False, WHITE)
            screen.blit(text, (SCREEN_WIDTH / 2 - 148, SCREEN_HEIGHT / 2))

            # Render text as orange when mouse hovers over it
            if SCREEN_WIDTH / 2 - 45 <= mouse[0] <= SCREEN_WIDTH / \
                    2 + 45 and SCREEN_HEIGHT / 2 + 100 <= mouse[
                    1] <= SCREEN_HEIGHT / 2 + 140:
                text = menu_font.render("EXIT", False, ORANGE)
            # Render text as white when mouse isn't hovering over text
            else:
                text = menu_font.render("EXIT", False, WHITE)
            screen.blit(text, (SCREEN_WIDTH / 2 - 45, SCREEN_HEIGHT /
                               2 + 100))

            text = description_font.render("Created By Connor Fitzpatrick",
                                           False, WHITE)
            screen.blit(text, [90, 660])

        # update and draw snow
        snow_list.update()
        snow_list.draw(screen)

        clock.tick(60)
        pygame.display.flip()

    level_is_over = False

    # Set mouse to invisible
    pygame.mouse.set_visible(False)

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            # Move player left or right if corresponding arrow key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()

            # Stop the player's movement if an arrow key is lifted
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If player drops below a certain height, shift everything up
        if player.rect.y >= 150:
            diff = player.rect.y - 200
            player.rect.y = 200
            current_level.shift_world_y(-diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # Calculate current position
        current_position = current_level.world_shift - \
            player.rect.height - player.rect.y

        # if player has beat the level, stop the player and avalanche.
        # Then notify the player
        if current_position <= current_level.level_limit:
            if not level_is_over:
                pygame.mixer.music.pause()
                pygame.mixer.Channel(1). \
                    play(pygame.mixer.Sound(PATH_TO_SOUNDS /
                                            "win_sound_effect.wav"))
            level_is_over = True
            current_level.avalanche.stop()
            pygame.mixer.Channel(0).stop()
            player.disable_movement()
            text = menu_font.render("You Win!", False, WHITE)
            screen.blit(text, [160, 250])

            # if game is over render the game over screen
            if current_level_no == len(level_list) - 1:
                screen.fill(WHITE)
                text = title_font.render("You Win!", False, BLACK)
                screen.blit(text, [135, 300])
            else:
                text = description_font. \
                    render("Press RETURN for Next Level", False, BLACK)
                screen.blit(text, [90, 375])

            # If return key is pressed, go to next level if there is one
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if current_level_no < len(level_list) - 1:
                        pygame.mixer.music.unpause()
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player.level = current_level
                        player.enable_movement()
                        level_is_over = False
                    else:
                        done = True

        # If the player and the avalanche collide, they lose. Show lose screen.
        if current_level.avalanche.is_hit():
            if not level_is_over:
                pygame.mixer.music.pause()
                pygame.mixer.Channel(1). \
                    play(pygame.mixer.Sound(PATH_TO_SOUNDS /
                                            "lose_sound_effect.wav"))
            level_is_over = True
            current_level.avalanche.rect.y = -3
            player.disable_movement()
            player.image.fill(WHITE)
            text = menu_font.render("You Lose!", False, BLACK)
            screen.blit(text, [170, 300])
            text = description_font.render("Press RETURN to restart",
                                           False, BLACK)
            screen.blit(text, [120, 375])

            # If return key to be pressed, restart the entire game.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.unpause()

                    # Create the player
                    player = Player()

                    # Create all the levels
                    level_list = [Level01(player), Level02(player),
                                  Level03(player)]

                    # Set the current level
                    current_level_no = 0
                    current_level = level_list[current_level_no]

                    active_sprite_list = pygame.sprite.Group()
                    player.level = current_level

                    # Set player's spawning location and add it to sprite list
                    player.rect.x = 100
                    player.rect.y = 299
                    active_sprite_list.add(player)

                    level_is_over = False

        # update and draw snow
        snow_list.update()
        snow_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
