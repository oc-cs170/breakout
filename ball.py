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
        super(Ball, self).__init__()

        # Creation parameters
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Get art, set initial position and velocity
        self.image = pygame.image.load('images/ballBlue16.png').convert_alpha()
        self.rect = self.image.get_rect(center=(0, 0))
        self.x_velocity, self.y_velocity = 0, 0
        self.moving = False

        # Load sound(s)
        self.wall_sound = pygame.mixer.Sound('sounds/transform.wav')

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
            r = self.rect.move(self.x_velocity, self.y_velocity)
            if r.left <= 0 or r.right >= self.screen_width:
                self.x_velocity *= -1
                self.wall_sound.play()
            if r.top <= 22 or r.bottom >= self.screen_height:
                self.y_velocity *= -1
                self.wall_sound.play()
            self.rect = r
        else:
            self.rect.midbottom = paddle.rect.midtop
