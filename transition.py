import math
import numpy as np
import random

def step(agent, speed, rotation_speed, WIDTH, HEIGHT):
        agent.direction_change_time += 1
        if agent.direction_change_time >= agent.direction_change_interval:
            agent.direction_change_time = 0
            agent.direction_change_interval = random.randint(10, 30)
            agent.target_angle = random.uniform(0, 2 * math.pi)

        # Calculate the smallest angular difference
        angle_diff = (agent.target_angle - agent.current_angle + math.pi) % (2 * math.pi) - math.pi

        # Adjust current angle smoothly towards target angle
        if abs(angle_diff) < rotation_speed:
            agent.current_angle = agent.target_angle
        else:
            agent.current_angle += rotation_speed * math.copysign(1, angle_diff)

        # Update position
        agent.position = (agent.position[0] + speed * math.cos(agent.current_angle), agent.position[1] + speed * math.sin(agent.current_angle))
        agent.angle = agent.current_angle

        #Ensure the triangle stays within the screen bounds
        if agent.position[0] < 0 or agent.position[0] > WIDTH or agent.position[1] < 0 or agent.position[1] > HEIGHT:
            agent.current_angle = (agent.current_angle + math.pi) % (2 * math.pi)  # Reverse direction if out of bounds
            position = (max(0, min(WIDTH, agent.position[0])), max(0, min(HEIGHT, agent.position[1])))