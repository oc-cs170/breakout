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
            radius: an optional int, the radius of the ball
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
        self.x_velocity = random.randint(-3,3)
        self.y_velocity = -5
        self.x = paddle.x
        self.y = paddle.y - self.radius
        self.moving = False

    def serve(self):
        """Set the ball in motion."""
        self.moving = True

    def update(self, paddle, bricks):
        """Update the position of the ball.

        Args:
            paddle: the game's paddle object
        """

        
        if self.moving:
            # if sides are hit
            self.x += self.x_velocity
            if self.x >= self.screen_width - self.radius or self.x <= self.radius:
                self.x_velocity = -self.x_velocity
            
            # if the top of display is hit
            self.y += self.y_velocity
            if self.y <= self.radius:
                self.y_velocity = -self.y_velocity

            # if paddle is hit
            if (self.y + self.radius >= paddle.y and paddle.x - paddle.width / 2 <= self.x <= paddle.x + paddle.width / 2):
                self.y_velocity = -self.y_velocity
                # Make another check to adjust x_velocity
                # Hit left half of paddle from left
                if (self.x_velocity >= 0 and self.x < paddle.x):
                    delta = (paddle.x - self.x) / 5
                    self.x_velocity = max(-5, self.x_velocity - delta)

                # Hit right half of paddle from right
                if (self.x_velocity <= 0 and self.x > paddle.x):
                    delta = (self.x - paddle.x) / 5
                    self.x_velocity = min(5, self.x_velocity + delta)


            # if a brick is hit
            for brick in bricks:
                # top side of ball makes contact
                if (self.y-self.radius) - (brick.y+brick.height) <= 0 and (self.y-self.radius) - (brick.y+brick.height) >= -self.radius:
                    if brick.x <= self.x and self.x <= brick.x+brick.width:
                        self.y_velocity = -self.y_velocity
                        return brick
                        
                # bottom side of ball makes contact
                elif self.radius >= (self.y+self.radius) - brick.y and (self.y+self.radius) - brick.y >= 0:
                    if brick.x <= self.x and self.x <= brick.x+brick.width:
                        self.y_velocity = -self.y_velocity
                        return brick
                        
                # if right side makes contact
                if self.radius >= (self.x+self.radius) - brick.x and (self.x+self.radius) - brick.x >= 0:
                    if brick.y <= self.y and self.y <= brick.y+brick.height:
                        self.x_velocity = -self.x_velocity
                        return brick
                        
                # if left side makes contact
                elif -self.radius <= (self.x-self.radius) - (brick.x+brick.width) and (self.x-self.radius) - (brick.x+brick.width) <= 0:
                    if brick.y <= self.y and self.y <= brick.y+brick.height:
                        self.x_velocity = -self.x_velocity
                        return brick
                    
                        
                    
            
        else:
            self.x = paddle.x









