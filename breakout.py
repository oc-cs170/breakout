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
		self.screen_width, self.screen_height = 600, 800
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # , pygame.FULLSCREEN)
		pygame.display.set_caption('Breakout')
		
		# Create the game objects
		self.paddle = Paddle(self.screen_width, self.screen_height)
		self.ball = Ball(self.screen_width, self.screen_height)
		self.bricks = list()
		for i in range(0,600,60):
			for j in range(42, 211, 42):
				self.bricks.append(Brick(self.screen_width, self.screen_height, i, j))

		# Let's control the frame rate
		self.clock = pygame.time.Clock()

	def new_game(self):
		"""Start a new game of Breakout.

		Resets all game-level parameters, and starts a new round.
		"""
		self.game_over = False
		self.round = 0
		self.paddle.reset()

		self.new_round()

	def new_round(self):
		"""Start a new round in a Breakout game.

		Resets all round-level parameters, increments the round counter, and
		puts the ball on the paddle.
		"""
		self.round += 1
		self.ball.reset(self.paddle)

	def play(self):
		"""Start Breakout program.

		New game is started and game loop is entered.
		The game loop checks for events, updates all objects, and then
		draws all the objects.
		"""
		self.new_game()
		while not self.game_over:           # Game loop
			self.clock.tick(50)             # Frame rate control
			font = pygame.font.SysFont("monospace", 15)
			round_counter = font.render("Round " + str(self.round), 2, (255,255,0))
		
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
				contact = self.ball.update(self.paddle, self.bricks)
				for brick in self.bricks:
					if contact == brick:
						self.bricks.remove(brick)
					

				self.screen.fill((0, 0, 0))
				self.screen.blit(round_counter, (0, 0))
				ball_loc = font.render(str(self.ball.x) + "," + str(self.ball.y), 2, (255,255,0))
				self.screen.blit(ball_loc, (0, 14))
				self.paddle.draw(self.screen)
				self.ball.draw(self.screen)
				pygame.display.flip()
		
		
				for brick in self.bricks:
					brick.draw(self.screen)
				
				pygame.display.flip()
					
				if self.ball.y >= self.screen_height - self.ball.radius:
					self.new_round()
				if self.round > 3:
					self.new_game()
		

		pygame.quit()

if __name__ == '__main__':
	game = Breakout()
	game.play()
