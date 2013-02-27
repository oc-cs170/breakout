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
        pygame.mixer.pre_init(44100)
        pygame.init()
        self.screen_width, self.screen_height = 600, 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Breakout')

        # Create the game objects
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.paddle_sprite = pygame.sprite.GroupSingle(self.paddle)
        self.ball = Ball(self.screen_width, self.screen_height, paddle=self.paddle)
        self.ball_sprite = pygame.sprite.GroupSingle(self.ball)

        # Let's control the frame rate
        self.clock = pygame.time.Clock()

        # Load sounds
        self.sound = pygame.mixer.Sound('Radioactive Field 01.wav')

        # Load font
        self.font = pygame.font.SysFont("monospace", 15)

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        splash = pygame.Surface((self.screen_width, self.screen_height))
        hello = self.font.render("Welcome to Breakout", 2, (255,255,0))
        splash.fill((0, 0, 0))
        splash.blit(hello, (0, 0))
        self.screen.blit(splash, (0, 0))
        pygame.display.flip()

        pygame.time.wait(1)

        self.game_over = False
        self.round = 0
        self.points = 0

        self.bricks = pygame.sprite.Group()
        for i in range(0,600,60):
            for j in range(42, 211, 42):
                brick = Brick(i, j)
                self.bricks.add(brick)

        self.paddle.reset()
        self.new_round()

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """

        self.round += 1
        self.ball.reset()

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.new_game()
        while not self.game_over:           # Game loop
            self.clock.tick(50)             # Frame rate control
            round_counter = self.font.render("Round " + str(self.round), 2, (255,255,0))

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

                    if event.key == pygame.K_a:
                        self.ball.x_velocity = -3
                    elif event.key == pygame.K_d:
                        self.ball.x_velocity = 3
                    elif event.key == pygame.K_w:
                        self.ball.y_velocity = -5
                    elif event.key == pygame.K_s:
                        self.ball.y_velocity = 5

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

            contact = pygame.sprite.spritecollide(self.ball, self.bricks, True,
                                                  pygame.sprite.collide_mask)

            self.paddle.update()
            self.ball.update(contact)

            if contact:
                self.points += 100


            # Draw onscreen text
            self.screen.fill((0, 0, 0))
            self.screen.blit(round_counter, (0, 0))
            ball_loc = self.font.render(str(self.ball.rect.centerx) + "," + str(self.ball.rect.centery), 2, (255,255,0))
            self.screen.blit(ball_loc, (0, 14))
            score = self.font.render("Score: " + str(self.points), 2, (255,255,0))
            self.screen.blit(score, (0, 28))

            # Draw onscreen objects
            self.paddle_sprite.draw(self.screen)
            self.ball_sprite.draw(self.screen)
            self.bricks.draw(self.screen)


            pygame.display.flip()
                
            if self.ball.rect.bottom >= self.screen_height:
                self.new_round()
            if self.round > 3:
                self.new_game()


        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
