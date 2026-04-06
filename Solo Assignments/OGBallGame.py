import pygame
import sys
import os
import random

# I will make a ball bounce around and can click on it.

class ballgame:
    def __init__(self, width=800, height=600, x=None, y=None):
        self.width = width
        self.height = height
        if x is None:
            self.x = width // 2
        else:
            self.x = x
        if y is None:
            self.y = height // 2
        else:
            self.y = y
        self.radius = 30
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def spawn_random(self):
        """Spawn the ball at a random position on the screen"""
        self.x = random.randint(self.radius, self.width - self.radius)
        self.y = random.randint(self.radius, self.height - self.radius)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius < 0 or self.x + self.radius > self.width:
            self.dx *= -1
            return True
        if self.y - self.radius < 0 or self.y + self.radius > self.height:
            self.dy *= -1
            return True
        return False

    def is_clicked(self, click_x, click_y):
        return (click_x - self.x) ** 2 + (click_y - self.y) ** 2 <= self.radius ** 2 

# Pygame setup
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
ROYAL_BLUE = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")
clock = pygame.time.Clock()

# Load ball image and sound
ball_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "Ball.png"))
ball_image = pygame.transform.scale(ball_image, (60, 60))
boing_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "Boing.mp3"))

# Setup font for text
font = pygame.font.Font(None, 36)

# Create initial ball
balls = [ballgame(WIDTH, HEIGHT)]
click_count = 0

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.is_clicked(event.pos[0], event.pos[1]):
                    print("Ball was clicked!")
                    click_count += 1
                    boing_sound.play()
                    # Respawn the ball at random position
                    ball.spawn_random()
                    break
    
    # Update
    for ball in balls:
        bounced = ball.move()
        if bounced:
            boing_sound.play()
    
    # Draw
    screen.fill(ROYAL_BLUE)
    for ball in balls:
        ball_rect = ball_image.get_rect(center=(int(ball.x), int(ball.y)))
        screen.blit(ball_image, ball_rect)
    
    # Draw counters
    click_text = font.render(f"Clicks: {click_count}", True, (255, 255, 255))
    ball_text = font.render(f"Balls: {len(balls)}", True, (255, 255, 255))
    screen.blit(click_text, (10, 10))
    screen.blit(ball_text, (10, 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()