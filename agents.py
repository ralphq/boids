import math
import random
import simulate
import utils
import numpy as np

class Agent:
    def __init__(self, position, vec, vertices):
        self.position = position
        self.vec = vec
        self.vertices = vertices
        self.target_vec = vec # will be changed by boids

# returns a random position and heading 
def rand_init(screen_width, screen_height):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    vec = utils.rad_to_unitvec(random.uniform(0, 2 * math.pi))
    return x, y, vec

# creates agents. called once at beginning of sim
def create_agents(num_agents, screen_width, screen_height, size):
    agent_array = np.empty((0,))
    for agent in range(0,num_agents):
        x, y, vec = rand_init(screen_width, screen_height)
        vertices = simulate.draw_vertices(np.array([x, y]), math.atan2(y,x), size)
        agent_array = np.append(agent_array, Agent(np.array([x, y]), vec, vertices))

    return agent_array
