import pygame


class Brick(pygame.sprite.Sprite):
    brick = pygame.Surface((60, 42))
    pygame.draw.rect(brick, pygame.Color('red'), pygame.Rect((0, 0), brick.get_size()), 1)
    brick.set_colorkey(pygame.Color('black'))
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.brick
        self.rect = pygame.Rect((0, 0), self.image.get_size())

        self.rect.topleft = (x, y)
        
        