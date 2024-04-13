import pygame
import bear
from math import sin, cos, radians
import box

class BoxElement:
    def __init__(self, boxNumber: int, elementName: str, parent: "box.Box", offset: tuple[int, int] = (0, 0), scale: tuple[int, int] = (100, 100)):
        self.spritePath = "assets/box_" + str(boxNumber) + "/" + elementName + ".png"
        self.scale = scale
        self.offsetX = offset[0]
        self.offsetY = offset[1]
        self.rotation = 0
        self.parent = parent

    def update(self):
        pass

    def setParent(self, parent: "box.Box"):
        self.parent = parent

    def rotate(self, rotation):
        self.rotation = rotation

    def offset(self, offsetX, offsetY):
        self.offsetX = offsetX
        self.offsetY = offsetY

    def render(self):
        screen = bear.getScreen()
        sprite = pygame.image.load(self.spritePath)
        sprite = pygame.transform.scale(sprite, self.scale)
        sprite = pygame.transform.rotate(sprite, self.rotation)
        spriteRect = sprite.get_rect()

        rads = radians(self.rotation)

        spriteRect.centerx = self.parent.xRange[0] + (self.parent.xRange[1] - self.parent.xRange[0])/2 + self.offsetY * sin(rads) + self.offsetX * cos(rads)
        spriteRect.centery = self.parent.yRange[0] + (self.parent.yRange[1] - self.parent.yRange[0])/2 - self.offsetX * sin(rads) + self.offsetY * cos(rads)

        screen.blit(sprite, spriteRect)
