import pygame
import sys
import math
import random
import agents
import utils
import transition
import boids
import numpy as np


def animate(agents, WIDTH, HEIGHT, size, save_frames, sim_length):

    # initialize pygame window
    pygame.display.set_caption("Boids Algorithm Simulation")
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    frame_count = 0

    speed = 5  # adjust speed as needed
    rotation_speed = 250  # adjust rotation speed for smooth turning
    
    # distance-from-neighbor threshold at which separation rule takes effect
    threshold = (HEIGHT+WIDTH)/2 * 0.05

    # game window loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # paint over agent polygons from previous frame
        screen.fill("BLACK")

        # simulation loop
        for agent in agents:

            # only nearby agents should effect behavior
            local_agents = boids.get_neighbors(agent, agents, 125)
            
            # apply boid's algorithm to agent. see boids.py
            boids.separation(agent, local_agents, threshold)
            boids.alignment_and_cohesion(agent, local_agents)    
            boids.edge_avoidance(agent, WIDTH, HEIGHT, 250, 2) # no loop

            # move agents towards target vector defined by boids. see transition.py
            transition.step(agent, speed, rotation_speed, WIDTH, HEIGHT)

            # draw agents
            vertices = draw_vertices(agent.position, utils.unitvec_to_rad(agent.vec), size)
            pygame.draw.polygon(screen, "WHITE", vertices)
            

        # save each frame as an image
        if save_frames:
            pygame.image.save(screen, f"frames/frame_{frame_count:03d}.png")
        
        frame_count += 1
        clock.tick(30)

        # limits simulation length to 10s
        if frame_count >= sim_length:
            break

        pygame.display.flip()

def draw_vertices(position, angle, size):
    x, y = position

    # define the vertices of the triangle
    front_vertex = (x + size * math.cos(angle), y + size * math.sin(angle))
    base_left = (x + size * math.cos(angle + 2 * math.pi / 3), y + size * math.sin(angle + 2 * math.pi / 3))
    base_right = (x + size * math.cos(angle - 2 * math.pi / 3), y + size * math.sin(angle - 2 * math.pi / 3))
    
    return [front_vertex, base_left, base_right]

