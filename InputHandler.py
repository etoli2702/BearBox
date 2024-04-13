import pygame
from pygame.math import Vector2
from math import nan, isnan

class InputHandler:
    def __init__(self):
        self.isDragging = False # Whether the player is currently dragging the mouse
        self.isCircling = False # Whether the player is making a circle with their mouse
        self.isCounterClockwiseCircle = False # If the player is dragging their mouse counterclockwise

        self.dragStartPos: tuple[int, int] = (0, 0) # The position that the current drag started at
        self.lastMousePos = None # The position of the mouse when we last updated
        self.lastDragVector: Vector2 = None # In the last update, the vector from the previous mouse position to the current one
        self.lastDragCross = nan # The cross product of the lastDragVector and the vector before it

        self.updateCount = 0 # The number of times this has been updated


    def update(self):
        self.updateCount += 1

        # If this is the first update in a drag motion
        dragJustStarted = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.isDragging = True
                    dragJustStarted = True
                    self.isCircling = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.isDragging = False


        if self.isDragging:
            if dragJustStarted:
                self.dragStartPos = pygame.mouse.get_pos()
                self.lastMousePos = pygame.mouse.get_pos()

            # Calculate data about whether it is circling. Only does this one in seven updates to make it more lenient.
            elif self.updateCount % 7 == 0:
                self.updateCircling()
        else:
            self.isCircling = False
            self.lastDragVector = None
            self.lastDragCross = nan

    def updateCircling(self):
        """Updates the status as to if the player is circling their mouse.

        Uses the cross product of the vector from the second-to-last mouse position and the last, and the vector from the last mouse position to the current.
        Recall that the cross product is positive if two vectors are counterclockwise, and if they are clockwise. As such, if the above cross product and the
        one before it are the same sign, the player is circling their mouse.
        """
        newDragVector = Vector2(pygame.mouse.get_pos()[0] - self.lastMousePos[0], pygame.mouse.get_pos()[1] - self.lastMousePos[1])
        self.lastMousePos = pygame.mouse.get_pos()

        # If the last drag vector is none, we cannot compute the cross product so we just return
        if self.lastDragVector is None:
            self.lastDragVector = newDragVector
            return

        thisCross = self.lastDragVector.cross(newDragVector)
        self.isCounterClockwiseCircle = thisCross <= 0

        if not isnan(self.lastDragCross):
            # Sets isCircling to true if this cross and the previous one have the same sign
            self.isCircling = self.isCircling and ((thisCross >= 0 and self.lastDragCross >= 0) or (thisCross <= 0 and self.lastDragCross <= 0))
        
        self.lastDragCross = thisCross
        self.lastDragVector = newDragVector