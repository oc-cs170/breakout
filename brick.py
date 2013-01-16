import pygame


class Brick(object):
    """A Bricks class that is aware of pygame.

    Many small rectangular bricks to play Breakout.
    Coordinates are the top left of the brick.
    """
    def __init__(self, x, y):
        """Create a Bricks object.

        Args:
            screen_size: an int 2-tuple of screen width and height
        """
        self.screen_width = 600
        self.screen_height = 700

        # Size and location
        self.width, self.height = 50, 16
        self.x, self.y = x, y
        self.rect = (self.x, self.y, self.width, self.height)

        self.color = 255, 128, 128

    def draw(self, screen):
        """Draw the bricks on the screen.

        Args:
            screen: the active screen object
        """

        pygame.draw.rect(screen, self.color, self.rect)
