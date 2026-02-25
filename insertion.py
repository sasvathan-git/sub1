import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heart on Black Screen")

clock = pygame.time.Clock()

def draw_heart(surface, color, center, size):
    points = []
    for t in range(0, 360):
        t = math.radians(t)
        x = 16 * math.sin(t)**3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t)
              - 2 * math.cos(3*t) - math.cos(4*t))
        points.append((
            center[0] + x * size,
            center[1] + y * size
        ))
    pygame.draw.polygon(surface, color, points)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Black background
    draw_heart(screen, (255, 0, 0), (width//2, height//2), 10)

    pygame.display.flip()
    clock.tick(60)
