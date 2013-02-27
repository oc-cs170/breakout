import pygame


class Paddle(pygame.sprite.Sprite):
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
        pygame.sprite.Sprite.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Size and location
        self.image = pygame.Surface((80, 16))
        self.rect = pygame.Rect((0, 0), self.image.get_size())
        pygame.draw.rect(self.image, pygame.Color(192, 192, 192), self.rect)

        # Velocity
        self.x_velocity = 0
        

    def reset(self):
        """Prepare the paddle for a new round.

        Does nothing...

        Args:
            none so far...
        """
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - (2 * self.rect.height)

    def update(self):
        """Update the position of the paddle.

        Should be called every frame, by the main game loop to allow the
        paddle to move.
        """
        self.rect.move_ip(self.x_velocity, 0)
        # Sets boundaries for paddle 
        self.rect.right = max(min(self.rect.right, self.screen_width), self.rect.width)
