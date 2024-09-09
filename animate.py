import pygame
import sys
import math
import random
import agents
import utils
import transition
import boids
import numpy as np

def animate(agents, WIDTH, HEIGHT,size):
    pygame.display.set_caption("Boids Algorithm Simulation")

    clock = pygame.time.Clock()
    running = True

    # Initialize agent-specific states
    for agent in agents:
        agent.current_angle = random.uniform(0, 2 * math.pi)
        agent.target_vec = agent.vec

    speed = 5  # Adjust speed as needed
    rotation_speed = 250  # Adjust rotation speed for smooth turning
    threshold = (HEIGHT+WIDTH)/2 * 0.05

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill("BLACK")

        for agent in agents:
            local_agents = boids.get_neighbors(agent, agents, 125)
            
            boids.separation(agent, local_agents, threshold)
            boids.alignment_and_cohesion(agent, local_agents)
                
            boids.edge_avoidance(agent, WIDTH, HEIGHT, 250, 2) # no loop

            transition.step(agent, speed, rotation_speed, WIDTH, HEIGHT)
            vertices = utils.draw_vertices(agent.position, utils.unitvec_to_rad(agent.vec), size)
            pygame.draw.polygon(screen, "WHITE", vertices)
            
        pygame.display.flip()
        clock.tick(60)