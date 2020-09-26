#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      0401824
#
# Created:     26/05/2017
# Copyright:   (c) 0401824 2017
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
blink = 0
flash = False



pygame.display.set_caption("20XX")
pygame.mixer.music.load('Menu.mp3')
pygame.mixer.music.play(-1)
background_image = pygame.image.load("blank.png").convert()


play = pygame.image.load('play.png')
play1 = pygame.image.load('play1.png')
instructionsbutton = pygame.image.load('instructions.png')
instructionsbutton1 = pygame.image.load('instructions1.png')
mouse_click = [0,0]

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
    if time >=2 and time <=2.5:
        background_image = pygame.image.load("0.png").convert()
    if time >2.5 and time <=3:
        background_image = pygame.image.load("1.png").convert()
    if time >3 and time <=3.5:
        background_image = pygame.image.load("2.png").convert()
    if time >3.5 and time <=4:
        background_image = pygame.image.load("3.png").convert()
    if time >4 and time <=4.5:
        background_image = pygame.image.load("4.png").convert()
    if time >4.5 and time <=5:
        background_image = pygame.image.load("5.png").convert()
    if time >5 and time <=5.5:
        background_image = pygame.image.load("6.png").convert()
    if time >5.5:
        background_image = pygame.image.load("full.png").convert()
        flash = True
    screen.blit(background_image, [0, 0])

    if flash == True:
        if blink <=30:
            blink +=1
            background_image = pygame.image.load("full.png").convert()
            screen.blit(background_image, [0, 0])
        if blink >30:
            blink +=1
            background_image = pygame.image.load("blank.png").convert()
            screen.blit(background_image, [0, 0])
        if blink ==40:
            blink =0

        screen.blit(play,[174,290])
        screen.blit(instructionsbutton,[174,360])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()