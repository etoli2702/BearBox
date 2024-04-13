import pygame
from bear import getScreen, getWindowSize
import warnings

# Suppress libpng warning
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")

class Title:
    def __init__(self):
        self.visible = True
        self.menu = "assets/white.png"
        self.button = "assets/box_1/box_1.png"
        self.press = "assets/box_1/box_1_damage.png"
        self.isPress = False
        self.confirm = False
        self.location = [960,865,1080,930]
    
    def checkPress(self):
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (self.location[0] < mouse[0] < self.location[2] and self.location[1] < mouse[1] < self.location[3]):
                    self.isPress = True
            elif(event.type != pygame.MOUSEMOTION and self.isPress):
                self.isPress = False
                self.confirm = True
                


    def render(self):
        screen = getScreen()
        windowSize =getWindowSize()
        screen.blit(pygame.image.load("assets/background.png"), (0,0))
        
        if (self.isPress):
            p = pygame.image.load(self.press)
            
        else:
            p = pygame.image.load(self.button)
            
        p = pygame.transform.scale(p, (windowSize[0] / 16, windowSize[1] / 16))
        screen.blit(p, (windowSize[0] / 2, windowSize[1] / 1.25))


            

