import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Ball class
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        # Update ball position
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        # Draw the ball
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


# Create a list of balls
def create_balls(num_balls):
    balls = []
    for _ in range(num_balls):
        radius = random.randint(10, 30)
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        speed_x = random.choice([-5, -4, -3, 3, 4, 5])
        speed_y = random.choice([-5, -4, -3, 3, 4, 5])
        color = random.choice(BALL_COLORS)
        ball = Ball(x, y, radius, color, speed_x, speed_y)
        balls.append(ball)
    return balls


# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bouncing Balls")
    clock = pygame.time.Clock()

    # Create balls
    balls = create_balls(10)

    running = True
    while running:
        screen.fill(BLACK)  # Clear the screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw balls
        for ball in balls:
            ball.move()
            ball.draw(screen)

        pygame.display.flip()  # Update the screen
        clock.tick(FPS)  # Maintain frame rate

    pygame.quit()


if __name__ == "__main__":
    main()
