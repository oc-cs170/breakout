#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from ball import Ball
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BORDER = 20


class Breakout(object):
    def __init__(self):
        # Initilaize pygame and the display/window
        pygame.mixer.pre_init(44100)
        pygame.init()
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # , pygame.FULLSCREEN)
        self.background = self.screen.copy()
        pygame.display.set_caption('Breakout')

        # Create the game objects
        self.scoreboard = Scoreboard(self.screen)
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.player = pygame.sprite.Group(self.paddle, self.ball)
        self.bricks = []
        for i in range(5):
            y = 100 + i * 25
            for j in range(10):
                x = 2 + j * 60
                self.bricks.append(Brick(x, y))
        self.level = pygame.sprite.Group(self.bricks)

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
        self.level.add(self.bricks)

    def new_round(self):
        """Start a new round in a Breakout game.

        Resets all round-level parameters, increments the round counter, and
        puts the ball on the paddle.
        """
        self.round += 1
        self.paddle.reset()
        self.ball.reset(self.paddle)

    def splash_screen(self):
        title = 'BREAKOUT'
        bg = (216, 216, 255)
        fg = (0, 128, 0)
        clock = pygame.time.Clock()

        # Build the splash screen
        splash = self.screen.copy()
        splash.fill((0, 0, 0))
        inner = (BORDER, BORDER, SCREEN_WIDTH - 2 * BORDER, SCREEN_HEIGHT - 2 * BORDER)
        splash.fill(bg, inner)

        # hide_screen = pygame.time.get_ticks()
        font1 = pygame.font.SysFont('Arial', 80, bold=True)
        antialias = True
        width, height = font1.size(title)
        x = (SCREEN_WIDTH - width) / 2
        y = 2 * BORDER

        for i in range(len(title)):
            clock.tick(4)
            self.screen.blit(splash, (0, 0))
            surf = font1.render(title[0:i + 1], antialias, fg, bg)
            self.screen.blit(surf, (x, y))
            pygame.display.flip()

        # clock.tick(1)
        font2 = pygame.font.SysFont('Arial', 24, bold=True)
        x *= 2
        y = y + height + BORDER
        lines = ['<-, ->: Move paddle',
                 'Space: Serve ball',
                 'Esc, Q: Quit game',
                 ' ',
                 ' ',
                 'Press any key to start...']
        for line in lines:
            clock.tick(10)
            surf = font2.render(line, antialias, fg, bg)
            self.screen.blit(surf, (x, y))
            y += surf.get_height()
            pygame.display.flip()

        waiting = True
        while waiting:           # Pause loop
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    if event.key == pygame.K_q:
                        self.game_over = True
                    break

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
        self.splash_screen()
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
            else:
                self.scoreboard.draw(self.screen)
                self.scoreboard.update()

                self.paddle.update()
                self.ball.update(self.paddle)

                self.player.clear(self.screen, self.background)
                self.player.draw(self.screen)

                self.level.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
