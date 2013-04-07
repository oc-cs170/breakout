#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from ball import Ball
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard
from splashscreen import SplashScreen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BORDER = 20


class Breakout(object):
    def __init__(self):
        # Initialize mixer for sound
        pygame.mixer.init(44100)
        pygame.mixer.set_num_channels(4)

        # Initilaize pygame and the display/window
        pygame.init()
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # , pygame.FULLSCREEN)
        self.background = self.screen.copy()
        # self.background.fill((100, 100, 100))
        pygame.display.set_caption('Breakout')

        # Create the game objects
        self.splashscreen = SplashScreen(self.screen, BORDER)
        self.scoreboard = Scoreboard(self.screen)
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.player = pygame.sprite.RenderUpdates(self.paddle, self.ball)

        # Create all bricks and add a brick group
        self.bricks = pygame.sprite.Group()
        colors = ['red', 'yellow', 'green', 'blue', 'purple', 'grey']
        for i, color in enumerate(colors):
            y = 100 + i * 34
            for j in range(10):
                x = 1 + j * 60
                self.bricks.add(Brick(x, y, color))

        # Let's control the frame rate
        self.clock = pygame.time.Clock()

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        self.game_over = False
        self.round = 0

        # Clear the screen
        self.screen.blit(self.background, (0, 0))

        self.new_level(0)
        self.new_round()

    def new_level(self, level):
        self.level = self.bricks.copy()
        self.level.draw(self.screen)

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """
        self.round += 1
        self.paddle.reset()
        self.ball.reset(self.paddle)
        updated_rects = self.player.draw(self.screen)
        pygame.display.update(updated_rects)

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.splashscreen.show()
        self.new_game()
        while not self.game_over:           # Game loop
            self.clock.tick(50)             # Frame rate control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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
                    # This adds points, it's only here for debugging purposes
                    if event.key == pygame.K_p:
                        pass
                    # This adds levels, it's only here for debugging purposes
                    if event.key == pygame.K_l:
                        pass
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.paddle.velocity < 0:
                        self.paddle.velocity = 0
                    if event.key == pygame.K_RIGHT and self.paddle.velocity > 0:
                        self.paddle.velocity = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.ball.rect.center = event.pos
            else:
                self.scoreboard.update()
                # self.scoreboard.draw(self.screen)

                hits = pygame.sprite.spritecollide(self.ball, self.level, True)
                for brick in hits:
                    self.ball.brick_reflect(brick)
                    brick.clear(self.screen, self.background)

                self.player.clear(self.screen, self.background)
                self.player.update()
                updated_rects = self.player.draw(self.screen)
                pygame.display.update(updated_rects)

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
