import pygame

class Box:
    def __init__(self, stage = 1, boxSize = [100,100], latchSize = [100,100]):
        self.face = "front"
        self.health = 100
        self.latch = "assets/box_" + stage + "/latch_right.png"
        self.image = "assets/box_" + stage + "/box_" + stage + ".png"
        self.hurt = "assets/box_" + stage + "/box_" + stage + "damage.png"
        self.xRange = [0,boxSize[0]]
        self.yRange = [0,boxSize[1]]
        self.xLatch = [0,latchSize[0]]
        self.yLatch = [0,latchSize[1]]
        self.taken = False
        pygame.image.load(self.image)
        pygame.image.load(self.latch)
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


    


