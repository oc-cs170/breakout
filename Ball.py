class Ball(object):
    def __init__(self, x, y, radius=8):
        self.x, self.y = x, y
        self.radius = radius
        self.x_velocity, self.y_velocity = 0, -5
        self.color = (255, 255, 64)

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
