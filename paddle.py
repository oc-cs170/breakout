import pygame


class Paddle(object):
    """A Paddle class that is aware of pygame.

    A small rectangular paddle to play Breakout.
    Coordinates are the center of the top edge of the paddle.
    """
    def __init__(self, screen_width, screen_height):
        """Create a Paddle object.

        Args:
            screen_size: an int 2-tuple of screen width and height
        """
        # Creation parameter
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Size and location
        self.width, self.height = 80, 16
        self.x, self.y = self.screen_width / 2, self.screen_height - (2 * self.height)
        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)

        # Velocity
        self.x_velocity = 0

        self.color = 192, 192, 192

    def draw(self, screen):
        """Draw the paddle on the screen.

        Args:
            screen: the active screen object
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def reset(self):
        """Prepare the paddle for a new round.

        Does nothing...

        Args:
            none so far...
        """
        pass

    def update(self):
        """Update the position of the paddle.

        Should be called every frame, by the main game loop to allow the
        paddle to move.
        """
        
       
        if self.x > 560:
            self.x = 560
        if self.x < 40:
            self.x = 40
        self.x += self.x_velocity
        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)
