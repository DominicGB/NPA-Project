#--------------------------------------------------------------
#Title: Game.py
#Purpose: Main game script for NPA Game
# Author: Dominic Benell
# Date: 07/03/2022
#--------------------------------------------------------------

#--------------------------------------------------------------
import pygame
#--------------------------------------------------------------

# Initialisation and setup
# Initilise python so we can use it

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Set up player image
playerImg = pygame.image.load('assets/graphics/bear.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250
#--------------------------------------------------------------


# Set up some varaibles to use later in our game
running = True
#--------------------------------------------------------------


#--------------------------------------------------------------
# Game Loop
#--------------------------------------------------------------
# Run over abnd over until user aks to quit
while running:

    #--------------------------------------------------------------
    # Input
    # Did user click the window close button?
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerRect.centerx -= 10
            if event.key ==pygame.K_RIGHT:
                playerRect.centerx += 10
            if event.key ==pygame.K_UP:
                playerRect.centery -=20
            if event.key ==pygame.K_DOWN:
                playerRect.centery +=10
            
    #--------------------------------------------------------------


    #--------------------------------------------------------------
    # Update
    #--------------------------------------------------------------
    

    #--------------------------------------------------------------
    # Draw
    #--------------------------------------------------------------
    # Fill the background with a colour
    #--------------------------------------------------------------
    screen.fill((255, 255, 255))

    # Draw everything
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    screen.blit(playerImg, playerRect)

    #Flip the display
    pygame.display.flip()



# END of Game Loop
