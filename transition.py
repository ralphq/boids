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

        if agent.position[0] < 0:
            agent.position[0] += WIDTH
        elif agent.position[0] >= WIDTH:
            agent.position[0] -= WIDTH

        if agent.position[1] < 0:
            agent.position[1] += HEIGHT
        elif agent.position[1] >= HEIGHT:
            agent.position[1] -= HEIGHT