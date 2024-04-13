import pygame
from bear import getScreen
import warnings

# Suppress libpng warning
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")

class Title:
    def __init__(self):
        self.visible = True
        self.menu = "assets/white.png"
        self.button = "assets/start.png"
        self.press = "assets/start2.png"
        self.isPress = False
        self.confirm = False
        self.location = [pygame.display.get_window_size()[0] / 2.43,pygame.display.get_window_size()[1] / 1.2,pygame.display.get_window_size()[0] / 1.78,pygame.display.get_window_size()[0] / 1.1]
    
    def checkPress(self):
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (self.location[0] < mouse[0] < self.location[2] and self.location[1] < mouse[1] < self.location[3]):
                    self.isPress = True
            elif(event.type == pygame.MOUSEMOTION):
                if (self.location[0] > mouse[0] or mouse[0] > self.location[2] 
                    or self.location[1] > mouse[1] or mouse[1] > self.location[3]):
                    self.isPress = False    
            elif(self.isPress):
                self.isPress = False
                self.confirm = True

                


    def render(self):
        screen = getScreen()
        windowSize = pygame.display.get_window_size()
        screen.blit(pygame.image.load("assets/background.png"), (0,0))
        
        if (self.isPress):
            p = pygame.image.load(self.press)
            
        else:
            p = pygame.image.load(self.button)
            
        p = pygame.transform.scale(p, (windowSize[0] / 4, windowSize[1] / 3))
        screen.blit(p, (windowSize[0] / 2.75, windowSize[1] / 1.5))


            

