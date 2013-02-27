import pygame


class Brick(pygame.sprite.Sprite):
    """A Bricks class that is aware of pygame.

    Many small rectangular bricks to play Breakout.
    Coordinates are the top left of the brick.
    """
    width = 50
    height = 16

    def __init__(self, x=0, y=0, color='#F08080'):
        """Create a Bricks object.

        Args:
            screen_size: an int 2-tuple of screen width and height
        """
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey((1, 2, 3))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.set_color(color)

    def set_color(self, color):
        self.image.fill(pygame.color.Color(color))
