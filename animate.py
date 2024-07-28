import pygame
import sys
import math
import random
import agents
import utils
import transition
import boids
import numpy as np

def animate(agents, WIDTH, HEIGHT):
    pygame.display.set_caption("Triangle Random Path")

    clock = pygame.time.Clock()
    running = True

    # Initialize agent-specific states
    for agent in agents:
        agent.current_angle = random.uniform(0, 2 * math.pi)
        agent.target_vec = agent.vec
        agent.direction_change_time = 0
        agent.direction_change_interval = random.randint(20, 50)

    speed = 0.05  # Adjust speed as needed
    rotation_speed = 0.5  # Adjust rotation speed for smooth turning
    size = 5
    threshold = (HEIGHT+WIDTH)/2 * 0.5

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill("BLACK")

        avg_pos = boids.cohesion(agents)
        boids.separation(agents, threshold)
        avg_heading = boids.alignment(agents)

        #avg_pos = [WIDTH/2, HEIGHT/2]

        for agent in agents:
            transition.step(agent, speed, rotation_speed, WIDTH, HEIGHT)
            vertices = utils.draw_vertices(agent.position, utils.unitvec_to_rad(agent.vec), size)
            pygame.draw.polygon(screen, "WHITE", vertices)
            pygame.draw.circle(screen, "GREEN", avg_pos, size/2)
            pygame.draw.line(screen, "RED", avg_pos, avg_pos+np.array((avg_heading))*(size/2), 5)

        pygame.display.flip()
        clock.tick(60)