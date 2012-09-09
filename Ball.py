class Ball(object):
    """A Ball class that is aware of pygame.
    
    Longer description goes here.
    """
    def __init__(self, x, y, radius=8):
        """Create a Ball object.
        
        Args:
            x: an int, the initial x coordinate of the ball
            y: an int, the initial y coordinate of the ball
            radius: an optional int, the radius of the ball
        """
        self.x, self.y = x, y
        self.radius = radius
        self.x_velocity, self.y_velocity = 0, -5
        self.color = (255, 255, 64)

    def update(self):
        """Update the position of the ball."""
        self.x += self.x_velocity
        self.y += self.y_velocity

    def draw(self, pygame, screen):
        """Draw the ball on the screen.
        
        Args:
            pygame: the active pygame object
            screen: the active screen object
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
