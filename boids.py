import agents
import math
import utils
import numpy as np

"""
Implementation of Boid's algorithm based on https://en.wikipedia.org/wiki/Boids
Each rule of boid's algorithm adds a vector to the agent's target vector (the direction
in which it will fly next time step). Each rule's vector is weighted differently
based on visual tuning.
"""

# separation rule: steers away from agents within some threshold distance
def separation(agent, agent_array, THRESHOLD):
    for near_agent in agent_array:
        diff = np.array(near_agent.position) - np.array(agent.position)
        dist = np.linalg.norm(diff)
        if dist < THRESHOLD and dist!=0:
            agent.target_vec += -1*0.5*utils.unit_vector(diff)
            
# alignment and cohesion rules: steers towards average position and heading of neighbors
# these have been combined into one function since they both involve averaging across array
def alignment_and_cohesion(agent, agent_array):
    headings = np.empty(len(agent_array), dtype=object)
    positions = np.empty(len(agent_array), dtype=object)
    for i in range(0, len(agent_array)):
        headings[i] = agent_array[i].vec
        positions[i] = agent_array[i].position
    
    avg_heading = utils.avg(headings)
    agent.target_vec += 0.66*utils.unit_vector(avg_heading)
    
    avg_pos = utils.avg(positions)
    dist_from_avg = avg_pos - np.array(agent.position)
    agent.target_vec += 1.5*utils.unit_vector(dist_from_avg)

# not a rule of boid's algorithm, but minimizing screenwrapping improves aesthetics
def edge_avoidance(agent, WIDTH, HEIGHT, margin, force):
    if agent.position[0] < margin:
        agent.target_vec += np.array([force, 0])
    elif agent.position[0] > WIDTH - margin:
        agent.target_vec += np.array([-force, 0])
    
    if agent.position[1] < margin:
        agent.target_vec += np.array([0, force])
    elif agent.position[1] > HEIGHT - margin:
        agent.target_vec += np.array([0, -force])

# used to exclude agents outside a given radius from boid's algorithm calculations
def get_neighbors(agent, agent_array, radius):
    neighbors = []
    for agent_candidate in agent_array:
        diff = np.array(agent_candidate.position) - np.array(agent.position)
        dist = np.linalg.norm(diff)
        if dist < radius:
            neighbors.append(agent_candidate)
    
    return np.array(neighbors)