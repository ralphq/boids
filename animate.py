import pygame
import sys
import math
import random
import agents
import utils
import transition

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def animate(agents, WIDTH, HEIGHT):
    pygame.display.set_caption("Triangle Random Path")

    clock = pygame.time.Clock()
    running = True

    # Initialize agent-specific states
    for agent in agents:
        agent.current_angle = random.uniform(0, 2 * math.pi)
        agent.target_angle = agent.current_angle
        agent.direction_change_time = 0
        agent.direction_change_interval = random.randint(10, 30)

    speed = 5  # Adjust speed as needed
    rotation_speed = 0.05  # Adjust rotation speed for smooth turning

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill(BLACK)

        for agent in agents:
            transition.step(agent, speed, rotation_speed, WIDTH, HEIGHT)

            vertices = utils.draw_vertices(agent.position, agent.angle)
            pygame.draw.polygon(screen, RED, vertices)

        pygame.display.flip()
        clock.tick(60)