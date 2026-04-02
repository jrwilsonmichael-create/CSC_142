# RaindropsManager and Raindrop implementation

import random
import pygame

class Raindrop:
    __slots__ = ('x', 'y', 'radius')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, surface):
        color = (0, 0, 255)
        position = (int(self.x), int(self.y))
        pygame.draw.circle(surface, color, position, self.radius)


class RaindropsManager:
    RAIN_RATE = 300  # milliseconds between raindrops
    MAX_RADIUS = 40  # after this radius, raindrop is removed

    def __init__(self, width=800, height=600, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Raindrops on Glass')

        self.clock = pygame.time.Clock()
        self.raindrops = []
        self.running = True
        self.last_drop_time = pygame.time.get_ticks()

    def add_raindrop(self):
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        self.raindrops.append(Raindrop(x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_drop_time >= self.RAIN_RATE:
            self.last_drop_time = now
            self.add_raindrop()

        for drop in list(self.raindrops):
            drop.update()
            if drop.radius > self.MAX_RADIUS:
                self.raindrops.remove(drop)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for drop in self.raindrops:
            drop.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()


if __name__ == '__main__':
    manager = RaindropsManager()
    manager.run()
