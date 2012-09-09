class Paddle(object):
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = ((x + width) / 2, (y + height) / 2, width, height)
        self.x_velocity, self.y_velocity = 0, 0

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, (192, 192, 192), self.rect)
