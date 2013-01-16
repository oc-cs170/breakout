import pygame


class Brick(object):
    """A Brick class that is aware of pygame.

    A small rectangular brick to play Breakout.
    Coordinates are the center of the paddle.
    """
    def __init__(self, x, y, width=50, height=16, color=None):
        """Create a Brick object.

        Args:
            x: an int, the horizontal location of the brick
            y: an int, the vertical location of the brick
            width: an int, the width of the brick
            height: an int, the height of the brick
        """
        # Creation parameters
        self.rect = (x - width / 2, y - height / 2, width, height)

        if color:
            self.color = color
        else:
            self.color = 192, 255, 255

        self.visible = True

    def draw(self, screen):
        """Draw the brick on the screen.

        Args:
            screen: the active screen object
        """
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)

    def hit_ball(self, ball):
        """Test for ball contact and reflect if necessary.

        Args:
            ball: an int, the horizontal location of the ball center
            x_velocity: an int, the horizontal velocity of the ball
            y_velocity: an int, the vertical velocity of the ball
        """
        if not self.visible:
            return

        if ball.rect[1] < self.rect[1] + self.rect[3] and \
           ball.rect[1] > self.rect[1]:
            if ball.rect[0] < self.rect[0] + self.rect[2] and \
               ball.rect[0] > self.rect[0]:
                self.visible = False
                ball.y_velocity = -ball.y_velocity
