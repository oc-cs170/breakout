import pygame


class Brick(object):
    """A Brick class that is aware of pygame."""

    def __init__(self, screen_width, screen_height):
        # Create a Brick object.

        # Creation parameter
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Size and location
        self.width, self.height = 80, 16
        self.x, self.y = self.screen_width / 2, 0 + self.height
        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)

        
        self.color = 255, 255, 255

    def draw(self, screen):
        
        pygame.draw.rect(screen, self.color, self.rect)

   
    
