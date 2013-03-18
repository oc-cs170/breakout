import pygame

WIDTH = 58
HEIGHT = 32
COLORS = ('red', 'yellow', 'purple', 'green', 'grey')


class Brick(pygame.sprite.Sprite):
    """A Brick class that is aware of pygame.

    Args:
        x: an int, the horizontal location of the brick
        y: an int, the vertical location of the brick
        color: a str, name of brick color {red, yellow, purple, green, grey}
               default grey
    """
    images = None

    def __init__(self, x=0, y=0, color=None):
        """Create a Brick object.

        Args:
            x: an int, the location of the brick
            y: an int, the location of the brick
            color: a string, the name of a color to fill the brick
        """
        # Initialize sprite
        super(Brick, self).__init__()

        if Brick.images is None:
            images = [pygame.image.load('element_' + c + '_rectangle.png').convert_alpha()
                      for c in COLORS]
            Brick.images = [pygame.transform.scale(image, (WIDTH, HEIGHT))
                            for image in images]

        self.set_color(color or 'grey')
        self.rect = self.image.get_rect(topleft=(x, y))

    def set_color(self, color):
        if color in COLORS:
            index = COLORS.index(color)
        else:
            index = -1
        self.image = Brick.images[index]
