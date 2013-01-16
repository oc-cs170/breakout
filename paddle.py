import pygame


class Paddle(object):
    """A Paddle class that is aware of pygame.

    A small rectangular paddle to play Breakout.
    Coordinates are the center of the top edge of the paddle.
    """
    def __init__(self, screen_width, screen_height):
        """Create a Paddle object.

        Args:
            screen_width: an int, the width of the screen
            screen_height: an int, the height of the screen
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

    def hit_ball(self, ball_x, x_velocity, y_velocity):
        """Test for ball contact and reflect if necessary.

        Args:
            ball_x: an int, the horizontal location of the ball center
            x_velocity: an int, the horizontal velocity of the ball
            y_velocity: an int, the vertical velocity of the ball
        """
        if y_velocity < 0 or ball_x < self.rect[0] or ball_x > self.rect[0] + self.rect[2]:
            return x_velocity, y_velocity

        return x_velocity, -y_velocity

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
        # Keep the paddle on the screen stopping it at the edges
        if self.rect[0] <= 0:
            self.x = self.width / 2 + 1
            self.x_velocity = 0
        elif self.rect[0] + self.rect[2] >= self.screen_width:
            self.x = self.screen_width - self.width / 2 - 1
            self.x_velocity = 0
        else:
            self.x += self.x_velocity

        self.rect = (self.x - self.width / 2, self.y, self.width, self.height)
