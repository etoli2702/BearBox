import pygame
from InputHandler import InputHandler
import warnings
import box
import BoxElement
stage = 2

# Suppress libpng warning
warnings.filterwarnings("ignore", category=UserWarning, message="iCCP")


def getScreen():
    return BearBox.screen

import box
from hud import Healthbar 
from hud import Timers 

import box
import BoxElement
from start import Title

# define a main function
def main():
    game = BearBox()
    game.run()
     
class BearBox:
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    def __init__(self):
        self.inputHandler = InputHandler()
        self.activeBox: box.Box
        self.activeHud = Healthbar
        self.start = Title
        self.timer = Timers

    def run(self):
        # initialize the pygame module
        pygame.init()
        logo = pygame.image.load("assets/background.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("test")
        pygame.time.Clock().tick(60)
        # load and set the logo
        i = 0
        gamerun = False

            
        while not BearBox.shouldQuit():   
            # Title Screen 
            self.start = Title()
            self.start.render()

            while not(self.start.confirm):
                if (BearBox.shouldQuit()):
                    pygame.quit() 
                if pygame.event.get(pygame.VIDEORESIZE):
                    newSize = pygame.display.get_surface().get_size()
                    if newSize:
                        pygame.display.set_mode(newSize, pygame.RESIZABLE)
                        self.start.update_location(newSize)
                self.start.checkPress()
                self.start.render()
                pygame.display.flip()
            
            boxNo = 0
            if self.start.choice == 0:
                boxNo = 1
            elif self.start.choice == 1:
                boxNo = 2
            else:
                pygame.quit()
                             

                    

                
            
            defaultElements = [BoxElement.BoxElement(stage, "latch_left", None, (-110, -87), (55, 110)),
                            BoxElement.BoxElement(stage, "latch_right", None, (110, -87), (55, 110))]
            self.activeBox = box.Box(stage=stage, elements=defaultElements)
            self.activeBox.action()
            self.activeHud = Healthbar()
            self.timer = Timers()


            inputHandler = InputHandler()        
            # main loop

            while not gamerun:
                if (BearBox.shouldQuit()):
                        pygame.quit()
                inputHandler.update()
                if inputHandler.hasMadeCircle():
                    print("CIRCLE COMPLETE!")
                    if self.activeBox.contains(inputHandler.dragStartPos[0], inputHandler.dragStartPos[1]):
                        print("Roll")
                        self.activeBox.roll(inputHandler.isCounterClockwiseCircle)
                    inputHandler.restartDrag()

                if inputHandler.hasDoneBounce():
                    print("BOUNCE COMPLETE!")
                    inputHandler.restartDrag()

                clickPostion = inputHandler.consumeClick()
                if not (clickPostion is None):
                    print(f"Player clicked at {clickPostion}")
                    self.activeBox.click(clickPostion[0], clickPostion[1])


                #Global health calculation
                i = self.activeBox.health
                for element in defaultElements:
                    i += element.health
                global_health = i
                if global_health == 0:
                    gamerun = False

                self.activeBox.update()
                self.render(global_health)


            # Win screen
            self.wins()


        pygame.quit()
    
    def title(self):
        while not(self.start.confirm) and not BearBox.shouldQuit():
            if pygame.event.get(pygame.VIDEORESIZE):
                newSize = pygame.display.get_surface().get_size()
                if newSize:
                    pygame.display.set_mode(newSize, pygame.RESIZABLE)
                    self.start.update_location(newSize)
                    self.start.checkPress()
                    self.start.render()
                    pygame.display.flip()
                    if (BearBox.shouldQuit()):
                        pygame.quit()

    def render(self, global_health):
        background = pygame.image.load("assets/background.png")
        background = pygame.transform.scale(background, pygame.display.get_window_size())

        BearBox.screen.blit(background, (0,0))

        self.activeBox.render()
        self.timer.render()
        self.activeHud.render(global_health)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    def wins(self):
        # Render win screen
        win = True
        while win:
            if (BearBox.shouldQuit()):
                pygame.quit()
                win = self.wins()

            screen = getScreen()
            windowSize = pygame.display.get_window_size()

            screen.fill((255, 255, 255))


            p = pygame.image.load("assets/win.png")
                
            p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
            screen.blit(p, (windowSize[0] / 4, windowSize[1] / 4))
            pygame.display.flip()

            mouse_state = pygame.mouse.get_pressed()
            if mouse_state[0]:
                win = False
            else:
                win = True



    @staticmethod
    def shouldQuit():
        return len(pygame.event.get(pygame.QUIT)) > 0

if __name__=="__main__":
    # call the main function
    main()