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

class Timer:
    def __init___ (self):
        self.elapsed_time = 0
        self.running = False

    def update (self, game_time):
        if self.running:
            self.elapsed_time += 1