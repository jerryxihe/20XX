#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      0401824
#
# Created:     31/05/2017
# Copyright:   (c) 0401824 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
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
from math import sin,cos,pi,radians
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()

# Set the width and height of the screen [width, height]
size = (448, 576)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Red Alien")


alien = pygame.image.load("red_alien.png").convert()
center_of_rotation_x = 224-10
center_of_rotation_y = 0
radius = 30
angle = radians(0)  #pi/4 # starting angle 45 degrees
omega = 0.1 #Angular velocity
center = 0
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
    center +=1
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    x = center_of_rotation_x + radius * cos(angle) #Starting position x
    y = center_of_rotation_y - radius * sin(angle) #Starting position y
    screen.blit(alien, (x, y+center)) # Draw current x,y
    angle = angle + omega # New angle, we add angular velocity
    x = x + radius * omega * cos(angle + pi / 2) # New x
    y = y - radius * omega * sin(angle + pi / 2) # New y

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()