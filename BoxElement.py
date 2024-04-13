import pygame
import bear
from math import sin, cos, radians
import box

class BoxElement:
    def __init__(self, boxNumber: int, elementName: str, parent: "box.Box", offset: tuple[int, int] = (0, 0), scale: tuple[int, int] = (100, 100)):
        """Represents a component, like a latch or lock, of a Box.

        Args:
            boxNumber (int): The box that this element 
            elementName (str): _description_
            parent (box.Box): _description_
            offset (tuple[int, int], optional): _description_. Defaults to (0, 0).
            scale (tuple[int, int], optional): _description_. Defaults to (100, 100).
        """
        self.spritePath = "assets/box_" + str(boxNumber) + "/" + elementName + ".png"
        self.scale = scale
        self.offsetX = offset[0]
        self.offsetY = offset[1]
        self.rotation = 0
        self.parent = parent

    def update(self):
        pass

    def click(self, positionX, positionY):
        rads = radians(self.rotation)

        scale = (
            pygame.display.get_window_size()[0]/800 * self.scale[0],
            pygame.display.get_window_size()[0]/600 * self.scale[1]
        )
        
        # The elements may be offset and rotated from (0,0). Instead of trying to figure out if the click point is in that bounding box directly, we instead
        # apply the inverse of those transforms to the point and see if is as the (importantly non-rotated) bounding box centered at (0, 0)
        inversePositionX = positionX - (self.parent.xRange[0] + (self.parent.xRange[1] - self.parent.xRange[0])/2 + self.offsetY * sin(rads) + self.offsetX * cos(rads))
        inversePositionY = positionY - (self.parent.yRange[0] + (self.parent.yRange[1] - self.parent.yRange[0])/2 - self.offsetX * sin(rads) + self.offsetY * cos(rads))

        return -scale[0]/2 < inversePositionX < scale[0]/2 and -scale[1]/2 < inversePositionY < scale[1]/2
    
    def setParent(self, parent: "box.Box"):
        self.parent = parent

    def rotate(self, rotation):
        self.rotation = rotation

    def offset(self, offsetX, offsetY):
        self.offsetX = offsetX
        self.offsetY = offsetY

    def render(self):
        screenSizeScale = (
            pygame.display.get_window_size()[0]/800,
            pygame.display.get_window_size()[1]/600
        )
        screen = bear.getScreen()
        sprite = pygame.image.load(self.spritePath)
        sprite = pygame.transform.scale(sprite, (screenSizeScale[0] * self.scale[0], screenSizeScale[1] * self.scale[1]))
        sprite = pygame.transform.rotate(sprite, self.rotation)
        spriteRect = sprite.get_rect()

        rads = radians(self.rotation)

        spriteRect.centerx = self.parent.xRange[0] + (self.parent.xRange[1] - self.parent.xRange[0])/2 + screenSizeScale[0]*(self.offsetY * sin(rads) + self.offsetX * cos(rads))
        spriteRect.centery = self.parent.yRange[0] + (self.parent.yRange[1] - self.parent.yRange[0])/2 - screenSizeScale[1]-(self.offsetX * sin(rads) + self.offsetY * cos(rads))

        screen.blit(sprite, spriteRect)
