'''
Author: Sasha Sharman
Date: 04/13/2024
Project: Hack KU - Bear Box
Last modified: 04/13/2024
Purpose: Render the healthbar.
'''
import pygame

class Healthbar:
    def __init__(self):
        pass
    def current_health(self, global_health):
        healthbar = list()
        for num in range(8, global_health // 10, -1):
            print(num)
            healthbar.append(f"healthbar/food_{num}.png")
        return(healthbar)
        
from healthbar import Healthbar
health = Healthbar()
print(health.current_health(0))
        
