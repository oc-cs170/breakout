import pygame


class Brick(object):
	
	def __init__(self, screen_width, screen_height, x, y):
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.width, self.height = 60, 42
		
		self.x = x
		self.y = y
		
		self.rect = (self.x, self.y, self.width, self.height)
		
		self.color = 255, 0, 0
		
		
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect, 1)
		