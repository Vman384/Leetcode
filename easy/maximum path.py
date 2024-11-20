from collections import deque

def bfs_longest_path_value(graph, start):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    queue = deque()

    queue.append((start, graph[start]))  # Tuple: (current node, value of current node)
    visited[start] = True

    max_path_value = graph[start]

    while queue:
        node, path_value = queue.popleft()

        max_path_value = max(max_path_value, path_value)

        neighbors = get_neighbors(graph, node)
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append((neighbor, path_value + graph[neighbor]))
                visited[neighbor] = True

    return max_path_value

def get_neighbors(graph, node):
    neighbors = []
    if 0 <= node < len(graph):
        neighbors.append(graph[node])
    return neighbors

# Example graph as a 1D array
graph = [1, 3, -1, 3, 1, 5]

start_node = 0
longest_path_value = bfs_longest_path_value(graph, start_node)
print("Value of the longest path starting from node", start_node, ":", longest_path_value)
