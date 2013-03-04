import random
import pygame


class Ball(pygame.sprite.Sprite):
    """A Ball class that is aware of pygame.

    A small round ball to play Breakout.
    Coordinates are the center of the ball.
    """
    def __init__(self, screen_width, screen_height, radius = 8):
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
        self.radius = radius

        self.color = 255, 255, 64
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius))
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.image.set_colorkey(pygame.Color('black'))
        # Initial position and velocity
        self.rect = self.image.get_rect(center=(0, 0))
        self.x_velocity, self.y_velocity = 0, 0
        self.moving = False

    def reset(self, paddle):
        """Prepare the ball for a new round.

        Attach the ball to the center of the paddle, and give it a random
        upwards velocity vector.

        Args:
            paddle: the game's paddle object
        """
        # Stop the ball
        self.moving = False

        # Creates a random upwards velocity
        self.x_velocity = random.randint(-3, 2)
        if self.x_velocity >= 0:
            self.x_velocity += 1
        self.y_velocity = -5

        self.rect.midbottom = paddle.rect.midtop
        self.moving = False
        self.dead = False

    def serve(self):
        """Set the ball in motion."""
        self.moving = True

    def update(self, paddle, bricks):
        """Update the position of the ball.

        Args:
            paddle: the game's paddle object
        """

        # If we are moving then the game is being played. Otherwise stay stuck to the paddle
        if self.moving:
            self.rect.move_ip(self.x_velocity, self.y_velocity)
            # When ball rect makes contact with left or right of screen.
            if self.rect.left <= 0 or self.rect.right >= self.screen_width:
                self.x_velocity = -self.x_velocity
            # When ball rect makes contact with top of screen
            if self.rect.top <= 0:
                self.y_velocity *= -1
        else:
            self.rect.midbottom = paddle.rect.midtop

        # When the ball has passed the paddle and has made contact with bottom of screen, ball is now dead
        if self.rect.top >= self.screen_height:
            self.dead = True

        # When the ball makes contact with the paddle, y velocity is changed back to original speed of -5
        if pygame.sprite.collide_rect(self, paddle):
            self.y_velocity = -abs(self.y_velocity)

        # for brick in bricks:
        # When the ball makes contact with a brick, y velocity is changed to opposite its original
        # if pygame.sprite.spritecollide(self, bricks, True):
        #     self.y_velocity = -self.y_velocity

        if pygame.sprite.spritecollideany(self, bricks):
            self.y_velocity = -self.y_velocity
            # pygame.sprite.remove(bricks)
            
        
        #     # Top of ball hits bottom of brick and center of ball is less than bottom of brick
        #     if self.y - self.radius <= brick.y + brick.height and self.y >= brick.y + brick.height : 
        #         if self.x <= brick.x + (brick.width / 2):
        #             if self.x >= brick.x - (brick.width / 2):
        #                 self.y_velocity = -self.y_velocity
        #                 return brick
        
        #     # Bottom of ball hits top of brick and center of ball is greater than top of brick
        #     if self.y + self.radius >= brick.y and self.y <= brick.y + brick.height:
        #         if self.x <= brick.x + (brick.width / 2):
        #             if self.x >= brick.x - (brick.width / 2):
        #                 self.y_velocity = -abs(self.y_velocity)
        #                 return brick

        #     # left side of the ball hits right side of brick
        #     if self.x - self.radius <= brick.x + brick.width and self.x >= brick.x + brick.width:
        #         if self.y <= brick.y + (brick.height / 2):
        #             if self.y >= brick.y - (brick.height / 2):
        #                 self.x_velocity = -self.x_velocity
        #                 return brick

        #     # # right side of the ball hits the left side of the brick
        #     if self.x + self.radius >= brick.x and self.x <= brick.x:
        #         if self.y <= brick.y + (brick.height / 2):
        #             if self.y >= brick.y - (brick.height / 2):
        #                 self.x_velocity = -self.x_velocity
        #                 return brick

