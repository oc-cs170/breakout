#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from ball import Ball
from paddle import Paddle
from brick import Brick 

class Breakout(object):
    def __init__(self):
        # Initilaize pygame and the display/window
        pygame.init()
        self.screen_width, self.screen_height = 600, 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # , pygame.FULLSCREEN)
        pygame.display.set_caption('Breakout')

        # Create the game objects
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.brick = Brick(self.screen_width, self.screen_height)

        # Let's control the frame rate
        self.clock = pygame.time.Clock()

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        self.game_over = False
        self.round = 0
        # self.brick.reset()

        
        self.new_round()

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
        if self.round == 4:
            self.game_over = True

        # Draws the 50 bricks
        
                    # Frist Row
        self.bricks = [Brick(20,20), Brick(76, 20), Brick(132, 20), Brick(188, 20), Brick(244, 20), 
                    Brick(300, 20), Brick(356, 20), Brick(412, 20), Brick(468, 20), Brick(525, 20), 
                    # Second Row
                    Brick(20, 40), Brick(76, 40), Brick(132, 40), Brick(188, 40), Brick(244, 40), 
                    Brick(300, 40), Brick(356, 40), Brick(412, 40), Brick(468, 40), Brick(525, 40), 
                    # Third Row
                    Brick(20, 60), Brick(76, 60), Brick(132, 60), Brick(188, 60), Brick(244, 60), 
                    Brick(300, 60), Brick(356, 60), Brick(412, 60), Brick(468, 60), Brick(525, 60), 
                    # Fourth row
                    Brick(20, 80), Brick(76, 80), Brick(132, 80), Brick(188, 80), Brick(244, 80), 
                    Brick(300, 80), Brick(356, 80), Brick(412, 80), Brick(468, 80), Brick(525, 80),
                    # Fifth Row
                    Brick(20, 100), Brick(76, 100), Brick(132, 100), Brick(188, 100), Brick(244, 100), 
                    Brick(300, 100), Brick(356,100), Brick(412, 100), Brick(468, 100), Brick(525, 100),]

        print self.round

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.new_game()
        while not self.game_over:           # Game loop
            self.clock.tick(50)             # Frame rate control
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
                if self.ball.dead == True:
                    self.new_round()

                self.screen.fill((0, 0, 0))

                self.paddle.draw(self.screen)
                self.ball.draw(self.screen)
                

                for brick in self.bricks:
                    brick.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
