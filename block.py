import pygame

class Block(object):
    """ Blocks that will break when ball hits it"""
    def __init__(self,screen_width, screen_height, x, y):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.width, self.height = 55, 16
        self.x, self.y = x, y

        self.rect = (self.x, self.y, self.width, self.height)
        self.color = 255,255,255

    def draw(self, screen):
        """draw the blocks"""
        pygame.draw.rect(screen, self.color, self.rect,1)

    
