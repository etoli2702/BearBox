import pygame
from pygame.math import Vector2
import pygame.mouse as mouse
from math import nan, isnan
import time

# The maximim distance before two mouse postions are said to be the same
MAX_MOUSE_POSITION_DISTANCE = 50

# The distance that the mouse has to move from its original position before it can be said to have made a circle
REQUIRED_DISTANCE_FOR_CIRCLE = 200

# The maximum length, in seconds, for a mouse input to be considered a click
MAX_MOUSE_DOWN_TIME_FOR_CLICK_SECONDS = 0.2

class InputHandler:
    def __init__(self):
        self.isDragging = False # Whether the player is currently dragging the mouse
        self.isCircling = False # Whether the player is making a circle with their mouse
        self.isCounterClockwiseCircle = False # If the player is dragging their mouse counterclockwise

        # The max bounds of the current drag. (minX, minY, maxX, maxY)
        self.dragBoundingBox: tuple[int, int, int, int]

        self.dragStartPos: tuple[int, int] = (0, 0) # The position that the current drag started at
        self.lastMousePos = None # The position of the mouse when we last updated
        self.lastDragVector: Vector2 = None # In the last update, the vector from the previous mouse position to the current one
        self.lastDragCross = nan # The cross product of the lastDragVector and the vector before it

        self.mouseDownTime = 0 # The time at which the mouse was pressed
        self.hasClicked = False # Whether the mouse has been clicked since the game loop last checked

        self.updateCount = 0 # The number of times this has been updated

    def update(self):
        self.updateCount += 1

        self.checkMouseState()

        if self.isDragging:
            # Calculate data about whether it is circling. Only does this one in seven updates to make it more lenient.
            if self.updateCount % 7 == 0:
                self.updateCircling()
            
            self.updateDragBoundingBox()

    def updateCircling(self):
        """Updates the status as to if the player is circling their mouse.

        Uses the cross product of the vector from the second-to-last mouse position and the last, and the vector from the last mouse position to the current.
        Recall that the cross product is positive if two vectors are counterclockwise, and if they are clockwise. As such, if the above cross product and the
        one before it are the same sign, the player is circling their mouse.
        """
        newDragVector = Vector2(mouse.get_pos()[0] - self.lastMousePos[0], mouse.get_pos()[1] - self.lastMousePos[1])
        self.lastMousePos = mouse.get_pos()

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

    def updateDragBoundingBox(self):
        self.dragBoundingBox = (
            min(self.dragBoundingBox[0], mouse.get_pos()[0]),
            min(self.dragBoundingBox[1], mouse.get_pos()[1]),
            max(self.dragBoundingBox[2], mouse.get_pos()[0]),
            max(self.dragBoundingBox[3], mouse.get_pos()[1]))

    def hasMadeCircle(self) -> bool:
        if not self.isCircling:
            return False
        
        hasMouseReturnedToStartPosition = Vector2(mouse.get_pos()[0] - self.dragStartPos[0], mouse.get_pos()[1] - self.dragStartPos[1]).length() <= MAX_MOUSE_POSITION_DISTANCE

        hasMouseLeftStartPosition = Vector2(self.dragBoundingBox[0] - self.dragBoundingBox[2], self.dragBoundingBox[1] - self.dragBoundingBox[3]).length() >= REQUIRED_DISTANCE_FOR_CIRCLE

        return hasMouseLeftStartPosition and hasMouseReturnedToStartPosition
    
    def hasDoneBounce(self) -> bool:
        if (not self.isDragging) or self.isCircling:
            return False

        # If the mouse is lower than where the bounce started.
        hasMouseReturnedToStartPosition = self.dragStartPos[1] < mouse.get_pos()[1]

        hasMouseLeftStartPosition = self.dragBoundingBox[3] - self.dragBoundingBox[1] >= REQUIRED_DISTANCE_FOR_CIRCLE

        return hasMouseLeftStartPosition and hasMouseReturnedToStartPosition
    
    def consumeClick(self) -> "tuple[int, int] | None":
        """Returns the click position if the player has clicked since the last time the game checked, or None otherwise.

        Also updates self.hasClicked to False.
        Returns:
            tuple[int, int] | None: Ths click position if the player has clicked since the last time this function was called, or None otherwise.
        """
        if self.hasClicked:
            self.hasClicked = False
            return self.dragStartPos
        
        return None
    
    def startDrag(self):
        self.dragStartPos = mouse.get_pos()
        self.lastMousePos = mouse.get_pos()
        self.isDragging = True
        self.isCircling = True
        self.dragBoundingBox = (mouse.get_pos()[0], mouse.get_pos()[1], mouse.get_pos()[0], mouse.get_pos()[1])

    def endDrag(self):
        self.isCircling = False
        self.isDragging = False
        self.lastDragVector = None
        self.lastDragCross = nan

    def restartDrag(self):
        self.endDrag()
        self.startDrag()

    def checkMouseState(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.startDrag()

                    # Set the time that the mouse was pressed
                    self.mouseDownTime = time.process_time()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.endDrag()

                    # If the amount of time since the button was pressed is less than the max time,
                    if time.process_time() - self.mouseDownTime < MAX_MOUSE_DOWN_TIME_FOR_CLICK_SECONDS:
                        self.hasClicked = True