from typing import TYPE_CHECKING

import pygame

from interactive_bezier.models import Point

if TYPE_CHECKING:
    from config import Config


class App:
    def __init__(self, config: "Config"):
        self.config = config
        self.pygame = pygame
        self.pygame.init()

        if self.config.user_settings["fullscreen"]:
            self.display_size = (self.pygame.display.Info().current_w, self.pygame.display.Info().current_h)
        else:
            self.display_size = tuple(self.config.user_settings["resolution"])

        self.surface = self.pygame.display.set_mode(size=self.display_size)
        self.clock = self.pygame.time.Clock()
        self.surface.fill(color=pygame.Color(96, 96, 96))
        self.cart_to_px_offset = ... # display_size / 2?


    
    def mainloop(self):          
        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    return

                if event.type == self.pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())
                    # self.pygame.draw.circle(self.surface, "blue", pygame.mouse.get_pos(), 10)
                    point = Point()
            
            self.pygame.display.flip()
            self.clock.tick(60)
