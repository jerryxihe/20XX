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
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("arwing.png").convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0

    def changespeed(self, x):
        """ Change the speed of the player"""
        self.change_x += x

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 361:
            self.rect.x = 361

class Laser(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("laser.png").convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_y = 0

    def update(self):
        self.change_y = -20
        self.rect.y += self.change_y
        if laser.rect.y < -42:
            laser.kill()

class Green_alien(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("green_alien.png").convert()

        #Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.change_x = 4

    def update(self):
        if self.rect.x <= 0:
            self.change_x = 4
        if self.rect.x >= 398:
            self.change_x = -4
        self.change_y = 2
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.y > 576:
            self.rect.y = -100

class Blue_alien(pygame.sprite.Sprite):

    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("blue_alien.png").convert()

        #Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        self.change_y = 2
        self.rect.y += self.change_y
        if self.rect.y > 576:
            self.rect.y = -100

pygame.init()

# Set the height and width of the screen
screen_width = 448
screen_height = 576
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("20XX")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()
green_alien_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
blue_alien_list = pygame.sprite.Group()
alien_list = pygame.sprite.Group()

for i in range(35):
    green_alien = Green_alien()
    green_alien.rect.x = random.randrange(screen_width)
    green_alien.rect.y = random.randrange(-200, -100)
    green_alien_list.add(green_alien)
    all_sprites_list.add(green_alien)

for i in range(35):
    blue_alien = Blue_alien()
    blue_alien.rect.x = random.randrange(screen_width)
    blue_alien.rect.y = random.randrange(-600, -500)
    blue_alien_list.add(blue_alien)
    all_sprites_list.add(blue_alien)

alien_list.add(blue_alien_list, green_alien_list)

arwing = Arwing(185, 475)
laser = Laser(-100, -100)

all_sprites_list.add(arwing)

laser_sound = pygame.mixer.Sound("laser.ogg")

# Create an empty array
star_list = []

# Loop 175 times and add a star in a random x,y position
for i in range(175):
    x = random.randrange(0, screen_width)
    y = random.randrange(0, screen_height)
    star_list.append([x, y])

score = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arwing.changespeed(-3)
            elif event.key == pygame.K_RIGHT:
                arwing.changespeed(3)
            elif event.key == pygame.K_SPACE:
                laser = Laser(arwing.rect.x + 40, arwing.rect.y)
                laser_list.add(laser)
                all_sprites_list.add(laser)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                arwing.changespeed(3)
            elif event.key == pygame.K_RIGHT:
                arwing.changespeed(-3)

    # --- Game logic should go here
    """if laser.rect.y >= 455:
        laser_sound.play()"""

    # This calls update on all the sprites
    all_sprites_list.update()

    # See if the laser has collided with anything.
    green_alien_hit_list = pygame.sprite.groupcollide(laser_list, green_alien_list, True, True)
    blue_alien_hit_list = pygame.sprite.groupcollide(laser_list, blue_alien_list, True, True)
    arwing_hit_list = pygame.sprite.spritecollide(arwing, alien_list, True)

    # Check the list of collisions.
    for green_alien_hit in green_alien_hit_list:
        score += 50

    for blue_alien_hit in blue_alien_hit_list:
        score += 100

    if len(arwing_hit_list) > 0:
        pygame.quit()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    # Process each star in the list
    for i in range(len(star_list)):

        # Draw the star
        pygame.draw.circle(screen, WHITE, star_list[i], 1)

        # Move the star down three pixels
        star_list[i][1] += 3

        # If the star has moved off the bottom of the screen
        if star_list[i][1] > screen_height:
            # Reset it just above the top
            y = random.randrange(-50, 0)
            star_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, screen_width)
            star_list[i][0] = x

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(str(score), True, WHITE)

    if score <= 100:
        screen.blit(text, [410, 3])
    if score > 100 and score < 999:
        screen.blit(text, [400, 3])
    if score >= 1000 and score < 9999:
        screen.blit(text, [390, 3])
    if score >= 10000:
        screen.blit(text, [380, 3])
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()