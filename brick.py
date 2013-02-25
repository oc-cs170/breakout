import pygame


class Brick(pygame.sprite.Sprite):
    """A Brick class that is aware of pygame.

    A Brick to play Breakout.
    Coordinates are the topleft of the Brick.
    """
    width = 55
    height = 20

    def __init__(self, x=0, y=0, color='red'):
        """Create a Brick object.

        Args:
            x: an int, the location of the brick
            y: an int, the location of the brick
            color: a string, the name of a color to fill the brick
        """
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((self.width, self.height))
        self.image.set_colorkey((1, 2, 3))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.set_color(color)

    def set_color(self, color):
        self.image.fill(pygame.color.Color(color))
