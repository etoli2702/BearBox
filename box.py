'''
Author: Elijah, Chris
Date: 04/13/2024
Project: Hack KU - Bear Box
Last modified: 04/14/2024
Purpose: Represent a box for the game to test.
'''

import pygame
import bear
import BoxElement
from math import cos, pi

# The number of frames in the roll and bounce animations
ROLL_FRAMES = 20
BOUNCE_FRAMES = 20

class Box:
    def __init__(self, stage = 1, boxSize = [200,200,600,600], elements: list[BoxElement.BoxElement] = []):
        """Create a Box.

        Args:
            stage (int, optional): The box number to create. Currently 1 and two are supported. Defaults to 1.
            boxSize (list, optional): The default bounding box of the box, in pixels. Defaults to [200,200,600,600].
            elements (list[BoxElement.BoxElement], optional): The components that make up this box. i.e. all of its latches and locks... Defaults to [].
        """
        self.health = 40

        # The paths to this boc's assets
        self.image = "assets/box_" + str(stage) + "/box_" + str(stage) + ".png"
        self.hurt = "assets/box_" + str(stage) + "/box_" + str(stage) + "_damage.png"

        # The default bounding box
        self.xRange = [boxSize[0],boxSize[2]]
        self.yRange = [boxSize[1],boxSize[3]]
        self.rotation = 0

        # Sets this Box's component elements
        self.elements = elements
        for element in elements:
            element.setParent(self)

        # Whether or not damage was taken since the last update
        self.taken = False

        # Variables used during the roll animation
        self.rolling = False
        self.rollCounterClockwise = False
        self.rollFrames = 0

        # Variables used during the bounce animation
        self.ogYRange = []
        self.bouncing = False
        self.bounceFrames = 0

    def rotate(self, rotation):
        self.rotation = rotation
        for element in self.elements:
            element.rotate(rotation)

    def damage(self):
        if self.health <= 0:
            return
        self.health -= 1
        self.taken = True

    def getScaledXRange(self) -> list[float]:
        """Scale this box's bounding box width to the screen size.

        Returns:
            list[float]: This box's bounding box width, scaled to the screen size.
        """
        return [item/800*pygame.display.get_window_size()[0] for item in self.xRange]
    
    def getScaledYRange(self) -> list[float]:
        """Scale this box's bounding box height to the screen size.

        Returns:
            list[float]: This box's bounding box height, scaled to the screen size.
        """
        return [item/600*pygame.display.get_window_size()[1] for item in self.yRange]
        
    def checkHealth(self) -> bool:
        """Checks whether the box's health is above zero.

        Returns:
            bool: True if the box's health is above zero.
        """
        if self.health <= 0:
            return False
        return True

    def action(self):
        if (self.taken):
            return False
        return True
    
    def bounce(self):
        """Tries to initiate a bounce. Only succeeds if it is not already bouncing or rolling.
        """
        if self.bouncing:
            return
        self.bouncing = not self.rolling
        if self.bouncing:
            self.ogYRange = self.yRange

    def roll(self, counterclockwise: bool):
        """Tries to initiate a roll. Only succeeds if it is not already bouncing.
        """
        self.rolling = not self.bouncing
        self.rollCounterClockwise = counterclockwise

    def click(self, xPosition, yPosition):

        # Try to click on each of its child elements. Damage them and return if the click is in their bounding box.
        for element in self.elements:
            if(element.click(xPosition, yPosition)):
                print(f"Clicked on {element.spritePath}")
                element.damage()
                return
        
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        if (xRangeScaled[0] < xPosition < xRangeScaled[1]) and (yRangeScaled[0] < yPosition < yRangeScaled[1]):
            print("Clicked on the box!")
            self.damage()

    def contains(self, xPosition, yPosition):
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        return xRangeScaled[0] < xPosition < xRangeScaled[1] and yRangeScaled[0] < yPosition < yRangeScaled[1]

    def update(self):
        # Update the roll animation
        if self.rolling:
            self.rollFrames += 1
            if self.rollFrames <= ROLL_FRAMES:
                self.rotate(360/ROLL_FRAMES * self.rollFrames * (1 if self.rollCounterClockwise else -1))
            else:
                self.rollFrames = 0
                self.rolling = False
                self.rotate(0)
        # Update the bounce animation
        elif self.bouncing:
            if self.bounceFrames <= BOUNCE_FRAMES:
                heightDelta = 50 * cos(pi * self.bounceFrames/BOUNCE_FRAMES)
                self.yRange = [item - heightDelta for item in self.yRange]
                self.rotate(360/BOUNCE_FRAMES * self.bounceFrames)
            else:
                self.bounceFrames = 0
                self.bouncing = False
                self.rotate(0)
                self.yRange = self.ogYRange
            self.bounceFrames += 1

    def render(self):
        screen = bear.getScreen()
        windowSize = pygame.display.get_window_size()

        # Get the correct sprite based on whether the box took damage
        if self.taken and self.health >= 0:
            p = pygame.image.load(self.hurt)
            self.taken = False
        else:
            p = pygame.image.load(self.image)
            self.taken = False

        # Scale and rotate the sprite
        p = pygame.transform.scale(p, (windowSize[0] / 2, windowSize[1] / 2))
        p = pygame.transform.rotate(p, self.rotation)

        spriteRect = p.get_rect()

        # Translate the sprite to the correct position
        xRangeScaled = self.getScaledXRange()
        yRangeScaled = self.getScaledYRange()
        spriteRect.centerx = xRangeScaled[0] + (xRangeScaled[1] - xRangeScaled[0])/2
        spriteRect.centery = yRangeScaled[0] + (yRangeScaled[1] - yRangeScaled[0])/2

        screen.blit(p, spriteRect)

        # Render the sprite's componet elements.
        for element in self.elements:
            if element.health > 0:
                element.render()

        


