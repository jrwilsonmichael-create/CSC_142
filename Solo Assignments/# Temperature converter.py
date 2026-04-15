# Temperature converter
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False

    def draw(self, surface):
        color = GRAY if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        text_surf = SMALL_FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click

class TemperatureConverter:
    def __init__(self):
        self.input_text = ""
        self.result_text = ""
        self.conversion_type = "C to F"  # Default

    def celsius_to_fahrenheit(self, temp):
        return (temp * 9/5) + 32

    def fahrenheit_to_celsius(self, temp):
        return (temp - 32) * 5/9

    def convert(self):
        try:
            temp = float(self.input_text)
            if self.conversion_type == "C to F":
                result = self.celsius_to_fahrenheit(temp)
                self.result_text = f"{temp:.2f}°C = {result:.2f}°F"
            else:
                result = self.fahrenheit_to_celsius(temp)
                self.result_text = f"{temp:.2f}°F = {result:.2f}°C"
        except ValueError:
            self.result_text = "Invalid input"

def main():
    converter = TemperatureConverter()

    # Create buttons
    button_c_to_f = Button(50, 100, 120, 40, "Celsius to F", BLUE)
    button_f_to_c = Button(200, 100, 120, 40, "F to Celsius", BLUE)
    button_convert = Button(150, 160, 100, 40, "Convert", BLUE)

    input_rect = pygame.Rect(100, 50, 200, 32)
    active = False

    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        converter.convert()
                    elif event.key == pygame.K_BACKSPACE:
                        converter.input_text = converter.input_text[:-1]
                    else:
                        converter.input_text += event.unicode

        # Check button hovers and clicks
        button_c_to_f.check_hover(mouse_pos)
        button_f_to_c.check_hover(mouse_pos)
        button_convert.check_hover(mouse_pos)

        if button_c_to_f.is_clicked(mouse_pos, mouse_click):
            converter.conversion_type = "C to F"
        if button_f_to_c.is_clicked(mouse_pos, mouse_click):
            converter.conversion_type = "F to C"
        if button_convert.is_clicked(mouse_pos, mouse_click):
            converter.convert()

        # Draw everything
        window.fill(WHITE)

        # Draw input box
        color = GRAY if active else BLACK
        pygame.draw.rect(window, color, input_rect, 2)
        txt_surface = FONT.render(converter.input_text, True, BLACK)
        window.blit(txt_surface, (input_rect.x+5, input_rect.y+5))

        # Draw buttons
        button_c_to_f.draw(window)
        button_f_to_c.draw(window)
        button_convert.draw(window)

        # Draw result
        result_surf = SMALL_FONT.render(converter.result_text, True, BLACK)
        window.blit(result_surf, (50, 220))

        # Draw labels
        label_surf = SMALL_FONT.render("Enter temperature:", True, BLACK)
        window.blit(label_surf, (100, 20))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

            