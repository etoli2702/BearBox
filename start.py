import pygame
from bear import getScreen

class Title:
    def __init__(self):
        self.confirm = False
        self.choice = 0
        self.buttons = [
            {"button": "assets/stage1.png", "press": "assets/stage1p.png", "isPress": False, "confirm": False,
             "location": [100, 400, 300, 600]},
            {"button": "assets/stage2.png", "press": "assets/stage2p.png", "isPress": False, "confirm": False,
             "location": [330, 400, 530, 600]},
            {"button": "assets/exit.png", "press": "assets/exitp.png", "isPress": False, "confirm": False,
             "location": [560, 400, 760, 600]}
        ]

    def update_location(self, window_size):
        # Update self.location based on the new window size
        if window_size:
            for button in self.buttons:
                button_width = window_size[0] / 2.43
                button_height = window_size[1] / 1.2
                button[0] = button_width  
                button[2] = button_width + 120 
                button[1] = button_height  
                button[3] = button_height + 45 
            
    def checkPress(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.buttons[0]["location"][0] < mouse[0] < self.buttons[0]["location"][2] and self.buttons[0]["location"][1] < mouse[1] < self.buttons[0]["location"][3]):
                    self.buttons[0]["isPress"] = True
                elif (self.buttons[1]["location"][0] < mouse[0] < self.buttons[1]["location"][2] and self.buttons[1]["location"][1] < mouse[1] < self.buttons[1]["location"][3]):
                    self.buttons[1]["isPress"] = True
                elif (self.buttons[2]["location"][0] < mouse[0] < self.buttons[2]["location"][2] and self.buttons[2]["location"][1] < mouse[1] < self.buttons[2]["location"][3]):
                    self.buttons[2]["isPress"] = True    
            elif event.type == pygame.MOUSEMOTION:
                if not (self.buttons[0]["location"][0] < mouse[0] < self.buttons[0]["location"][2] and self.buttons[0]["location"][1] < mouse[1] < self.buttons[0]["location"][3]):
                    self.buttons[0]["isPress"] = False
                elif not(self.buttons[1]["location"][0] < mouse[0] < self.buttons[1]["location"][2] and self.buttons[1]["location"][1] < mouse[1] < self.buttons[1]["location"][3]):
                    self.buttons[1]["isPress"] = False
                elif not(self.buttons[2]["location"][0] < mouse[0] < self.buttons[2]["location"][2] and self.buttons[2]["location"][1] < mouse[1] < self.buttons[2]["location"][3]):
                    self.buttons[2]["isPress"] = False 


            elif self.buttons[0]["isPress"]:
                self.buttons[0]["isPress"] = False
                self.buttons[0]["confirm"] = True
                self.confirm = True
                self.choice = 0
            elif self.buttons[1]["isPress"]:
                self.buttons[1]["isPress"] = False
                self.buttons[1]["confirm"] = True
                self.confirm = True
                self.choice = 1
            elif self.buttons[2]["isPress"]:
                self.buttons[2]["isPress"] = False
                self.buttons[2]["confirm"] = True
                self.confirm = True
                self.choice = 2



                


    def render(self):
        screen = getScreen()
        windowSize = pygame.display.get_window_size()
        screen.blit(pygame.image.load("assets/background.png"), (0,0))
        
        for button in self.buttons:
            if button["isPress"]:  # Check if the button is pressed
                button_image = pygame.image.load(button["press"])  # Load the pressed button image
            else:
                button_image = pygame.image.load(button["button"])  # Load the normal button image
            
            # Scale the button image based on the difference between the x-coordinates and y-coordinates of the button's location list
            button_image = pygame.transform.scale(button_image, (int(button["location"][2] - button["location"][0]), int(button["location"][3] - button["location"][1])))
            
            # Blit the button image onto the screen at the appropriate position specified by the button's location list
            screen.blit(button_image, (button["location"][0], button["location"][1]))
