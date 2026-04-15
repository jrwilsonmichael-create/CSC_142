import pygame
import random
import time

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Ball Game")
clock = pygame.time.Clock()

def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Load and scale ball image
ball_image = pygame.transform.scale(pygame.image.load('Ball.png'), (40, 40))  # 40x40 for radius 20

# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, WINDOW_WIDTH - ball_radius)
ball_y = random.randint(ball_radius, WINDOW_HEIGHT - ball_radius)
x_speed = random.randint(1, 5)
y_speed = random.randint(1, 5)

# Game variables
score = 0
start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x - ball_x)**2 + (mouse_y - ball_y)**2 <= ball_radius**2:
                score += 1
                # Play success sound effect (assuming sound file is available)
                # pygame.mixer.Sound('success.wav').play()
                
                # Randomize ball position
                ball_x = random.randint(ball_radius, WINDOW_WIDTH - ball_radius)
                ball_y = random.randint(ball_radius, WINDOW_HEIGHT - ball_radius)
                
                # Increase speeds in magnitude
                x_speed = (1 if x_speed >= 0 else -1) * (abs(x_speed) + random.randint(1, 5))
                y_speed = (1 if y_speed >= 0 else -1) * (abs(y_speed) + random.randint(1, 5))

    # Move ball
    ball_x += x_speed
    ball_y += y_speed

    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WINDOW_WIDTH:
        x_speed = -x_speed
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= WINDOW_HEIGHT:
        y_speed = -y_speed

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(ball_image, (ball_x - ball_radius, ball_y - ball_radius))
    draw_text(screen, f"Score: {score}", 10, 10, (255, 255, 255))

    if score >= 5:
        running = False

    pygame.display.flip()
    clock.tick(60)

# Game over screen
elapsed_time = time.time() - start_time
screen.fill((0, 0, 0))
text = f"You took {elapsed_time:.2f} seconds to get 5 points!"
text_font = pygame.font.SysFont(None, 36)
text_surface = text_font.render(text, True, (255, 255, 255))
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
screen.blit(text_surface, text_rect)
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()