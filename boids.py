import agents
import math
import utils
import numpy as np

def separation(agent_array, THRESHOLD):
    for i in range(0, len(agent_array)):
        agent = agent_array[i]
        temp_agent_array = np.delete(agent_array, i)
        distance = 0
        for j in range(0,len(temp_agent_array)):
            diff = np.array(temp_agent_array[j].position) - np.array(agent.position)
            dist = np.linalg.norm(diff)
            if dist < THRESHOLD:
                agent.target_vec += -1*0.2*utils.unit_vector2(diff, dist)
            
def alignment(agent_array):
    for agent in agent_array:
        headings = np.empty(len(agent_array), dtype=object)
        for i in range(0, len(agent_array)):
            headings[i] = agent_array[i].vec
        
        avg_heading = utils.avg(headings)

        for agent in agent_array:
            agent.target_vec += 0.025*utils.unit_vector(avg_heading)

    return avg_heading

def cohesion(agent_array):
    for agent in agent_array:
        positions = np.empty(len(agent_array), dtype=object)
        for i in range(0, len(agent_array)):
            positions[i] = agent_array[i].position

        avg_pos = utils.avg(positions)

        for agent in agent_array:
            dist_from_avg = avg_pos - np.array(agent.position)
            agent.target_vec += 5*utils.unit_vector(dist_from_avg)


def edge_avoidance(agents, WIDTH, HEIGHT, margin, force):
    for agent in agents:
        if agent.position[0] < margin:
            agent.target_vec += np.array([force, 0])
        elif agent.position[0] > WIDTH - margin:
            agent.target_vec += np.array([-force, 0])
        
        if agent.position[1] < margin:
            agent.target_vec += np.array([0, force])
        elif agent.position[1] > HEIGHT - margin:
            agent.target_vec += np.array([0, -force])

def get_neighbors(agent, agent_array, radius):
    neighbors = []
    for agent_candidate in agent_array:
        diff = np.array(agent_candidate.position) - np.array(agent.position)
        dist = np.linalg.norm(diff)
        if dist < radius:
            neighbors.append(agent_candidate)
    
    return np.array(neighbors)