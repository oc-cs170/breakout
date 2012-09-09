#! /usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules."""

import pygame
import random

from Ball import Ball
from Paddle import Paddle

class Breakout(object):
    def __init__(self):
        # Initilaize pygame and the display/window
        pygame.init()
        self.width, self.height = 600, 800
        self.screen = pygame.display.set_mode((self.width, self.height)) #, pygame.FULLSCREEN)
        pygame.display.set_caption('Breakout')
        # background = pygame.image.load("PiInvaders/background.png").convert();

        # Create the game objects
        self.ball = Ball(self.width / 2, self.height - 32)
        self.paddle = Paddle(self.width / 2, self.height - 16, 80, 16)

    def new_game(self):
        """Start a new game of Breakout

        Resets all game level parameters, and starts a new round."""
        self.game_over = False
        self.round = 0

        self.new_round()

    def new_round(self):
        """Start a new round in a Breakout game

        Resets all round level parameters, increments the round counter, and
        puts the ball on the paddle, centering both."""
        self.round += 1
        self.ball_is_moving = False
        self.ball.x_velocity = random.randint(-3, 3)
        self.paddle.x = self.width / 2
        self.ball.y = self.height - 32

    def play(self):
        """Start Breakout game

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects."""
        self.new_game()
        while not self.game_over:           # Game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                    self.game_over = True
                    break
                if event.type == pygame.KEYDOWN:
                    if not self.ball_is_moving and event.key == pygame.K_SPACE:
                        self.ball_is_moving = True
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
                if self.ball_is_moving:
                    self.ball.update()
                else:
                    self.ball.x = self.paddle.x

                self.screen.fill((0, 0, 0))
                self.paddle.draw(pygame, self.screen)
                self.ball.draw(pygame, self.screen)
                
                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()

