class Paddle(object):
    """A Paddle class that is aware of pygame.
    
    A small rectangular paddle to play Breakout.
    Coordinates are the center of the paddle.
    """
    def __init__(self, x, y, width, height):
        """Create a Paddle object.
        
        Args:
            x: an int, the initial x coordinate of the paddle
            y: an int, the initial y coordinate of the paddle
            width: an int, the initial width of the paddle
            height: an int, the initial height of the paddle
        """
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = ((x + width) / 2, (y + height) / 2, width, height)
        self.x_velocity, self.y_velocity = 0, 0

    def update(self):
        """Update the position of the paddle."""
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def draw(self, pygame, screen):
        """Draw the paddle on the screen.
        
        Args:
            pygame: the active pygame object
            screen: the active screen object
        """
        pygame.draw.rect(screen, (192, 192, 192), self.rect)
