import pygame
from pygame.math import Vector2
from math import nan, isnan

class InputHandler:
    def __init__(self):
        self.isDragging = False
        self.dragStartPos: tuple[int, int] = (0, 0)
        self.lastDragEndpoint = None
        self.lastDragVector: Vector2 = None
        self.lastDragCross = nan

        self.isCounterClockwiseCircle = False
        self.isCircling = False

        self.updateCount = 0


    def update(self):
        self.updateCount += 1

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
                self.lastDragEndpoint = pygame.mouse.get_pos()
            elif self.updateCount % 7 == 0:
                newDragVector = Vector2(pygame.mouse.get_pos()[0] - self.lastDragEndpoint[0], pygame.mouse.get_pos()[1] - self.lastDragEndpoint[1])
                self.lastDragEndpoint = pygame.mouse.get_pos()

                if self.lastDragVector is None:
                    self.lastDragVector = newDragVector
                    return
                
                thisCross = self.lastDragVector.cross(newDragVector)
                self.isCounterClockwiseCircle = thisCross <= 0

                if not isnan(self.lastDragCross):
                    self.isCircling = self.isCircling and ((thisCross >= 0 and self.lastDragCross >= 0) or (thisCross <= 0 and self.lastDragCross <= 0))
                
                self.lastDragCross = thisCross
                self.lastDragVector = newDragVector
        else:
            print("Stopped")
            self.isCircling = False
            self.lastDragVector = None
            self.lastDragCross = nan