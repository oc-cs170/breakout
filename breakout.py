#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from ball import Ball
from paddle import Paddle
from brick import Brick 
from scoreboard import ScoreBoard
from splashscreen import SplashScreen

WINDOW_TITLE = "Breakout"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700


class Breakout(object):
    def __init__(self):
        # Initilaize pygame and the display/window
        pygame.mixer.pre_init(frequency=11025)
        pygame.init()
        self.screen_width, self.screen_height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = self.screen.copy()
        pygame.display.set_caption(WINDOW_TITLE)

        # self.font = pygame.font.SysFont("monospace", 15)

        # Create the game objects
        self.scoreboard = ScoreBoard(self.screen)
        self.splashscreen = SplashScreen()
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.brick = Brick(self.screen_width, self.screen_height)
        self.player = pygame.sprite.Group(self.paddle, self.ball)
        
        # Creats the 50 bircks in a sprite group
        self.bricks = pygame.sprite.Group()
        for i in range(5):
            y = 100 + (i * 25)
            for j in range(10):
                x = 2 + (j * 60)
                self.bricks.add(Brick(x, y))
        
        # self.level = pygame.sprite.Group(self.bricks)
        self.bm = pygame.sprite.Group(self.ball)

        # Let's control the frame rate
        self.clock = pygame.time.Clock()

        self.transform = pygame.mixer.Sound('Transform.wav')

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        self.game_over = False
        self.round = 0

        # Clears the screen
        self.screen.blit(self.background, (0, 0))
      
        # self.new_level(0)
        self.new_round()

    # def new_level(self, level):
    #     self.level.add(self.bricks)

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """
        self.round += 1
        self.paddle.reset()
        self.ball.reset(self.paddle)

        if self.round < 3:
            self.game_over = False
            self.level = self.bricks.copy()
            self.level.draw(self.screen)
        # if self.round == 4:
        #     self.game_over = True

        print self.round

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.splashscreen.draw()
        self.new_game()
        while not self.game_over:           # Game loop
            self.clock.tick(50)            # Frame rate control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.transform.play()
                        self.ball.serve()
                    if event.key == pygame.K_LEFT:
                        self.paddle.velocity = -4
                    elif event.key == pygame.K_RIGHT:
                        self.paddle.velocity = 4

                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        self.game_over = True

                    # This starts a new round, it's only here for debugging purposes
                    if event.key == pygame.K_r:
                        self.new_round()
                    # This starts a new game, it's only here for debugging purposes
                    if event.key == pygame.K_g:
                        self.new_game()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.paddle.velocity < 0:
                        self.paddle.velocity = 0
                    if event.key == pygame.K_RIGHT and self.paddle.velocity > 0:
                        self.paddle.velocity = 0
            else:
                # Do the scoreboard
                self.scoreboard.update()
                self.scoreboard.draw(self.screen)

                # Where is the ball?
                bx, by = self.ball.rect.center

                # Handle ball/brick(s) collisions
                # hits is a dict if brick(s) is(are) hit
                # {self.ball: [brick_a, brick_b]}
                hits = pygame.sprite.groupcollide(self.bm, self.level, False, True)
                if hits:
                    bricks = hits[self.ball]
                    print len(bricks), 'hits(s)'
                    # Clear all bricks, then redraw those not killed
                    self.level.clear(self.screen, self.background)
                    self.level.draw(self.screen)

                    # Do ball (off brick) reflection here
                    hit_brick = bricks[0] # ignoring multi brick hits for now
                    if by < hit_brick.rect.bottom or by > hit_brick.rect.top:
                        self.ball.y_velocity = -self.ball.y_velocity
                    if bx < hit_brick.rect.left or bx > hit_brick.rect.right:
                        self.ball.x_velocity = -self.ball.x_velocity

                # Handle ball/paddle collisions
                # Do ball (off paddle) reflection here
                if by < self.paddle.rect.top:
                    if pygame.sprite.collide_rect(self.ball, self.paddle):
                        self.ball.y_velocity = -self.ball.y_velocity
                if self.ball.rect.top >= self.screen_height:
                    self.ball.dead = True
                    # self.scoreboard.update()
                    print 'Dead ball!!'

                # Dead ball, lock it to the paddle
                if not self.ball.moving:
                    self.ball.rect.midbottom = self.paddle.rect.midtop

                # Affter everything, update and redraw the ball and paddle
                self.player.clear(self.screen, self.background)
                self.player.update()
                self.player.draw(self.screen)

                if self.ball.dead == True:
                    self.new_round()
                if self.round == 4:
                    self.splashscreen.game_over()
                    self.new_game()

                # self.screen.fill((0, 0, 0))
                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
