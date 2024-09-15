import math
import os
import pygame
import simulate
import agents
import sys
import utils
import argparse
import glob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--num_agents',
        type=int,
        default=100,
        help="number of agents in simulation"
    )
    parser.add_argument(
        '--save_frames',
        type=bool,
        default=False,
        help="dictates whether to save frames from sim"
    )
    parser.add_argument(
        '--sim_length',
        type=int,
        default=300,
        help="dictates length of sim in frames. Note: pygame window runs at 30fps"
    )
    args = parser.parse_args()

    # Screen dimensions
    WIDTH, HEIGHT = 1250, 750
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    if args.save_frames:        
        if not os.path.exists("frames"):
            os.makedirs("frames")
        else:
            # delete the saved frames
            for file in glob.glob("frames/*.png"):
                os.remove(file)
        
    size = 5
    agent_array = agents.create_agents(args.num_agents, WIDTH, HEIGHT, size)

    pygame.init()
    simulate.simulate(agent_array, WIDTH, HEIGHT, size, args.save_frames, args.sim_length)

    sys.exit()

if __name__ == "__main__":
    main()