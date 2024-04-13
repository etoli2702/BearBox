import pygame
import sys
from InputHandler import InputHandler
import box
import BoxElement

def getScreen():
    return BearBox.screen

def getWindowSize():
    return BearBox.windowSize

# define a main function
def main():
    game = BearBox()
    game.run()
     
class BearBox:
    windowSize = [800,600]
    screen = pygame.display.set_mode((windowSize[0], windowSize[1]))

    def __init__(self):
        self.inputHandler = InputHandler()
        self.activeBox: box.Box

    def run(self):
        # initialize the pygame module
        pygame.init()
        logo = pygame.image.load("assets/white.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("test")
        # load and set the logo
        
        defaultElements = [BoxElement.BoxElement(1, "latch_left", None, (-110, -87), (55, 110)),
                           BoxElement.BoxElement(1, "latch_right", None, (110, -87), (55, 110))]
        self.activeBox = box.Box(elements=defaultElements)
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
                self.activeBox.click(clickPostion[0], clickPostion[1])

            self.render()

        pygame.quit()

    i = 0
    def render(self):
        BearBox.screen.blit(pygame.image.load("assets/white.png"), (0,0))

        BearBox.i += 5
        self.activeBox.rotate(BearBox.i)
        self.activeBox.render()
        
        pygame.display.flip()

    @staticmethod
    def shouldQuit():
        return len(pygame.event.get(pygame.QUIT)) > 0

if __name__=="__main__":
    # call the main function
    main()