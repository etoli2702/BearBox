import pygame
import sys
from InputHandler import InputHandler
from box import Box
 
# define a main function
def main():
    game = BearBox()
    game.run()
     
class BearBox:
    def __init__(self):
        self.inputHandler = InputHandler()
        self.activeBox: Box

    def run(self):
        # initialize the pygame module
        pygame.init()
        logo = pygame.image.load("assets/white.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("test")
        # load and set the logo
        
        # create a surface on screen that has the size of 240 x 180
        self.screen = pygame.display.set_mode((800, 600))
        
        self.activeBox = Box()
        self.activeBox.action()

        inputHandler = InputHandler()
        
        # main loop
        while not BearBox.shouldQuit():
            inputHandler.update()
            if inputHandler.hasMadeCircle():
                print("CIRCLE COMPLETE!")
                inputHandler.restartDrag()

            if inputHandler.hasDoneBounce():
                print("BOUNCE COMPLETE!")
                inputHandler.restartDrag()

            clickPostion = inputHandler.consumeClick()
            if not (clickPostion is None):
                print(f"Player clicked at {clickPostion}")

            self.render()

        pygame.quit()

    def render(self):
        self.screen.blit(pygame.image.load("assets/white.png"), (0,0))
        pygame.display.flip()

        # self.activeBox.render()

    @staticmethod
    def shouldQuit():
        return len(pygame.event.get(pygame.QUIT)) > 0

if __name__=="__main__":
    # call the main function
    main()