import heapq

def dijkstra(graph, source, target):
    # Initialize distances and previous nodes
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    # Priority queue
    Q = []
    heapq.heappush(Q, (0, source))

    while Q:
        current_dist, current = heapq.heappop(Q)

        # Stop if the target is reached
        if current == target:
            break

        # Update distances for neighbors
        for neighbor, weight in graph[current].items():
            alt = current_dist + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current
                heapq.heappush(Q, (alt, neighbor))

    return reconstruct_path(prev, source, target)


def a_star(graph, source, target, heuristic):
    # Initialize distances and previous nodes
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    # Priority queue
    Q = []
    heapq.heappush(Q, (heuristic(source), source))

    while Q:
        current_f, current = heapq.heappop(Q)

        # Stop if the target is reached
        if current == target:
            break

        # Update distances for neighbors
        for neighbor, weight in graph[current].items():
            tentative_g = dist[current] + weight
            if tentative_g < dist[neighbor]:
                dist[neighbor] = tentative_g
                prev[neighbor] = current
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(Q, (f_score, neighbor))

    return reconstruct_path(prev, source, target)

def reconstruct_path(prev, source, target):
    path = []
    current = target
    while current:
        path.insert(0, current)
        current = prev[current]
    return path if path[0] == source else None


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def heuristic(node,):
    h_values = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }
    return h_values[node]


# Dijkstra's Algorithm
shortest_path = dijkstra(graph, 'A', 'D')
print("Dijkstra's shortest path:", shortest_path)

# A* Algorithm
shortest_path = a_star(graph, 'A', 'D', heuristic)
print("A* shortest path:", shortest_path)
