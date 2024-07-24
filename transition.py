import math
import numpy as np
import random
import utils

def step(agent, speed, rotation_speed, WIDTH, HEIGHT):
        
        print(agent.target_vec)

        agent.direction_change_time += 1
        if agent.direction_change_time >= agent.direction_change_interval:
            agent.direction_change_time = 0
            agent.direction_change_interval = random.randint(10, 30)
            agent.target_vec = utils.rad_to_unitvec(random.uniform(0, 2 * math.pi))

        # Calculate the smallest angular difference
        vec_diff = (agent.target_vec - agent.vec)

        # # Adjust current angle smoothly towards target angle
        # if abs(utils.unitvec_to_rad(vec_diff) < rotation_speed):
        #     agent.vec = agent.target_vec
        # else:
        #     agent.vec += rotation_speed*vec_diff

        agent.vec = utils.lerp(agent.vec, agent.target_vec, rotation_speed)

        # Update position
        agent.position = (agent.position + speed * agent.vec)
        agent.angle = agent.current_angle

        #Ensure the triangle stays within the screen bounds
        print(agent.position)
        if agent.position[0] < 0 or agent.position[0] > WIDTH or agent.position[1] < 0 or agent.position[1] > HEIGHT:
            agent.vec *= -1  # Reverse direction if out of bounds
            agent.position = (max(0, min(WIDTH, agent.position[0])), max(0, min(HEIGHT, agent.position[1])))