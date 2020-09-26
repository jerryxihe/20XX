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

def game(ship_type):
    import pygame
    import random
    import time
    from Lose_Function import lose
    from math import sin, cos, pi, radians

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

            from Select_Char_Function import select_ship

            if ship_type == "classic":
                self.image = pygame.image.load("classic_body.png").convert()
            elif ship_type == "space":
                self.image = pygame.image.load("space_body.png").convert()
            elif ship_type == "steel":
                self.image = pygame.image.load("steel_body.png").convert()
            elif ship_type == "kappapride":
                self.image = pygame.image.load("kappapride_body.png").convert()
            elif ship_type == "ice":
                self.image = pygame.image.load("ice_body.png").convert()
            elif ship_type == "victorious":
                self.image = pygame.image.load("victorious_body.png").convert()
            elif ship_type == "cool":
                self.image = pygame.image.load("cool_body.png").convert()

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

            if self.rect.x < 27:
                self.rect.x = 27
            if self.rect.x > 388:
                self.rect.x = 388

    class Left_wing(pygame.sprite.Sprite):
        """ The class is the player-controlled sprite. """

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            if ship_type == "classic":
                self.image = pygame.image.load("classic_leftwing.png").convert()
            elif ship_type == "space":
                self.image = pygame.image.load("space_leftwing.png").convert()
            elif ship_type == "steel":
                self.image = pygame.image.load("steel_leftwing.png").convert()
            elif ship_type == "kappapride":
                self.image = pygame.image.load("kappapride_leftwing.png").convert()
            elif ship_type == "ice":
                self.image = pygame.image.load("ice_leftwing.png").convert()
            elif ship_type == "victorious":
                self.image = pygame.image.load("victorious_leftwing.png").convert()
            elif ship_type == "cool":
                self.image = pygame.image.load("cool_leftwing.png").convert()

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

    class Right_wing(pygame.sprite.Sprite):
        """ The class is the player-controlled sprite. """

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            if ship_type == "classic":
                self.image = pygame.image.load("classic_rightwing.png").convert()
            elif ship_type == "space":
                self.image = pygame.image.load("space_rightwing.png").convert()
            elif ship_type == "steel":
                self.image = pygame.image.load("steel_rightwing.png").convert()
            elif ship_type == "kappapride":
                self.image = pygame.image.load("kappapride_rightwing.png").convert()
            elif ship_type == "ice":
                self.image = pygame.image.load("ice_rightwing.png").convert()
            elif ship_type == "victorious":
                self.image = pygame.image.load("victorious_rightwing.png").convert()
            elif ship_type == "cool":
                self.image = pygame.image.load("cool_rightwing.png").convert()

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

            if self.rect.x < 60:
                self.rect.x = 60
            if self.rect.x > 421:
                self.rect.x = 421

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
            if self.rect.y < -42:
                self.kill()

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
                self.kill()

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
                self.kill()

            number = random.randrange(1, 150)
            if number == 1:
                blue_alien_bullet = Blue_alien_bullet(self.rect.x + 24, self.rect.y + 24)
                blue_alien_bullet_list.add(blue_alien_bullet)
                all_sprites_list.add(blue_alien_bullet)

    class Blue_alien_bullet(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            self.image = pygame.image.load("blue_alien_bullet.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set speed vector
            self.change_y = 0

        def update(self):
            self.change_y = 5
            self.rect.y += self.change_y
            if self.rect.y > 618 or self.rect.y < -22:
                self.kill()

    class Red_alien(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            self.image = pygame.image.load("red_alien.png").convert()

            #Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()

            self.center_of_rotation_x = 224-10
            self.center_of_rotation_y = 0
            self.radius = 45
            self.angle = radians(0)  #pi/4 # starting angle 45 degrees
            self.omega = 0.001 * random.randint(100, 175) #Angular velocity
            self.center = 0
            self.change_x = self.radius * self.omega * cos(self.angle + pi / 2) # New x
            self.change_y = self.radius * self.omega * sin(self.angle + pi / 2) # New y

        def update(self):
            self.rect.x = self.center_of_rotation_x + self.radius * cos(self.angle) + self.shift_x #Starting position x
            self.rect.y = self.center_of_rotation_y - self.radius * sin(self.angle) + self.shift_y #Starting position y
            self.center += 1
            self.angle += self.omega # New angle, we add angular velocity
            self.rect.x += self.change_x
            self.rect.y += self.change_y + self.center

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
    enemy_list = pygame.sprite.Group()
    blue_alien_bullet_list = pygame.sprite.Group()
    red_alien_list = pygame.sprite.Group()

    def wave(green_alien_number, green_alien_delay, blue_alien_number, blue_alien_delay, red_alien_number, red_alien_delay):
        for i in range(green_alien_number):
            green_alien = Green_alien()
            green_alien.rect.x = random.randrange(screen_width)
            green_alien.rect.y = -green_alien_delay - random.randint(30, 130)
            green_alien_list.add(green_alien)
            all_sprites_list.add(green_alien)

        for i in range(blue_alien_number):
            blue_alien = Blue_alien()
            blue_alien.rect.x = random.randrange(16, screen_width - 70)
            blue_alien.rect.y = -blue_alien_delay - random.randint(60, 160)
            blue_alien_list.add(blue_alien)
            all_sprites_list.add(blue_alien)

        for i in range(red_alien_number):
            red_alien = Red_alien()
            red_alien.shift_x = random.randrange(-screen_width/2, screen_width/2)
            red_alien.shift_y = -red_alien_delay - random.randint(40, 140)
            red_alien_list.add(red_alien)
            all_sprites_list.add(red_alien)

    wave(1, 0, 0, 0, 0, 0)

    arwing = Arwing(212, 475)
    left_wing = Left_wing(185, 511)
    right_wing = Right_wing(245, 511)
    laser = Laser(-100, -100)
    blue_alien_bullet = Blue_alien_bullet(-100, -100)

    all_sprites_list.add(arwing)
    all_sprites_list.add(left_wing)
    all_sprites_list.add(right_wing)

    laser_sound = pygame.mixer.Sound("laser.ogg")

    # Create an empty array
    star_list = []

    # Loop 175 times and add a star in a random x,y position
    for i in range(175):
        x = random.randrange(0, screen_width)
        y = random.randrange(0, screen_height)
        star_list.append([x, y])

    score = 0

    wave2 = False
    wave3 = False
    wave4 = False
    wave5 = False
    wave6 = False
    wave7 = False
    wave8 = False
    wave9 = False
    wave10 = False
    wave11 = False
    wave12 = False
    wave13 = False
    wave14 = False
    wave15 = False

    green_alien_hit = 0
    blue_alien_hit = 0
    red_alien_hit = 0

    start_time = int(time.time())

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
                    left_wing.changespeed(-3)
                    right_wing.changespeed(-3)
                elif event.key == pygame.K_RIGHT:
                    arwing.changespeed(3)
                    left_wing.changespeed(3)
                    right_wing.changespeed(3)
                elif event.key == pygame.K_SPACE:
                    laser = Laser(arwing.rect.x + 14, arwing.rect.y)
                    laser_list.add(laser)
                    all_sprites_list.add(laser)

            # Reset speed when key goes up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    arwing.changespeed(3)
                    left_wing.changespeed(3)
                    right_wing.changespeed(3)
                elif event.key == pygame.K_RIGHT:
                    arwing.changespeed(-3)
                    left_wing.changespeed(-3)
                    right_wing.changespeed(-3)

        # --- Game logic should go here
        if laser.rect.y >= 455:
            laser_sound.play()

        current_time = int(time.time())
        timer = current_time - start_time

        if timer == 5 and wave2 == False:
            wave(0, 0, 1, 0, 0, 0)
            wave2 = True
        if timer == 10 and wave3 == False:
            wave(1, 0, 1, 200, 0, 0)
            wave3 = True
        if timer == 15 and wave4 == False:
            wave(5, 200, 5, 0, 0, 0)
            wave4 = True
        if timer == 20 and wave5 == False:
            wave(10, 0, 10, 200, 0, 0)
            wave5 = True
        if timer == 25 and wave6 == False:
            wave(20, 0, 0, 0, 0, 0)
            wave6 = True
        if timer == 30 and wave7 == False:
            wave(0, 0, 20, 0, 0, 0)
            wave7 = True
        if timer == 35 and wave8 == False:
            wave(15, 0, 15, 200, 0, 0)
            wave8 = True
        if timer == 40 and wave9 == False:
            wave(0, 0, 0, 0, 1, 0)
            wave9 = True
        if timer == 45 and wave10 == False:
            wave(15, 0, 0, 0, 5, 0)
            wave10 = True
        if timer == 55 and wave11 == False:
            wave(10, 0, 10, 200, 10, 0)
            wave11 = True
        if timer == 65 and wave12 == False:
            wave(20, 0, 0, 0, 25, 50)
            wave12 = True
        if timer == 75 and wave13 == False:
            wave(15, 0, 15, 400, 15, 50)
            wave13 = True
        if timer == 85 and wave14 == False:
            wave(0, 0, 15, 200, 15, 0)
            wave14 = True
        if timer == 95 and wave15 == False:
            wave(15, 0, 20, 400, 20, 50)
            wave15 = True

        # This calls update on all the sprites
        all_sprites_list.update()

        # See if the laser has collided with anything.
        green_alien_hit += len(pygame.sprite.groupcollide(laser_list, green_alien_list, True, True))
        blue_alien_hit += len(pygame.sprite.groupcollide(laser_list, blue_alien_list, True, True))
        red_alien_hit += len(pygame.sprite.groupcollide(laser_list, red_alien_list, True, True))

        blue_alien_bullet_hit_list = pygame.sprite.groupcollide(laser_list, blue_alien_bullet_list, True, True)

        enemy_list.add(blue_alien_list, green_alien_list, red_alien_list, blue_alien_bullet_list)

        arwing_hit = pygame.sprite.spritecollide(arwing, enemy_list, True)
        left_wing_hit = pygame.sprite.spritecollide(left_wing, enemy_list, True)
        right_wing_hit = pygame.sprite.spritecollide(right_wing, enemy_list, True)

        # Check the list of collisions.
        score = green_alien_hit * 50 + blue_alien_hit * 100 + red_alien_hit * 50

        for hit in arwing_hit:
            lose()

        for hit in left_wing_hit:
            lose()

        for hit in right_wing_hit:
            lose()

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