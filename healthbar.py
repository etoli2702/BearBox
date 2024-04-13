'''
Author: Sasha Sharman
Date: 04/13/2024
Project: Hack KU - Bear Box
Last modified: 04/13/2024
Purpose: Render the healthbar.
'''
import pygame
from bear import getScreen, getWindowSize

class Healthbar:
    def __init__(self):
        pass
    def current_health(self, global_health):
        """Return a list of assests that need to be rendered in the healthbar."""
        healthbar = list()
        for num in range(8, global_health // 10, -1):
            healthbar.append(f"assests/healthbar/food_{num}.png")
        return(healthbar)
        
    def render(self, global_health):
        # screen = getScreen()
        # windowSize = getWindowSize()
        healthbar = self.current_health(global_health)
        for item, index in enumerate(healthbar):
            r = pygame.image.load(item, (50 + index * 100, 50))
           # r = pygame.transform.scale(r, (windowSize[0] / 3, windowSize[1] / 3))
           # self.screen.blit(r, (windowSize[0] / 4, windowSize[1] / 4))
           # pygame.display.flip()