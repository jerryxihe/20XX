#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      0401824
#
# Created:     18/05/2017
# Copyright:   (c) 0401824 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def intro(ship_type, highscore):
    import pygame
    from Game_v14 import game


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (12, 28, 153)
    YELLOW = (176, 239, 67)
    pygame.init()


    size = (448, 576)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("20XX")


    #Importing sprites, sounds, background, and setting up some variables for creating the speech boxes
    duck = pygame.image.load('duckright.png')
    window = pygame.image.load("window.png")
    scroll =True
    image_x=0
    blink = 0
    quack = 0
    dialogue = 0
    quack_sound = pygame.mixer.Sound("quack.ogg")
    pygame.mixer.music.load('Intro.mp3')
    pygame.mixer.music.play(-1)
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
        # --- Game logic should go here
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if dialogue <=3:
                        dialogue +=1
                        quack_sound.play()

        #This is for asthetic effect. When Capt Quack is speaking, you can see the interior of your ship
        if scroll == True:
            image_x -=1
        if image_x ==-500:
            scroll=False
        if scroll==False:
            image_x +=1
        if image_x==0:
            scroll=True




        screen.fill(BLACK)

        # --- Drawing code should go here


        #Drawing the speech boxes
        screen.blit(window,[image_x,30])
        if dialogue <4:
            pygame.draw.rect(screen,BLUE,[120,20,310,100],0)
            pygame.draw.rect(screen,WHITE,[120,20,310,100],4)
            pygame.draw.rect(screen,BLUE,[20,20,100,100],0)
            pygame.draw.rect(screen,WHITE,[20,20,100,100],4)

        #This is to animate Capt Quack. He will alternate between open and closed mouth sprite.
        if quack <=15:
            quack +=1
            duck = pygame.image.load('duckright.png')

        #Scale the image down. The duck is too big
            duck = pygame.transform.scale(duck, (80, 80))
        if quack >15:
            quack +=1
            duck = pygame.image.load('ducktalk.png')
            duck = pygame.transform.scale(duck, (80, 80))
        if quack ==25:
            quack =0
        if dialogue <4:
            #If dialogue <4, then the user is still reading. Once the user has pressed enter 4 times, the images will hide and the game will start
            screen.blit(duck,[30,20])
            pygame.draw.rect(screen,BLUE,[20,90,100,30],0)
            pygame.draw.rect(screen,WHITE,[20,90,100,30],4)
            font = pygame.font.SysFont('Calibri', 15, True, False)
            name = font.render("Capt. Quack",True,YELLOW)
            screen.blit(name, [27, 97])
        #Create flashing text
        font = pygame.font.SysFont('Calibri', 15, True, False)
        if blink <=30:
            blink +=1
            #Dialogue, introduces story of the game
            text1 = font.render(("Welcome Pilot 479. My name is Captain Quack."),True,YELLOW)
            text2 = font.render(("I have assigned you a difficult task."),True,YELLOW)
            text3 = font.render(("The future of our nation depends on you."),True,YELLOW)
            text4 = font.render(("Don't die. Good luck."),True,YELLOW)
        if blink >30:
            blink +=1
            text1 = font.render((""),True,YELLOW)
            text2 = font.render((""),True,YELLOW)
            text3 = font.render((""),True,YELLOW)
        if blink ==40:
            blink =0
        if dialogue <4:
            press_enter = font.render(("Press enter to continue."),True,YELLOW)
            screen.blit(press_enter, [275, 95])
        if dialogue == 0:
            screen.blit(text1, [130, 30])
        if dialogue == 1:
            screen.blit(text2, [130, 30])
        if dialogue == 2:
            screen.blit(text3, [130, 30])
        if dialogue == 3:
            screen.blit(text4, [130, 30])
        if dialogue == 4:
            #Start game once dialogue is finished
            screen.fill(BLACK)
            game(ship_type, highscore)
            break
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()