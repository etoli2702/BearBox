import pygame
import bear
import BoxElement

ROLL_FRAMES = 60

class Box:
    def __init__(self, stage = 1, boxSize = [200,150,600,450], elements: list[BoxElement.BoxElement] = []):
        self.face = "front"
        self.health = 100
        self.image = "assets/box_" + str(stage) + "/box_" + str(stage) + ".png"
        self.hurt = "assets/box_" + str(stage) + "/box_" + str(stage) + "_damage.png"
        self.xRange = [boxSize[0],boxSize[2]]
        self.yRange = [boxSize[1],boxSize[3]]
        self.rotation = 0
        self.elements = elements
        for element in elements:
            element.setParent(self)
        self.taken = False

        self.rolling = False
        self.rollCounterClockwise = False
        self.rollFrames = 0

    def setDirection(self, dir = "front"):
        # Sets the side of the box
        self.face = dir

    def rotate(self, rotation):
        self.rotation = rotation
        for element in self.elements:
            element.rotate(rotation)

    def damage(self, location = [0,0]):
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        if (xRangeScaled[0] < location[0] < xRangeScaled[1]) and (yRangeScaled[0] < location[1] < yRangeScaled[1]):
            self.health -= 1
            self.taken = True

    def getScaledXRange(self):
        return [item/800*pygame.display.get_window_size()[0] for item in self.xRange]
    
    def getScaledYRange(self):
        return [item/600*pygame.display.get_window_size()[1] for item in self.xRange]
        
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

    def roll(self, counterclockwise: bool):
        self.rolling = True
        self.rollCounterClockwise = counterclockwise

    def click(self, xPosition, yPosition):
        for element in self.elements:
            if(element.click(xPosition, yPosition)):
                print(f"Clicked on {element.spritePath}")
                return
        
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        if (xRangeScaled[0] < xPosition < xRangeScaled[1]) and (yRangeScaled[0] < yPosition < yRangeScaled[1]):
            print("Clicked on the box!")

    def contains(self, xPosition, yPosition):
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        return xRangeScaled[0] < xPosition < xRangeScaled[1] and yRangeScaled[0] < yPosition < yRangeScaled[1]

    def update(self):
        if self.rolling:
            self.rollFrames += 1
            if self.rollFrames < ROLL_FRAMES:
                self.rotate(360/ROLL_FRAMES * self.rollFrames * (1 if self.rollCounterClockwise else -1))
            else:
                self.rollFrames = 0
                self.rolling = False
                self.rotate(0)

    def render(self):
        screen = bear.getScreen()
        windowSize = pygame.display.get_window_size()
        p = pygame.image.load(self.image)
        p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
        p = pygame.transform.rotate(p, self.rotation)

        spriteRect = p.get_rect()

        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        spriteRect.centerx = xRangeScaled[0] + (xRangeScaled[1] - xRangeScaled[0])/2
        spriteRect.centery = yRangeScaled[0] + (yRangeScaled[1] - yRangeScaled[0])/2

        screen.blit(p, spriteRect)

        for element in self.elements:
            element.render()

        


