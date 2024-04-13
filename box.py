import pygame
from bear import getScreen, getWindowSize

class Box:
    def __init__(self, stage = 1, boxSize = [200,150,600,450], latchSize1 = [270,150,315,270], latchSize2 = [490,150,530,270]):
        self.face = "front"
        self.health = 100
        self.latchLeft = "assets/box_" + str(stage) + "/latch_left.png"
        self.latchRight = "assets/box_" + str(stage) + "/latch_right.png"
        self.image = "assets/box_" + str(stage) + "/box_" + str(stage) + ".png"
        self.hurt = "assets/box_" + str(stage) + "/box_" + str(stage) + "_damage.png"
        self.xRange = [boxSize[0],boxSize[2]]
        self.yRange = [boxSize[1],boxSize[3]]
        self.xLatchLeft = [latchSize1[0],latchSize1[2]]
        self.yLatchLeft = [latchSize1[1],latchSize1[3]]
        self.xLatchRight = [latchSize1[0],latchSize1[2]]
        self.yLatchRight = [latchSize1[1],latchSize1[3]]
        self.taken = False
        p = pygame.image.load(self.image)
        p = pygame.transform.scale(p, (50,50))

        pygame.image.load(self.hurt)

    def setDirection(self, dir = "front"):
        # Sets the side of the box
        self.face = dir

    def rotate(self):
        # Rotates the box
        pass

    def damage(self, location = [0,0]):
        if (self.xRange[0] < location[0] < self.xRange[1] and self.yRange[0] < location[1] < self.yRange[1]):
            self.health -= 1
            self.taken = True
        elif (self.xRange[0] < location[0] < self.xRange[1] and self.yRange[0] < location[1] < self.yRange[1]):
            self.health -= 10
            self.taken = True
        
    def checkHealth(self):
        if self.health <= 0:
            return False
        return True

    def action(self):
        if (self.taken):
            return False
        return True
    
    def bounce(self):
        pass

    def roll(self):
        pass

    def click(self, xPosition, yPosition):
        if (self.xRange[0] < xPosition < self.xRange[1] and self.yRange[0] < yPosition < self.yRange[1]):
            print("Clicked on the box!")

    def render(self):
        screen = getScreen()
        windowSize = getWindowSize()
        p = pygame.image.load(self.image)
        p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
        screen.blit(p, (windowSize[0] / 4, windowSize[1] / 4))
        q = pygame.image.load(self.latchLeft)
        q = pygame.transform.scale(q, (windowSize[0] / 16, windowSize[1] / 5))
        screen.blit(q, (windowSize[0] / 3, windowSize[1] / 4))
        r = pygame.image.load(self.latchRight)
        r = pygame.transform.scale(r, (windowSize[0] / 16, windowSize[1] / 5))
        screen.blit(r, (windowSize[0] / 1.65, windowSize[1] / 4))


