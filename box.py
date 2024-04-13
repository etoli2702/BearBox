import pygame

class Box:
    def __init__(self, stage = 0):
        self.face = "front"
        self.health = 100
        self.image = pygame.image.load("assets/black1.png")
        self.xRange = [0,100]
        self.yRange = [0,100]

    def setDirection(self, dir = "front"):
        # Sets the side of the box
        self.face = dir

    def rotate(self):
        # Rotates the box
        pass

    def damage(self):
        pass

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
    


