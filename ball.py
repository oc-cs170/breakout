import random
import pygame


class Ball(pygame.sprite.Sprite):
    """A Ball class that is aware of pygame.

    A small round ball to play Breakout.
    Coordinates are the center of the ball.
    """
    def __init__(self, screen_width, screen_height, radius=8):
        """Create a Ball object.

        Args:
            screen_width: an int, the width of the game screen
            screen_height: an int, the height of the game screen
            radius: an optional int, the radius of the ball
        """
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)

        # Creation parameters
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Create visualization
        self.color = 255, 255, 64
        self.image = pygame.Surface((2 * radius, 2 * radius))
        self.image.fill((1, 2, 3))  # A "Fake" black
        self.image.set_colorkey((1, 2, 3))
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

        # Initial position and velocity
        self.rect = self.image.get_rect(center=(0, 0))
        self.x_velocity, self.y_velocity = 0, 0
        self.moving = False

        # Load sound(s)
        self.wall_sound = pygame.mixer.Sound('click.wav')

    def reset(self, paddle):
        """Prepare the ball for a new round.

        Attach the ball to the center of the paddle, and give it a random
        upwards velocity vector.

        Args:
            paddle: the game's paddle object
        """
        # Stop the ball
        self.moving = False

        # Create a random upwards velocity...
        # Vx in [-3, -2, -1, 1, 2, 3]
        # Vy = -5
        self.x_velocity = random.randint(-3, 2)
        if self.x_velocity >= 0:
            self.x_velocity += 1
        self.y_velocity = -5

    def serve(self):
        """Set the ball in motion."""
        self.moving = True

    def update(self, paddle):
        """Update the position of the ball.

        Args:
            paddle: the game's paddle object
        """
        if self.moving:
            self.rect.move_ip(self.x_velocity, self.y_velocity)
            if self.rect.left <= 0 or self.rect.right >= self.screen_width:
                self.x_velocity *= -1
                self.wall_sound.play()
            if self.rect.top <= 0:
                self.y_velocity *= -1
                self.wall_sound.play()
        else:
            self.rect.midbottom = paddle.rect.midtop
