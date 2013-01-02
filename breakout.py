#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from Ball import Ball
from Paddle import Paddle


class Breakout(object):
    def __init__(self):
        # Initilaize pygame and the display/window
        pygame.init()
        self.screen_size = self.screen_width, self.screen_height = 600, 800
        self.screen = pygame.display.set_mode(self.screen_size)  # , pygame.FULLSCREEN)
        pygame.display.set_caption('Breakout')

        # Create the game objects
        self.paddle = Paddle(self.screen_size)
        self.ball = Ball(self.screen_size)

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        self.game_over = False
        self.round = 0

        self.new_round()

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """
        self.round += 1
        self.paddle.reset()
        self.ball.reset(self.paddle)

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.new_game()
        while not self.game_over:           # Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.serve()
                    if event.key == pygame.K_LEFT:
                        self.paddle.x_velocity = -4
                    elif event.key == pygame.K_RIGHT:
                        self.paddle.x_velocity = 4

                    # This starts a new round, it's only here for debugging purposes
                    if event.key == pygame.K_r:
                        self.new_round()
                    # This starts a new game, it's only here for debugging purposes
                    if event.key == pygame.K_g:
                        self.new_game()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.paddle.x_velocity < 0:
                        self.paddle.x_velocity = 0
                    if event.key == pygame.K_RIGHT and self.paddle.x_velocity > 0:
                        self.paddle.x_velocity = 0
            else:
                self.paddle.update()
                self.ball.update(self.paddle)

                self.screen.fill((0, 0, 0))
                self.paddle.draw(self.screen)
                self.ball.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
