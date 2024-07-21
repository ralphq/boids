import pygame
import sys
import math
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triangle Random Path")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_triangle(screen, color, position, angle):
    x, y = position
    size = 20

    # Define the vertices of the triangle
    front_vertex = (x + size * math.cos(angle), y + size * math.sin(angle))
    base_left = (x + size * math.cos(angle + 2 * math.pi / 3), y + size * math.sin(angle + 2 * math.pi / 3))
    base_right = (x + size * math.cos(angle - 2 * math.pi / 3), y + size * math.sin(angle - 2 * math.pi / 3))

    pygame.draw.polygon(screen, color, [front_vertex, base_left, base_right])

def main():
    clock = pygame.time.Clock()
    running = True

    position = (WIDTH // 2, HEIGHT // 2)
    current_angle = random.uniform(0, 2 * math.pi)
    target_angle = current_angle
    speed = 5  # Adjust speed as needed
    rotation_speed = 0.05  # Adjust rotation speed for smooth turning

    direction_change_time = 0
    direction_change_interval = random.randint(10, 30)  # Change direction more frequently

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Change direction at random intervals
        direction_change_time += 1
        if direction_change_time >= direction_change_interval:
            direction_change_time = 0
            direction_change_interval = random.randint(10, 30)
            target_angle = random.uniform(0, 2 * math.pi)

        # Calculate the smallest angular difference
        angle_diff = (target_angle - current_angle + math.pi) % (2 * math.pi) - math.pi

        # Adjust current angle smoothly towards target angle
        if abs(angle_diff) < rotation_speed:
            current_angle = target_angle
        else:
            current_angle += rotation_speed * math.copysign(1, angle_diff)

        # Update position
        position = (position[0] + speed * math.cos(current_angle), position[1] + speed * math.sin(current_angle))

        # Ensure the triangle stays within the screen bounds
        if position[0] < 0 or position[0] > WIDTH or position[1] < 0 or position[1] > HEIGHT:
            current_angle = (current_angle + math.pi) % (2 * math.pi)  # Reverse direction if out of bounds
            position = (max(0, min(WIDTH, position[0])), max(0, min(HEIGHT, position[1])))

        draw_triangle(screen, RED, position, current_angle)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
