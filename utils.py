import math

def draw_vertices(position, angle):
    x, y = position
    size = 20

    # Define the vertices of the triangle
    front_vertex = (x + size * math.cos(angle), y + size * math.sin(angle))
    base_left = (x + size * math.cos(angle + 2 * math.pi / 3), y + size * math.sin(angle + 2 * math.pi / 3))
    base_right = (x + size * math.cos(angle - 2 * math.pi / 3), y + size * math.sin(angle - 2 * math.pi / 3))
    
    return [front_vertex, base_left, base_right]