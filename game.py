import time, pygame, threading, random

class Game:
    display = pygame.display.set_mode([800, 600])
    white = (255, 255, 255)
    size_up = 1
    
    def displayUpdate(self):
        pygame.display.flip()
    
    
    def gameSetting(self):
        pygame.display.set_caption('Game Tester')
        self.display.fill(self.white)
        
    def gameInteract(self, events):
        mouse_motion, scroll_mouse = 4, 2
        down_click, up_click = 5, 6
    
        #Up width line
        self.size_up += 1 if events.type == down_click and events.button == scroll_mouse else 0    
        
        # pencil
        if events.type == mouse_motion and events.buttons[0] != 0:
            pygame.draw.line(self.display, (0, 0, 0), events.pos, events.pos, self.size_up)
                
        # eraser 
        elif events.type == mouse_motion and events.buttons[2] != 0:
            pygame.draw.line(self.display, self.white, events.pos, events.pos, 100)
        
        print(self.size_up)
        
        
        
    def gameWorking(self):
        status = True
        
        while status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False
                self.gameInteract(event)
            self.displayUpdate()
                
    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        self.gameSetting()
        self.gameWorking()
        pygame.quit()
            
    

Game().run()