import math
import numpy as np
import random
import utils
import boids

def step(agent, speed, rotation_speed, WIDTH, HEIGHT):

        #print(agent.target_vec)
        #agent.vec = utils.lerp(agent.vec, agent.target_vec, 0.3)
        agent.vec = utils.unit_vector(agent.target_vec)
        # Update position
        agent.position = agent.position + speed * agent.vec
        #Ensure the triangle stays within the screen bounds
        if agent.position[0] < 0 or agent.position[0] > WIDTH or agent.position[1] < 0 or agent.position[1] > HEIGHT:
            agent.target_vec*= -1  # Reverse direction if out of bounds
            agent.position = (max(0, min(WIDTH, agent.position[0])), max(0, min(HEIGHT, agent.position[1])))