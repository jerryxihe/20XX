#-------------------------------------------------------------------------------
# Name:        Capstone Project
# Purpose:
#
# Author:      Grant Yao and Jerry He
#
# Created:     15/05/2017
# Copyright:   (c) 1201835 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Arwing(pygame.sprite.Sprite):
    """def __init__(self):"""

pygame.init()

# Set the width and height of the screen [width, height]
size = (448, 576)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("20XX")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

arwing = pygame.image.load("arwing.png").convert()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arwing.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                arwing.changespeed(3, 0)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                arwing.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                arwing.changespeed(-3, 0)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    screen.blit(arwing, [185, 475])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()