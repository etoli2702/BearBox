import pygame
import sys
from InputHandler import InputHandler



def getScreen():
    return BearBox.screen

def getWindowSize():
    return BearBox.windowSize
import box
from hud import Healthbar

import box
import BoxElement

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
        self.activeHud = Healthbar

    def run(self):
        # initialize the pygame module
        pygame.init()
        logo = pygame.image.load("assets/white.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("test")
        # load and set the logo
        
        self.activeBox = box.Box()
        self.activeBox.action()
        self.activeHud = Healthbar()



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

        self.activeBox.render()
        self.activeHud.render(10)

        latch = BoxElement.BoxElement(1, "latch_left")
        latch2 = BoxElement.BoxElement(1, "latch_left")
        BearBox.i+=5
        latch.setOrigin(400, 300)
        latch.offset(100, -200)
        latch.rotate(BearBox.i)
        latch.render()
        latch2.setOrigin(400, 300)
        latch2.offset(-100, -200)
        latch2.rotate(BearBox.i)
        latch2.render()
        
        pygame.display.flip()

    @staticmethod
    def shouldQuit():
        return len(pygame.event.get(pygame.QUIT)) > 0

if __name__=="__main__":
    # call the main function
    main()