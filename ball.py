import random
import pygame


class Ball(object):
    """A Ball class that is aware of pygame.

    A small round ball to play Breakout.
    Coordinates are the center of the ball.
    """
    def __init__(self, screen_width, screen_height, radius=8):
        """Create a Ball object.

        Args:
            screen_width: an int, the width of the game screen
            screen_height: an int, the height of the game screen
            radius: an int (optional), the radius of the ball
        """
        # Creation parameters
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = radius

        # Initial position and velocity
        self.x, self.y = 0, 0
        self.x_velocity, self.y_velocity = 0, 0
        self.moving = False

        self.color = 255, 255, 64

    def draw(self, screen):
        """Draw the ball on the screen.

        Args:
            screen: the active screen object
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def reset(self, paddle):
        """Prepare the ball for a new round.

        Attach the ball to the center of the paddle, and give it a random
        upwards velocity vector.

        Args:
            paddle: the game's paddle object
        """
        self.x_velocity = random.randint(-3, 3)
        self.y_velocity = -5
        self.x = paddle.x
        self.y = paddle.y - self.radius
        self.rect = (self.x - self.radius, self.y - self.radius, self.radius, self.radius)
        self.moving = False

    def serve(self):
        """Set the ball in motion."""
        self.moving = True

    def update(self, paddle):
        """Update the position of the ball.

        Args:
            paddle: the game's paddle object
        """
        if self.moving:
            # Check if ball has hit horizontal edge
            if self.x + self.radius > self.screen_width:
                self.x_velocity = -self.x_velocity
            elif self.x < self.radius:
                self.x_velocity = -self.x_velocity

            # Check if ball has hit top
            if self.y < self.radius:
                self.y_velocity = -self.y_velocity

            # Check if ball has hit bottom
            if self.y >= self.screen_height - self.radius:
                self.y_velocity = 0
                return False

            # Check if ball has hit paddle
            if self.y + self.radius > paddle.y:
                self.x_velocity, self.y_velocity = paddle.hit_ball(self.x, self.x_velocity, self.y_velocity)

            self.x += self.x_velocity
            self.y += self.y_velocity
        else:
            self.x = paddle.x
        self.rect = (self.x - self.radius, self.y - self.radius, self.radius, self.radius)

        return True
