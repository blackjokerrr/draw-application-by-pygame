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
        mouse_motion = 4
        left_click = 5
        right_click = 6
        
        while status:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    status = False

                elif event.type == mouse_motion and event.buttons[0] != 0:
                    pygame.draw.line(self.display, (0, 0, 0), event.pos, event.pos, 5)
                    
                elif event.type == mouse_motion and event.buttons[2] != 0:
                    pygame.draw.line(self.display, self.white, event.pos, event.pos, 100)
                    
                    
            self.displayUpdate()
                
    def run(self):
        pygame.init()
        pygame.display.init()
        pygame.mixer.init()
        self.gameSetting()
        self.gameInteract()
        pygame.quit()
            
    

Game().run()