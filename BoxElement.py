import pygame
from bear import getScreen, getWindowSize
from math import sin, cos, radians

class BoxElement:
    def __init__(self, boxNumber: int, elementName: str):
        self.spritePath = "assets/box_" + str(boxNumber) + "/" + elementName + ".png"
        self.originX = 0
        self.originY = 0
        self.offsetX = 0
        self.offsetY = 0
        self.rotation = 0

    def update(self):
        pass

    def setOrigin(self, positionX, positionY):
        self.originX = positionX
        self.originY = positionY

    def rotate(self, rotation):
        self.rotation = rotation

    def offset(self, offsetX, offsetY):
        self.offsetX = offsetX
        self.offsetY = offsetY
        
#    def setPositionRadial(self, originX, originY, rotation, distance, offset):
#        self.setPosition(originX + distance * cos(radians(rotation) + offset * sin(radians(rotation))), originY - distance * sin(radians(rotation)) - offset * cos(radians(rotation)), rotation)

    def render(self):
        screen = getScreen()
        sprite = pygame.image.load(self.spritePath)
        sprite = pygame.transform.rotate(sprite, self.rotation)
        spriteRect = sprite.get_rect()

        rads = radians(self.rotation)

        spriteRect.centerx = self.originX + self.offsetY * sin(rads) + self.offsetX * cos(rads)
        spriteRect.centery = self.originY - self.offsetX * sin(rads) + self.offsetY * cos(rads)

        screen.blit(sprite, spriteRect)
        #screen.blit(sprite, (self.positionX, self.positionY))
