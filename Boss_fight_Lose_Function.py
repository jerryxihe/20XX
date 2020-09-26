#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Grant
#
# Created:     03/06/2017
# Copyright:   (c) Grant 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lose():
    from Game_boss_fight import game
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

    pygame.display.set_caption("20XX")
    pygame.mixer.music.load('Instructions.mp3')
    pygame.mixer.music.play(-1)
    background_image = pygame.image.load("lose.png").convert()


    play_again = pygame.image.load('play_again.png')
    play_again1 = pygame.image.load('play_again1.png')
    quitbutton = pygame.image.load('quit.png')
    quitbutton1 = pygame.image.load('quit1.png')


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
                gameover = True
                break
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
        screen.blit(play_again,[174,360])
        if 174<mouse[0]<274 and 360<mouse[1]<410:
            screen.blit(play_again1,[174,360])
        if 174<mouse_click[0]<274 and 360<mouse_click[1]<410:
            game("ice")
            break
        screen.blit(quitbutton,[174,430])
        if 174<mouse[0]<274 and 430<mouse[1]<480:
            screen.blit(quitbutton1,[174,430])
        if 174<mouse_click[0]<274 and 430<mouse_click[1]<480:
            pygame.quit()
            break
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()