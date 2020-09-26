#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Grant
#
# Created:     29/05/2017
# Copyright:   (c) Grant 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (448, 576)
screen = pygame.display.set_mode(size)


mouse_click = [0,0]

pygame.display.set_caption("Instructions")
pygame.mixer.music.load('Instructions.mp3')
pygame.mixer.music.play(-1)
background_image = pygame.image.load("lore.png").convert()


back = pygame.image.load('back.png')
back1 = pygame.image.load('back1.png')
instructions = pygame.image.load('instructions.png')
instructions1 = pygame.image.load('instructions1.png')


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
    # --- Game logic should go here
    time = (pygame.time.get_ticks()/1000)
    mouse = pygame.mouse.get_pos()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    screen.blit(background_image,[0,0])
    screen.blit(back,[330,505])
    if 330<mouse[0]<430 and 505<mouse[1]<555:
        screen.blit(back1,[330,505])
    if 330<mouse_click[0]<430 and 505<mouse_click[1]<555:
        import Menu

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()