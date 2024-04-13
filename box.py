import pygame
import bear
import BoxElement


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
        p = pygame.image.load(self.image)
        p = pygame.transform.scale(p, (50,50))

        pygame.image.load(self.hurt)

    def setDirection(self, dir = "front"):
        # Sets the side of the box
        self.face = dir

    def rotate(self, rotation):
        self.rotation = rotation
        for element in self.elements:
            element.rotate(rotation)

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
        for element in self.elements:
            if(element.click(xPosition, yPosition)):
                print(f"Clicked on {element.spritePath}")
        if (self.xRange[0] < xPosition < self.xRange[1] and self.yRange[0] < yPosition < self.yRange[1]):
            print("Clicked on the box!")

    def render(self):
        screen = bear.getScreen()
        windowSize = bear.getWindowSize()
        p = pygame.image.load(self.image)
        p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
        p = pygame.transform.rotate(p, self.rotation)

        spriteRect = p.get_rect()

        spriteRect.centerx = self.xRange[0] + (self.xRange[1] - self.xRange[0])/2
        spriteRect.centery = self.yRange[0] + (self.yRange[1] - self.yRange[0])/2

        screen.blit(p, spriteRect)

        for element in self.elements:
            element.render()

        


