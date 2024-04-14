'''
Author: Sasha Sharman
Date: 04/13/2024
Project: Hack KU - Bear Box
Last modified: 04/13/2024
Purpose: Render the healthbar.
'''
import pygame
from bear import getScreen


class Healthbar:
    def __init__(self):
        pass
    def currentHealth(self, global_health):
        """Return a list of assests that need to be rendered in the healthbar."""
        healthbar = list()
        for num in range(8, (global_health + 9) // 10, -1):
            if num > 0:
                healthbar.append(f"assets/healthbar/food_{num}.png")
        return(healthbar)
        
    def render(self, global_health):
        screen = getScreen()
        windowSize = pygame.display.get_window_size()
        healthbar = self.currentHealth(global_health)
        for index, item in enumerate(healthbar):
            image = pygame.image.load(item)
            image = pygame.transform.scale(image, (int(windowSize[0] / 12), int(windowSize[1] / 12)))  
            screen.blit(image, ((10 + index * 60)*windowSize[0]/800, 20 * windowSize[1]/600))

class Timers:
    def __init__ (self):
        self.elapsed_time = 0
        self.running = False
        self.sec = 0
        self.min = 0
        self.start = 0

    def update (self, game_time):
        self.elapsed_time = game_time - self.start
        
        if(self.elapsed_time % 10 == 0):
            self.start += 10
            if self.sec == 60:
                self.min += 1
                self.sec = 1
            else:
                self.sec += 1

    def render(self):
        font = pygame.font.Font('ps2p.ttf', 32)        
        windowSize = pygame.display.get_window_size()
        if self.sec < 50:
            text = font.render(f"{self.min:02}:{self.sec:02}", True, (255, 255, 255))
        else:
            text = font.render(f"{self.min:02}:{self.sec:02}", True, (255, 0, 0))

        screen = getScreen()
        screen.blit(text, ((10 * 60)*windowSize[0]/800, 50 * windowSize[1]/600))
