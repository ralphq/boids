import math
import pygame
import animate
import agents
import sys
import utils
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--num_agents',
        type=int,
        default=1
    )
    args = parser.parse_args()

    # Screen dimensions
    WIDTH, HEIGHT = 1250, 750
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    size = 5
    agent_array = agents.create_agents(args.num_agents, WIDTH, HEIGHT, size)

    pygame.init()
    animate.animate(agent_array, WIDTH, HEIGHT, size)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()