import math

def shortest_path(M, start, goal):
    #path = [start]
    start_node = Node(start)
    start_node.f = start_node.h = euclidean_distance(M, start, goal)
    start_node.g = 0
    frontier = {}
    frontier[start] = start_node # number: node
    visited_nodes = {} # number: node
    current_node = Node(None)
    while current_node.number != goal:
        current_node = find_lowest_f(frontier) #take the node in path with lowest f
        del frontier[current_node.number]
        if current_node.number == goal:
            break
        visited_nodes[current_node.number] = current_node
        for neighbor in M.roads[current_node.number]:
            new_g = current_node.g + euclidean_distance(M, current_node.number, neighbor)
            if neighbor in visited_nodes:
                if new_g < visited_nodes[neighbor].g:
                    visited_nodes[neighbor].g = new_g
                    visited_nodes[neighbor].f = visited_nodes[neighbor].g + visited_nodes[neighbor].h
                    visited_nodes[neighbor].previous = current_node
            elif neighbor in frontier:
                if new_g < frontier[neighbor].g:
                    frontier[neighbor].g = new_g
                    frontier[neighbor].f = frontier[neighbor].g + frontier[neighbor].h
                    frontier[neighbor].previous = current_node
            elif not neighbor in visited_nodes and not neighbor in frontier:
                h = euclidean_distance(M, neighbor, goal)
                neighbor_node = Node(neighbor, new_g + h, new_g, h)
                neighbor_node.previous = current_node
                frontier[neighbor] = neighbor_node
    reverse_path = []
    while current_node is not None:
        reverse_path.append(current_node.number)
        current_node = current_node.previous
    reverse_path.reverse()
    return reverse_path

def euclidean_distance(M, a, b):
    return math.sqrt((M.intersections[a][0]-M.intersections[b][0])**2+(M.intersections[a][1]-M.intersections[b][1])**2)

class Node:

    def __init__(self, number, f=None, g=None, h=None):
        self.number = number
        self.f = f
        self.g = g
        self.h = h
        self.previous = None

def find_lowest_f(frontier):
    min_f = None
    for node in frontier:
        if min_f is None:
            min_f = frontier[node].f
            min_node = node
        elif frontier[node].f < min_f:
            min_f = frontier[node].f
            min_node = node
    return frontier[min_node]
