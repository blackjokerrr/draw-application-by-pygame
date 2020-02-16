import time, pygame, threading, random

class Game:
    display = pygame.display.set_mode([800, 600])
    white = (255, 255, 255)
    
    def displayUpdate(self):
        pygame.display.flip()
    
    
    def gameSetting(self):
        pygame.display.set_caption('Game Tester')
        self.display.fill(self.white)
    
    def gameInteract(self):
        status = True
        mouse_motion, scroll_mouse = 4, 2
        down_click, up_click = 5, 6
        size_up = 1
        
        while status:
            for event in pygame.event.get():
                #Up width line
                size_up += 1 if event.type == down_click and event.button == scroll_mouse else 0
                
                # close application
                if event.type == pygame.QUIT:
                    status = False
                
                # pencil
                elif event.type == mouse_motion and event.buttons[0] != 0:
                    pygame.draw.line(self.display, (0, 0, 0), event.pos, event.pos, size_up)
                
                # eraser 
                elif event.type == mouse_motion and event.buttons[2] != 0:
                    pygame.draw.line(self.display, self.white, event.pos, event.pos, 100)
                
                #print(event)
            self.displayUpdate()
                
    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        self.gameSetting()
        self.gameInteract()
        pygame.quit()
            
    

Game().run()