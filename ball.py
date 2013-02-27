import random
import pygame

class Ball(pygame.sprite.Sprite):
    """A Ball class that is aware of pygame.

    A small round ball to play Breakout.
    Coordinates are the center of the ball.
    """

    def __init__(self, screen_width, screen_height, paddle, radius=8):
        """Create a Ball object.

        Args:
            screen_width: an int, the width of the game screen
            screen_height: an int, the height of the game screen
            radius: an optional int, the radius of the ball
        """
        # Creation parameters
        pygame.sprite.Sprite.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.paddle = paddle

        # Initial position and velocity
        self.x_velocity, self.y_velocity = 0, -5
        self.moving = False

        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        pygame.draw.circle(self.image, pygame.Color(255, 255, 64), (self.radius, self.radius), self.radius)
        self.image.set_colorkey(pygame.Color('black'))
        self.rect = pygame.Rect((0, 0), self.image.get_size())

    def reset(self):
        """Prepare the ball for a new round.

        Attach the ball to the center of the paddle, and give it a random
        upwards velocity vector.

        Args:
            paddle: the game's paddle object
        """
        self.x_velocity = random.randint(-3,3)
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top
        self.moving = False

    def serve(self):
        """Set the ball in motion."""
        self.moving = True

    def update(self, brick=None):
        """Update the position of the ball.

        Args:
            paddle: the game's paddle object
        """

        if self.moving:

            # if sides are hit
            if self.rect.right >= self.screen_width or self.rect.left < 0:
                self.x_velocity = -self.x_velocity

            # if the top of display is hit
            if self.rect.top <= 0:
                self.y_velocity = -self.y_velocity

            # if paddle is hit
            if (self.rect.bottom > self.paddle.rect.top) and (self.paddle.rect.left < self.rect.centerx < self.paddle.rect.right):
                self.y_velocity = -self.y_velocity
                self.x_velocity += (self.rect.centerx - self.paddle.rect.centerx)/8

            # if a brick is hit
            if brick:
                brick = brick[0] 

                # if side is hit, bounce horizontally otherwise bounce vertically
                if brick.rect.top <= self.rect.centery <= brick.rect.bottom:
                    self.x_velocity = -self.x_velocity
                else:
                    self.y_velocity = -self.y_velocity

            # sets a max to horizontal speed
            self.x_velocity = min(self.x_velocity, 10)
            self.rect.move_ip(self.x_velocity, self.y_velocity)

        # if it's not moving about, put it on the paddle
        else:
            self.rect.centerx = self.paddle.rect.centerx
