import pygame

class App:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((1280, 720))
        self.clock = self.pygame.time.Clock()
    
    def run(self):
        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    return
                
            self.screen.fill("green")
            self.pygame.display.flip()
            self.clock.tick(60)