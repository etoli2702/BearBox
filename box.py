import pygame

class Box:
    def __init__(self, stage = 0, size = [100,100]):
        self.face = "front"
        self.health = 100
        self.image = pygame.image.load("assets/black1.png")
        self.xRange = [0,size[0]]
        self.yRange = [0,size[1]]
        self.locks = False

    def setDirection(self, dir = "front"):
        # Sets the side of the box
        self.face = dir

    def rotate(self):
        # Rotates the box
        pass

    def damage(self, location = [0,0]):
        if (self.xRange[0] < location[0] < self.xRange[1] and self.yRange[0] < location[1] < self.yRange[1]):
            if not(self.locks):
                self.health -= 10

    def checkHealth(self):
        if self.health <= 0:
            return False
        return True

    def action(self):
        if (self.face == "front"):
            self.image = pygame.image.load("assets/black1.png")
        elif (self.face == "back"):
            self.image = ""
        elif (self.face == "left"):
            self.image = pygame.image.load("assets/black2.png")
        elif (self.face == "right"):
            self.image = pygame.image.load("assets/black2.png")
        elif (self.face == "top"):
            self.image = ""
        else:
            self.image = ""
        
        return self.checkHealth()
    


