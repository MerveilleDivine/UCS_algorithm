from collections import deque

# define the graph of the maze as a dictionary of edges, where the keys are the nodes and the values are lists of tuples (neighbor, cost)
maze_graph = {
    'A': [('B', 10), ('C', 3)],
    'B': [('D', 2), ('E', 1)],
    'C': [('B', 4), ('E', 8), ('F', 2)],
    'D': [('E', 7), ('F', 6)],
    'E': [('F', 1)],
    'F': []
}

def uniform_cost_search(graph, start, goal):
    # maintain a queue of paths
    queue = deque([[start]])
    # mark the starting node as visited
    visited = set([start])

    while queue:
        # get the first path from the queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]

        # if the node is the goal, return the path
        if node == goal:
            return path
        
        # iterate over the neighbors of the node
        for neighbor, cost in graph[node]:
            # if the neighbor has not been visited, add it to the queue
            if neighbor not in visited:
                # create a new path using the old path and the neighbor
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # mark the neighbor as visited
                visited.add(neighbor)

    # if no path is found, return None
    return None

# test the uniform cost search function
start = 'A'
goal = 'F'
path = uniform_cost_search(maze_graph, start, goal)
print(path)
