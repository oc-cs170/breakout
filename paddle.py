import pygame


class Paddle(object):
    """A Paddle class that is aware of pygame.

    A small rectangular paddle to play Breakout.
    Coordinates are the center of the top edge of the paddle.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        """Create a Paddle object.

        Args:
            screen_size: an int 2-tuple of screen width and height
        """
        # Creation parameter
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        # Size and location
        self.width, self.height = 80, 16
        self.x, self.y = self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT - (2 * self.height)
        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)

        # Velocity
        self.x_velocity = 0

        self.color = 169, 169, 169

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
        
        # When paddle makes contact with right side of screen, paddle stops and stays on screen
        if self.x + (self.width / 2) >= self.WINDOW_WIDTH:
            self.x_velocity = 0
            self.x = (self.WINDOW_WIDTH - 1) - (self.width / 2)

        # When paddle makes contact with left side of screen, paddle stops and stays on screen
        if self.x - (self.width / 2) <= 0:
            self.x_velocity = 0
            self.x = 1 + (self.width / 2)

        # Allows movement of paddle
        self.x += self.x_velocity
        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)











