import math
import random
import utils

class Agent:
    def __init__(self, position, attitude, vertices):
        self.position = position
        self.attitude = attitude
        self.vertices = vertices

# Function to generate a random position on the screen
def rand_init(screen_width, screen_height):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    angle = random.uniform(0, 2 * math.pi)
    return x, y, angle

def create_agents(num_agents, screen_width, screen_height):
    agents = []

    for agent in range(0,num_agents):
        x, y, angle = rand_init(screen_width, screen_height)
        vertices = utils.draw_vertices([x, y], angle)
        agents.append(Agent([x, y], angle, vertices))
    
    return agents