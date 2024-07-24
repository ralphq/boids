import math
import random
import utils
import numpy as np

class Agent:
    def __init__(self, position, vec, vertices):
        self.position = position
        self.vec = vec
        self.vertices = vertices

# Function to generate a random position on the screen
def rand_init(screen_width, screen_height):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vec = utils.rad_to_unitvec(random.uniform(0, 2 * math.pi))
    return x, y, vec

def create_agents(num_agents, screen_width, screen_height):
    agent_array = np.empty((0,))

    for agent in range(0,num_agents):
        x, y, vec = rand_init(screen_width, screen_height)
        vertices = utils.draw_vertices([x, y], math.atan2(y,x))
        agent_array = np.append(agent_array, Agent([x, y], vec, vertices))
    
    return agent_array