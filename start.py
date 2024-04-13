import pygame

class Title:
    def __init__(self):
        self.visible = True
        self.menu = ""
        self.button = ""
        self.press = ""
        self.isPress = False
        self.location = [0,0,0,0]
    
    def checkPress(self):
        mouse = mouse.get_pos()
        for event in pygame.event.get():
            if (self.location[0] < mouse[0] < self.location[1] and self.location[0] < mouse[1] < self.location[1] and event.type == pygame.MOUSEBUTTONDOWN):
                self.isPress = True

