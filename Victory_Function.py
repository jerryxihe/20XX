#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Grant
#
# Created:     10/06/2017
# Copyright:   (c) Grant 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#Import score from Game function
def victory(score, highscore,ship_type):
    from Menu_Function import main_menu
    import pygame

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pygame.init()


    size = (448, 576)
    screen = pygame.display.set_mode(size)


    mouse_click = [0,0]

    #Import images, music, and buttons
    pygame.display.set_caption("20XX")
    pygame.mixer.music.load('Victory.mp3')
    pygame.mixer.music.play(-1)
    background_image = pygame.image.load("victory.png").convert()


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
                break
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = pygame.mouse.get_pos()
        # --- Game logic should go here
        time = (pygame.time.get_ticks()/1000)

        #Returns mouse position
        mouse = pygame.mouse.get_pos()

        screen.fill(BLACK)


        screen.blit(background_image,[0,0])
        font = pygame.font.SysFont('Calibri', 33, True, False)

        #Display score from the game
        your_score = font.render("Score:",True,WHITE)
        score_text = font.render(str(score),True,WHITE)
        screen.blit(your_score, [130, 260])
        screen.blit(score_text, [290, 260])
        screen.blit(play_again,[174,390])
        your_highscore = font.render("Highscore:",True,WHITE)
        highscore_text = font.render(str(highscore),True,WHITE)
        screen.blit(your_highscore, (130, 310))
        screen.blit(highscore_text, [290, 310])

        #Draw buttons, glow when user hovers over them
        if 174<mouse[0]<274 and 390<mouse[1]<440:
            screen.blit(play_again1,[174,390])
        #appends score and shipt type to a txt file (Highscores.txt)
        if 174<mouse_click[0]<274 and 390<mouse_click[1]<440:
            f=open("Highscores.txt","a")
            f.write(ship_type.upper())
            f.write(" - ")
            f.write(str(score))
            f.write("\n")
            f.close()
            main_menu(highscore)
            break
        screen.blit(quitbutton,[174,460])
        if 174<mouse[0]<274 and 460<mouse[1]<510:
            screen.blit(quitbutton1,[174,460])
        #appends score and shipt type to a txt file (Highscores.txt)
        if 174<mouse_click[0]<274 and 460<mouse_click[1]<510:
            f=open("Highscores.txt","a")
            f.write(ship_type.upper())
            f.write(" - ")
            f.write(str(score))
            f.write("\n")
            f.close()
            pygame.quit()
            break
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()