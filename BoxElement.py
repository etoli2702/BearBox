'''
Author: Chris
Date: 04/13/2024
Project: Hack KU - Bear Box
Last modified: 04/14/2024
Purpose: Build the box elements.
'''

import pygame
import bear
from math import sin, cos, radians
import box

class BoxElement:
    def __init__(self, boxNumber: int, elementName: str, parent: "box.Box", offset: tuple[int, int] = (0, 0), scale: tuple[int, int] = (100, 100)):
        """Represents a component, like a latch or lock, of a Box.

        Args:
            boxNumber (int): The box that this element belongs to.
            elementName (str): The name of this element as it appears in the assets folsder.
            parent (box.Box): The Box this element belongs to.
            offset (tuple[int, int], optional): The of the element, from the center of its parent box. Defaults to (0, 0).
            scale (tuple[int, int], optional): The size of the element's bounding box. Defaults to (100, 100).
        """

        # The path to the box's sprites
        self.spritePath = "assets/box_" + str(boxNumber) + "/" + elementName + ".png"
        self.hurt = "assets/box_" + str(boxNumber) + "/" + elementName + "_damage.png"

        # The size of the element's bounding box
        self.scale = scale

        # The offset of the element, from the center of its parent box.
        self.offsetX = offset[0]
        self.offsetY = offset[1]

        self.rotation = 0
        self.parent = parent
        self.health = 20

        # Whether damage was taken since the last frame
        self.taken = False

    def update(self):
        pass

    def damage(self):
            if self.health <= 0:
                return
            self.health -= 1
            self.taken = True

    def click(self, positionX: int, positionY: int) -> bool:
        """Checks whether a given click lands inside this element and performs this element's onClick actions as needed.

        Args:
            positionX (int): The x position of the click
            positionY (int): The y position of the click

        Returns:
            bool: Whether the click falls within this element's bounding box.
        """
        rads = radians(self.rotation)

        screenSizeScale = (
            pygame.display.get_window_size()[0]/800,
            pygame.display.get_window_size()[1]/600
        )

        scale = (
            pygame.display.get_window_size()[0]/800 * self.scale[0],
            pygame.display.get_window_size()[1]/600 * self.scale[1]
        )
        
        # The elements may be offset and rotated from (0,0). Instead of trying to figure out if the click point is in that bounding box directly, we instead
        # apply the inverse of those transforms to the point and see if is as the (importantly non-rotated) bounding box centered at (0, 0)
        parentXRange  = self.parent.getScaledXRange()
        parentYRange  = self.parent.getScaledYRange()

        inversePositionX = positionX - (parentXRange[0] + (parentXRange[1] - parentXRange[0])/2 + screenSizeScale[1]*self.offsetY * sin(rads) + screenSizeScale[0]*self.offsetX * cos(rads))
        inversePositionY = positionY - (parentYRange[0] + (parentYRange[1] - parentYRange[0])/2 - screenSizeScale[0]*self.offsetX * sin(rads) + screenSizeScale[1]*self.offsetY * cos(rads))

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
        if self.taken:
            sprite = pygame.image.load(self.hurt)
            self.taken = False
        else:
            sprite = pygame.image.load(self.spritePath)
    
        # Scale and rotate the sprite
        sprite = pygame.transform.scale(sprite, (screenSizeScale[0] * self.scale[0], screenSizeScale[1] * self.scale[1]))
        sprite = pygame.transform.rotate(sprite, self.rotation)
        spriteRect = sprite.get_rect()

        rads = radians(self.rotation)

        parentXRange  = self.parent.getScaledXRange()
        parentYRange  = self.parent.getScaledYRange()

        # Translate the sprite based on its parent's current position and its own offset and rotation.
        spriteRect.centerx = parentXRange[0] + (parentXRange[1] - parentXRange[0])/2 + screenSizeScale[1]*self.offsetY * sin(rads) + screenSizeScale[0]*self.offsetX * cos(rads)
        spriteRect.centery = parentYRange[0] + (parentYRange[1] - parentYRange[0])/2 - screenSizeScale[0]*self.offsetX * sin(rads) + screenSizeScale[1]*self.offsetY * cos(rads)

        screen.blit(sprite, spriteRect)
