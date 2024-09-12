import math
import numpy as np
import random
import utils
import boids

def step(agent, speed, rotation_speed, WIDTH, HEIGHT):

        # normalize at each step to prevent acceleration
        agent.vec = utils.unit_vector(agent.target_vec)
        # update position
        agent.position = agent.position + speed * agent.vec

        # screenwrapping
        if agent.position[0] < 0:
            agent.position[0] += WIDTH
        elif agent.position[0] >= WIDTH:
            agent.position[0] -= WIDTH

        if agent.position[1] < 0:
            agent.position[1] += HEIGHT
        elif agent.position[1] >= HEIGHT:
            agent.position[1] -= HEIGHT