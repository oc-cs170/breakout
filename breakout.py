#!/usr/bin/env python
"""Main file with game loop for Breakout

Uses Ball and Paddle from external modules.
"""

import pygame

from ball import Ball
from paddle import Paddle
from brick import Brick 

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
        self.paddle = Paddle(self.screen_width, self.screen_height)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.brick = Brick(self.screen_width, self.screen_height)
        self.player = pygame.sprite.Group(self.paddle, self.ball)
        # Creats the 50 bircks in a sprite group
        self.bricks = []
        for i in range(5):
            y = 100 + (i * 25)
            for j in range(10):
                x = 2 + (j * 60)
                self.bricks.append(Brick(x, y))
        self.level = pygame.sprite.Group(self.bricks)

        # Let's control the frame rate
        self.clock = pygame.time.Clock()

        self.transform = pygame.mixer.Sound('Transform.wav')

    def game_sounds(self, loop=0):
        pass

    # def title_screen(self):
    #     end = self.font.render("START GAME", 2, (255, 255, 0))
    #     self.screen.blit(end, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    #     pygame.display.flip()
    #     pygame.time.wait(3000)
        
    #     # self.new_game()

    def new_game(self):
        """Start a new game of Breakout.

        Resets all game-level parameters, and starts a new round.
        """
        self.game_over = False
        self.round = 0

        # Clears the screen
        self.screen.blit(self.background, (0, 0))
      
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

        

        print self.round

    def play(self):
        """Start Breakout program.

        New game is started and game loop is entered.
        The game loop checks for events, updates all objects, and then
        draws all the objects.
        """
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
                self.paddle.update()
                self.ball.update(self.paddle)

                self.player.clear(self.screen, self.background)
                self.player.draw(self.screen)
                
                if self.ball.dead == True:
                    self.new_round()

                # self.screen.fill((0, 0, 0))

                # self.paddle.draw(self.screen)
                # self.ball.draw(self.screen)
                

                # if (pygame.time.get_ticks() - self.now) >= 0:
                #     self.title_screen()
                self.level.draw(self.screen)

                pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Breakout()
    game.play()
