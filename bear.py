import pygame
import sys
from InputHandler import InputHandler
from box import Box
 
windowSize = [800,600]
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
 

        self.screen = pygame.display.set_mode((windowSize[0], windowSize[1]))
        
<<<<<<< HEAD
        # define a variable to control the main loop
        running = True
=======
        # create a surface on screen that has the size of 240 x 180
        self.screen = pygame.display.set_mode((800, 600))
        
>>>>>>> 474b0f3ef28a1a6da7d542a4f0e031e7b556aa3e
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

            self.render(self.activeBox)

<<<<<<< HEAD
    def render(self, box):
        
=======
        pygame.quit()

    def render(self):
>>>>>>> 474b0f3ef28a1a6da7d542a4f0e031e7b556aa3e
        self.screen.blit(pygame.image.load("assets/white.png"), (0,0))
        p = pygame.image.load(box.image)
        p = p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
        self.screen.blit(p, (windowSize[0] / 4, windowSize[1] / 4))
        q = pygame.image.load(box.latchLeft)
        q = pygame.transform.scale(q, (windowSize[0] / 16, windowSize[1] / 5))
        self.screen.blit(q, (windowSize[0] / 3, windowSize[1] / 4))
        r = pygame.image.load(box.latchRight)
        r = pygame.transform.scale(r, (windowSize[0] / 16, windowSize[1] / 5))
        self.screen.blit(r, (windowSize[0] / 1.65, windowSize[1] / 4))
        pygame.display.flip()

<<<<<<< HEAD
=======
        # self.activeBox.render()
>>>>>>> 474b0f3ef28a1a6da7d542a4f0e031e7b556aa3e

    @staticmethod
    def shouldQuit():
        return len(pygame.event.get(pygame.QUIT)) > 0

if __name__=="__main__":
    # call the main function
    main()