import pygame


class SplashScreen(object):
    def __init__(self, screen, border_width):
        self.screen = screen
        self.border = border_width
        self.screen_width, self.screen_height = screen.get_size()

    def show(self):
        title = 'BREAKOUT'
        bg = (216, 216, 255)
        fg = (0, 128, 0)
        clock = pygame.time.Clock()

        # Build the splash screen
        splash = self.screen.copy()
        splash.fill((0, 0, 0))
        inner = self.screen.get_rect().inflate(self.border, self.border)
        splash.fill(bg, inner)

        # hide_screen = pygame.time.get_ticks()
        font1 = pygame.font.SysFont('Arial', 80, bold=True)
        antialias = True
        width, height = font1.size(title)
        x = (self.screen_width - width) / 2
        y = 2 * self.border

        for i in range(len(title)):
            clock.tick(4)
            self.screen.blit(splash, (0, 0))
            surf = font1.render(title[0:i + 1], antialias, fg, bg)
            self.screen.blit(surf, (x, y))
            pygame.display.flip()

        # clock.tick(1)
        font2 = pygame.font.SysFont('Arial', 24, bold=True)
        x *= 2
        y = y + height + self.border
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

