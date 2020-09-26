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

#gets the ship_type and highscore parameter from the ship select module
def game(ship_type, highscore):
    import pygame
    import random
    import time
    from Lose_Function import lose
    from Victory_Function import victory
    from math import sin, cos, pi, radians

    # Define some colors
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    #boolean to check if the game is on the boss wave
    bosswave = False

    #arwing body sprite
    class Arwing(pygame.sprite.Sprite):
        """ This class is a player-controlled sprite. """

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #selects and loads arwing body type using the ship_type parameter
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
            # Set arwing body velocity vector
            self.change_x = 0

        def changespeed(self, x):
            """ Change the speed of the arwing body"""
            self.change_x += x

        def update(self):
            """ Find a new position for the arwing body"""
            self.rect.x += self.change_x

            #stops the arwing body from moving off-screen
            if self.rect.x < 27:
                self.rect.x = 27
            if self.rect.x > 388:
                self.rect.x = 388

    #arwing left wing sprite
    #the arwing sprite was split to create more reasonable hitboxes
    class Left_wing(pygame.sprite.Sprite):
        """ This class is a player-controlled sprite. """

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #selects and loads arwing left wing type using the ship_type parameter
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
            # Set arwing left wing velocity vector
            self.change_x = 0

        def changespeed(self, x):
            """ Change the speed of the arwing left wing"""
            self.change_x += x

        def update(self):
            """ Find a new position for the arwing left wing"""
            self.rect.x += self.change_x

            #stops the arwing left wing from moving off-screen
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 361:
                self.rect.x = 361

    #arwing right wing sprite
    class Right_wing(pygame.sprite.Sprite):
        """ The class is the player-controlled sprite. """

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #selects and loads arwing right wing type using the ship_type parameter
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
            # Set arwing right wing velocity vector
            self.change_x = 0

        def changespeed(self, x):
            """ Change the speed of the arwing right wing"""
            self.change_x += x

        def update(self):
            """ Find a new position for the arwing right wing"""
            self.rect.x += self.change_x

            #stops the arwing right wing from moving off-screen
            if self.rect.x < 60:
                self.rect.x = 60
            if self.rect.x > 421:
                self.rect.x = 421

    #laser sprite
    class Laser(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #selects and loads laser type using the ship_type parameter
            if ship_type == "classic":
                self.image = pygame.image.load("laser.png").convert()
            elif ship_type == "space":
                self.image = pygame.image.load("purple_laser.png").convert()
            elif ship_type == "steel":
                self.image = pygame.image.load("laser.png").convert()
            elif ship_type == "kappapride":
                self.image = pygame.image.load("kappapride_laser.png").convert()
            elif ship_type == "ice":
                self.image = pygame.image.load("blue_laser.png").convert()
            elif ship_type == "victorious":
                self.image = pygame.image.load("blue_laser.png").convert()
            elif ship_type == "cool":
                self.image = pygame.image.load("green_laser.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set laser velocity vector
            self.change_y = -20

        def update(self):
            """ Find a new position for the laser"""
            self.rect.y += self.change_y

            #kills the laser if it moves off-screen
            if self.rect.y < -42:
                self.kill()

    #green alien sprite
    class Green_alien(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads green alien sprite
            self.image = pygame.image.load("green_alien.png").convert()

            #Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

            # -- Attributes
            # Set green alien velocity vectors
            self.change_x = 3
            self.change_y = 2

        def update(self):
            """ Find a new position for the green alien"""
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            #reverses the green alien's horizontal velocity if it hits the edge of the screen
            if self.rect.x <= 0:
                self.change_x = 3
            if self.rect.x >= 398:
                self.change_x = -3

            #kills the green alien if it moves off-screen
            if self.rect.y > 576:
                self.kill()

    #blue alien sprite
    class Blue_alien(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads blue alien sprite
            self.image = pygame.image.load("blue_alien.png").convert()

            #Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

            # -- Attributes
            # Set blue alien velocity vector
            self.change_y = 2

        def update(self):
            """ Find a new position for the blue alien"""
            self.rect.y += self.change_y

            #kills the blue alien if it moves off-screen
            if self.rect.y > 576:
                self.kill()

            #randomly fires a bullet using the Blue_alien_bullet class
            number = random.randint(1, 150)
            if number == 1:
                blue_alien_bullet = Blue_alien_bullet(self.rect.x + 24, self.rect.y + 24)
                blue_alien_bullet_list.add(blue_alien_bullet)
                all_sprites_list.add(blue_alien_bullet)

    #blue alien bullet sprite
    class Blue_alien_bullet(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the blue alien bullet sprite
            self.image = pygame.image.load("blue_alien_bullet.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set blue alien bullet velocity vector
            self.change_y = 5

        def update(self):
            """ Find a new position for the blue alien bullet"""
            self.rect.y += self.change_y

            #kills the blue alien bullet if it moves off-screen
            if self.rect.y > 576 or self.rect.y < -22:
                self.kill()

    #red alien sprite
    class Red_alien(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the red alien sprite
            self.image = pygame.image.load("red_alien.png").convert()

            #Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()

            #red alien movement attributes
            self.center_of_rotation_x = 224-10
            self.center_of_rotation_y = 0
            self.radius = 45
            self.angle = radians(0)  #pi/4 # starting angle 45 degrees
            self.omega = 0.001 * random.randint(100, 175) #Angular velocity
            self.center = 0
            self.change_x = self.radius * self.omega * cos(self.angle + pi / 2) # New x
            self.change_y = self.radius * self.omega * sin(self.angle + pi / 2) # New y

        def update(self):
            #red alien movement
            self.rect.x = self.center_of_rotation_x + self.radius * cos(self.angle) + self.shift_x #Starting position x
            self.rect.y = self.center_of_rotation_y - self.radius * sin(self.angle) + self.shift_y #Starting position y
            self.center += 2
            self.angle += self.omega # New angle, we add angular velocity
            self.rect.x += self.change_x
            self.rect.y += self.change_y + self.center

            #kills the red alien if it moves off-screen
            if self.rect.y > 576:
                self.kill()

    #boss sprite
    class Boss(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the boss sprite
            self.image = pygame.image.load("boss_no_eye.png").convert()

            #loads the boss bullet sound
            self.boss_shot_sound = pygame.mixer.Sound("shot.ogg")

            #Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set boss velocity vectors
            self.change_x = 4
            self.change_y = 0

        #boss laser method
        def laser(self):
            #checks to see if the game is on the boss wave
            if bosswave == True:

                #calls the Boss_laser sprite
                boss_laser = Boss_laser(self.rect.x + 55, self.rect.y + 48)
                boss_laser_list.add(boss_laser)
                all_sprites_list.add(boss_laser)

        def update(self):
            #checks to see if the game is on the boss wave
            if bosswave == True:

                """ Find a new position for the boss"""
                self.rect.x += self.change_x
                self.rect.y += self.change_y

                #reverses the boss's horizontal velocity if it hits the edge of the screen
                if self.rect.x <= 0:
                    self.change_x = 4
                if self.rect.x >= 327:
                    self.change_x = -4

                #randomly fires a bullet using the Boss_bullet class
                number = random.randrange(1, 50)
                if number == 1:
                    boss_bullet = Boss_bullet(self.rect.x + 3, self.rect.y + 87)
                    boss_bullet_list.add(boss_bullet)
                    all_sprites_list.add(boss_bullet)

                    #plays the boss bullet sound
                    self.boss_shot_sound.play()

                #randomly fires a bullet using the Boss_bullet class
                number = random.randrange(1, 50)
                if number == 1:
                    boss_bullet = Boss_bullet(self.rect.x + 103, self.rect.y + 87)
                    boss_bullet_list.add(boss_bullet)
                    all_sprites_list.add(boss_bullet)

                    #plays the boss bullet sound
                    self.boss_shot_sound.play()

    #boss bullet sprite
    class Boss_bullet(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the boss bullet sprite
            self.image = pygame.image.load("boss_bullet.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set boss bullet velocity vector
            self.change_y = 5

        def update(self):
            """ Find a new position for the boss bullet"""
            self.rect.y += self.change_y

            #kills the boss bullet if it moves off-screen
            if self.rect.y > 591 or self.rect.y < -15:
                self.kill()

    #boss laser sprite
    class Boss_laser(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the boss laser sprite
            self.image = pygame.image.load("boss_laser.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    #boss laser warning sprite
    class Boss_laser_warning(pygame.sprite.Sprite):

        # -- Methods
        def __init__(self, x_change, y_change, x, y):
            """Constructor function"""
            # Call the parent's constructor
            super().__init__()

            #loads the boss laser warning sprite
            self.image = pygame.image.load("boss_laser_warning.png").convert()

            # Make our top-left corner the passed-in location.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            # -- Attributes
            # Set boss laser warning velocity vector
            self.change_x = x_change
            self.change_y = y_change

        def update(self):
            """ Find a new position for the boss laser warning"""
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            #reverses the boss laser warning's horizontal velocity if it hits the edge of the screen
            if self.rect.x <= 59:
                self.change_x = 4
            if self.rect.x >= 386:
                self.change_x = -4

    #initializes pygame
    pygame.init()

    # Set the height and width of the screen
    screen_width = 448
    screen_height = 576
    screen = pygame.display.set_mode([screen_width, screen_height])

    #game window caption
    pygame.display.set_caption("20XX")

    #background music
    pygame.mixer.music.load('Game.mp3')
    pygame.mixer.music.play(1)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #sprite lists to check for collisions and draw on-screen
    all_sprites_list = pygame.sprite.Group()
    green_alien_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()
    blue_alien_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    blue_alien_bullet_list = pygame.sprite.Group()
    red_alien_list = pygame.sprite.Group()
    boss_bullet_list = pygame.sprite.Group()
    boss_laser_list = pygame.sprite.Group()
    boss_laser_warning_list = pygame.sprite.Group()

    #wave function to specify types of aliens, number of aliens, and delays on each wave
    def wave(green_alien_number, green_alien_delay, blue_alien_number, blue_alien_delay, red_alien_number, red_alien_delay):

        #green aliens in a wave
        for i in range(green_alien_number):
            green_alien = Green_alien()
            green_alien.rect.x = random.randrange(screen_width)
            green_alien.rect.y = -green_alien_delay - random.randint(30, 130)
            green_alien_list.add(green_alien)
            all_sprites_list.add(green_alien)

        #blue aliens in a wave
        for i in range(blue_alien_number):
            blue_alien = Blue_alien()
            blue_alien.rect.x = random.randrange(16, screen_width - 70)
            blue_alien.rect.y = -blue_alien_delay - random.randint(60, 160)
            blue_alien_list.add(blue_alien)
            all_sprites_list.add(blue_alien)

        #red aliens in a wave
        for i in range(red_alien_number):
            red_alien = Red_alien()
            red_alien.shift_x = random.randrange(-screen_width/2, screen_width/2)
            red_alien.shift_y = -red_alien_delay - random.randint(40, 140)
            red_alien_list.add(red_alien)
            all_sprites_list.add(red_alien)

    #draws sprites that are referenced before the draw command
    arwing = Arwing(212, 475)
    left_wing = Left_wing(185, 511)
    right_wing = Right_wing(245, 511)
    laser = Laser(-100, -100)
    blue_alien_bullet = Blue_alien_bullet(-100, -100)
    boss_bullet = Boss_bullet(-100, -100)
    boss_laser = Boss_laser(-100, -100)
    boss_laser_warning = Boss_laser_warning(0, 0, -100, -100)
    boss = Boss(-500, -100)

    #adds sprites to the all_sprites_list for drawing
    all_sprites_list.add(arwing)
    all_sprites_list.add(left_wing)
    all_sprites_list.add(right_wing)
    all_sprites_list.add(boss)

    #loads game sounds
    laser_sound = pygame.mixer.Sound("laser.ogg")
    boss_laser_sound = pygame.mixer.Sound("boss_laser.ogg")
    boss_defeat_sound = pygame.mixer.Sound("boss_defeat.oga")
    green_death_sound = pygame.mixer.Sound("green_death.oga")
    blue_death_sound = pygame.mixer.Sound("blue_death.oga")
    red_death_sound = pygame.mixer.Sound("red_death.oga")

    # Create an empty array for the stars
    star_list = []

    # Loop 175 times and add a star in a random x,y position
    for i in range(175):
        x = random.randrange(0, screen_width)
        y = random.randrange(0, screen_height)
        star_list.append([x, y])

    #sets score = 0
    score = 0

    #sets wave booleans to False
    wave1 = False
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

    #sets boss hit list to 0
    boss_hit = 0

    #sets starting time for the wave timer
    start_time = int(time.time())

    #sets the boss laser and boss laser warning booleans to False
    boss_laser_fired = False
    boss_laser_warning_appear = False

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

            # Set the arwing velocity based on the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    arwing.changespeed(-3)
                    left_wing.changespeed(-3)
                    right_wing.changespeed(-3)
                elif event.key == pygame.K_RIGHT:
                    arwing.changespeed(3)
                    left_wing.changespeed(3)
                    right_wing.changespeed(3)

                #fires lasers when space bar pressed
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

        #plays laser sound
        if laser.rect.y >= 455:
            laser_sound.play()

        #sets current time for the wave timer
        current_time = int(time.time())

        #wave timer
        timer = current_time - start_time

        #calls waves and sets the wave booleans to True once the wave appears
        #the wave booleans ensures only one of each wave is sent
        if timer == 0 and wave1 == False:
            wave(1, 0, 0, 0, 0, 0)
            wave1 = True
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
            wave(12, 0, 0, 0, 0, 0)
            wave6 = True
        if timer == 30 and wave7 == False:
            wave(0, 0, 12, 0, 0, 0)
            wave7 = True
        if timer == 35 and wave8 == False:
            wave(12, 0, 12, 200, 0, 0)
            wave8 = True
        if timer == 40 and wave9 == False:
            wave(0, 0, 0, 0, 1, 0)
            wave9 = True
        if timer == 45 and wave10 == False:
            wave(12, 0, 0, 0, 5, 0)
            wave10 = True
        if timer == 55 and wave11 == False:
            wave(10, 0, 10, 200, 10, 0)
            wave11 = True
        if timer == 65 and wave12 == False:
            wave(12, 0, 0, 0, 15, 50)
            wave12 = True
        if timer == 75 and wave13 == False:
            wave(12, 0, 12, 400, 12, 50)
            wave13 = True
        if timer == 85 and wave14 == False:
            wave(0, 0, 15, 200, 15, 0)
            wave14 = True
        if timer == 95 and wave15 == False:
            wave(12, 0, 15, 400, 15, 50)
            wave15 = True
        if timer == 105:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Boss.mp3')
            pygame.mixer.music.play(-1)
        if timer == 109 and bosswave == False:
            boss.rect.x = 163
            boss.rect.y = 10
            bosswave = True

        #calls the boss laser warning and fires the boss laser every five seconds on the boss wave
        if timer % 5 == 0 and timer > 109 and boss_laser_warning_appear == False:

            #opens the boss's eye one second before he fires the laser
            boss.image = pygame.image.load("boss.png").convert()
            boss_laser_warning = Boss_laser_warning(boss.change_x, boss.change_y, boss.rect.x + 59, boss.rect.y + 48)
            boss_laser_warning_list.add(boss_laser_warning)
            all_sprites_list.add(boss_laser_warning)
            boss_laser_warning_appear = True

            #plays the boss laser sound, including a one second charge
            boss_laser_sound.play()

        if timer % 5 == 1 and timer > 109 and boss_laser_fired == False:
            boss.laser()
            boss_laser_fired = True
            boss.image = pygame.image.load("boss_no_eye.png").convert()
            boss_laser_warning_appear = False

        if timer % 5 == 2:
            all_sprites_list.remove(boss_laser_list)
            boss_laser_list.remove(boss_laser_list)
            boss_laser_fired = False

        # This calls update on all the sprites
        all_sprites_list.update()

        # See if the laser has collided with an enemy.
        #the groupcollide command fixed the piercing laser bug
        green_alien_hit = pygame.sprite.groupcollide(laser_list, green_alien_list, True, True)
        blue_alien_hit = pygame.sprite.groupcollide(laser_list, blue_alien_list, True, True)
        red_alien_hit = pygame.sprite.groupcollide(laser_list, red_alien_list, True, True)
        boss_hit += len(pygame.sprite.spritecollide(boss, laser_list, True))

        #checks if the laser has collided with destructible enemy projectiles
        blue_alien_bullet_hit_list = pygame.sprite.groupcollide(laser_list, blue_alien_bullet_list, True, True)
        boss_bullet_hit_list = pygame.sprite.groupcollide(laser_list, boss_bullet_list, True, True)

        #creates an enemies list
        enemy_list.add(blue_alien_list, green_alien_list, red_alien_list, blue_alien_bullet_list, boss, boss_bullet_list)

        #checks if any enemies have collided with the arwing
        arwing_hit = pygame.sprite.spritecollide(arwing, enemy_list, True)
        left_wing_hit = pygame.sprite.spritecollide(left_wing, enemy_list, True)
        right_wing_hit = pygame.sprite.spritecollide(right_wing, enemy_list, True)

        #checks if the boss laser has hit the arwing
        arwing_boss_laser_hit = pygame.sprite.spritecollide(arwing, boss_laser_list, False)
        left_wing_boss_laser_hit = pygame.sprite.spritecollide(left_wing, boss_laser_list, False)
        right_wing_boss_laser_hit = pygame.sprite.spritecollide(right_wing, boss_laser_list, False)

        #erases the boss laser warning when the boss laser appears
        boss_laser_warning_erase = pygame.sprite.groupcollide(boss_laser_warning_list, boss_laser_list, True, False)

        # Checks the collision lists, adds to the score, and plays alien death sounds
        #killing a green alien adds 50 points to the score
        for green_alien in green_alien_hit:
            score += 50
            green_death_sound.play()

        #killing a blue alien adds 100 points to the score
        for blue_alien in blue_alien_hit:
            score += 100
            blue_death_sound.play()

        #killing a red alien adds 50 points to the score
        for red_alien in red_alien_hit:
            score += 50
            red_death_sound.play()

        #moves the boss down if it's been hit 10 times
        if boss_hit >= 10:
            boss.change_y = 1
            if boss.rect.y > 100:
                boss.change_y = 0

        #kills the boss if it's been hit 50 times
        if boss_hit == 50:

            #killing the boss adds 5000 points to the score
            score += 5000

            pygame.mixer.music.stop()

            #plays the boss's defeat cry
            boss_defeat_sound.play()
            time.sleep(3)

            #calls the victory screen function
            victory(score,highscore,ship_type)

            break

        #sets the gameover and bosslaser_hit booleans to False
        gameover = False
        bosslaser_hit = False

        #sets the gameover boolean to True if the arwing has been hit
        if gameover == False:
            for hit in arwing_hit:
                gameover = True
                break

        if gameover == False:
            for hit in left_wing_hit:
                gameover = True
                break

        if gameover == False:
            for hit in right_wing_hit:
                gameover = True
                break

        if gameover == False:
            for hit in arwing_boss_laser_hit:
                gameover = True
                bosslaser_hit = True

        if gameover == False:
            for hit in left_wing_boss_laser_hit:
                gameover = True
                bosslaser_hit = True

        if gameover == False:
            for hit in right_wing_boss_laser_hit:
                gameover = True
                bosslaser_hit = True

        #calls the lose screen function
        if gameover == True:
            if bosswave == False:
                time.sleep(1)
                lose(score, highscore, ship_type)

                break
            elif bosswave == True and bosslaser_hit == False:
                time.sleep(1)
                lose(score, highscore, ship_type)

                break
            else:
                """since the boss laser wouldn't appear if it killed the player
                normally, we added a boolean to check if the boss laser killed
                the player. If this boolean returns True, this code draws all
                sprites, including the laser, so the player can see that the
                laser dealt the finishing blow"""
                all_sprites_list.draw(screen)
                pygame.display.flip()
                time.sleep(1)
                lose(score, highscore, ship_type)

                break

        #runs if gameover = False
        else:
            # --- Screen-clearing code goes here

            # Here, we clear the screen to black. Don't put other drawing commands
            # above this, or they will be erased with this command.
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

            #sets the score font
            font = pygame.font.SysFont('Calibri', 25, True, False)

            #blits the score on-screen
            text = font.render(str(score), True, WHITE)

            #shifts the score over when it increases digits, so it doesn't go off the screen
            if score < 100:
                screen.blit(text, [410, 3])
            if score >= 100 and score < 999:
                screen.blit(text, [400, 3])
            if score >= 1000 and score < 9999:
                screen.blit(text, [390, 3])
            if score >= 10000:
                screen.blit(text, [380, 3])

            #draws all sprites to the screen
            all_sprites_list.draw(screen)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

    # Close the window and quit.
    pygame.quit()