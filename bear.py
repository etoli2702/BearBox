import pygame
import sys
from InputHandler import InputHandler
from box import Box
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("assets/white.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("test")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800, 600))
     
    # define a variable to control the main loop
    running = True
    b = Box()
    b.action()

    inputHandler = InputHandler()
     
    # main loop
    while running:
        screen.blit(logo, (0,0))
        # event handling, gets all event from the event queue
        pygame.display.flip()

        inputHandler.update()
        #print("IsCircling", inputHandler.isCircling)
        #print("CCW", inputHandler.isCounterClockwiseCircle)
        if inputHandler.hasMadeCircle():
            print("CIRCLE COMPLETE!")
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()