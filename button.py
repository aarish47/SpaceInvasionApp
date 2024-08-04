import pygame
import pygame.font

def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

class Button:
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)  # Black background
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.SysFont(None, 38)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        radius = 10  # Radius for the rounded corners
        draw_rounded_rect(self.screen, self.button_color, self.rect, radius)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# Example usage in a Pygame loop
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rounded Button Example")
    ai_settings = None  # Replace with your actual settings if needed
    button = Button(ai_settings, screen, "Play")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))  # Fill the screen with white
        button.draw_button()
        pygame.display.flip()

    pygame.quit()
