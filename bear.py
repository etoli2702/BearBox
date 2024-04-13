import pygame
import sys
 
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
    x = False
     
    # main loop
    while running:
        screen.blit(logo, (0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                x = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get the position of the mouse click
                x = False
            elif event.type == pygame.MOUSEMOTION and x:
                # Check for drag
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
        pygame.display.flip()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()