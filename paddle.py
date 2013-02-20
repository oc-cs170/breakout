import pygame

PADDLE_WIDTH = 80
PADDLE_HEIGHT = 16


class Paddle(pygame.sprite.Sprite):
    """A Paddle class that is aware of pygame.

    A small rectangular paddle to play Breakout.
    Coordinates are the center of the top edge of the paddle.
    """
    def __init__(self, screen_width, screen_height):
        """Create a Paddle object.

        Args:
            screen_width: an int, the width of the game screen
            screen_height: an int, the height of the game screen
        """
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)

        # Creation parameter
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Size and location
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill((255, 0, 0))
        self.image.fill((192, 192, 192),
                        (1, 1, PADDLE_WIDTH - 2, PADDLE_HEIGHT - 2))

        paddlex = screen_width / 2
        paddley = screen_height - (2 * PADDLE_HEIGHT)
        self.rect = self.image.get_rect(midtop=(paddlex, paddley))

        # Velocity
        self.velocity = 0

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
        self.rect.move_ip(self.velocity, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
