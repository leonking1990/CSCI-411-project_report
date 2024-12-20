# Pathfinding Algorithms: Dijkstra's and A*

## Overview
This project explores two prominent algorithms used for pathfinding in computational tasks: **Dijkstra's Algorithm** and **A\***. Both algorithms are foundational for solving shortest-path problems, with distinct strengths and ideal use cases.

- **Dijkstra's Algorithm**: Introduced in 1956, it systematically explores all possible routes to guarantee the shortest path.
- **A_Star (A\*) Algorithm**: Developed in 1968, it enhances Dijkstra's method by incorporating heuristics to prioritize promising paths, improving efficiency.

## Algorithms Overview

### Dijkstra's Algorithm
Dijkstra's algorithm is a deterministic method designed to find the shortest path in a graph. It is particularly effective for applications where accuracy is critical.  
**Key Features**:
- Guarantees the shortest path by systematically exploring all routes.
- Ideal for applications such as network routing, transportation systems, and optimization problems.
- Does not use heuristics, which may lead to slower performance when exploring large graphs or sparse connections.

**Pseudocode**:
```bash
function Dijkstra(graph, source, target)
    dist = Dictionary()  # Distance from source to each node
    prev = Dictionary()  # Previous node in optimal path
    for each node in graph
        dist[node] = ∞
        prev[node] = null
    dist[source] = 0

    Q = PriorityQueue()  # Min-heap priority queue
    Q.push(source, 0)

    while Q is not empty
        current = Q.pop()  # Node with smallest distance

        if current == target
            break

        for neighbor in graph.neighbors(current)
            alt = dist[current] + graph.weight(current, neighbor)
            if alt < dist[neighbor]
                dist[neighbor] = alt
                prev[neighbor] = current
                Q.push(neighbor, alt)

    return reconstructPath(prev, source, target)

function reconstructPath(prev, source, target)
    path = []
    current = target
    while current is not null
        path.prepend(current)
        current = prev[current]
    return path

```

### A* Algorithm
A* algorithm builds on Dijkstra’s principles by integrating heuristics to optimize the search process. It is particularly suited for dynamic and time-sensitive applications.  
**Key Features**:
- Combines the actual cost of reaching a node with an estimated cost to the goal.
- Uses heuristics to guide the search, significantly reducing the computational load.
- Commonly used in game development, robotics, and real-time navigation systems.

**Pseudocode**:
```bash
function AStar(graph, source, target, heuristic)
    dist = Dictionary()  # Distance from source to each node
    prev = Dictionary()  # Previous node in optimal path
    for each node in graph
        dist[node] = ∞
        prev[node] = null
    dist[source] = 0

    Q = PriorityQueue()  # Min-heap priority queue
    Q.push(source, heuristic(source, target))

    while Q is not empty
        current = Q.pop()  # Node with smallest f(n) = g(n) + h(n)

        if current == target
            break

        for neighbor in graph.neighbors(current)
            tentative_g = dist[current] + graph.weight(current, neighbor)
            if tentative_g < dist[neighbor]
                dist[neighbor] = tentative_g
                prev[neighbor] = current
                f_score = tentative_g + heuristic(neighbor, target)
                Q.push(neighbor, f_score)

    return reconstructPath(prev, source, target)
```

## Comparison

| Feature              | Dijkstra's Algorithm               | A* Algorithm                       |
|----------------------|------------------------------------|------------------------------------|
| **Optimality**       | Always guarantees the shortest path. | Depends on the heuristic (admissible/consistent). |
| **Efficiency**       | Explores all possible paths.        | Focuses on the most promising paths. |
| **Use Cases**        | Network routing, large graphs.      | Real-time systems, dynamic environments. |
| **Heuristics**       | Not used.                          | Essential for guiding the search. |

## Trade-offs
- **Dijkstra’s Algorithm**: Precision at the cost of efficiency.
- **A* Algorithm**: Speed at the risk of suboptimality if the heuristic is poorly designed.

## Practical Applications
- **Dijkstra's Algorithm**: Suitable for large-scale network routing problems where precision is more important than speed.
- **A\* Algorithm**: Ideal for time-sensitive scenarios like game development or autonomous vehicle navigation.

## Key Insights
- Dijkstra’s algorithm employs an **"uninformed search"** approach, systematically evaluating all nodes.
- A* algorithm exemplifies **"informed search"**, using heuristics to prioritize paths, enhancing performance in complex environments.

## Project Structure

### Files
- **`Comparison_Test.py`**: Python script to compare the performance of the two algorithms.
- **`implementation.py`**: Script that implements both algorithms and allows experimentation with different graph structures.
- **Figure**:
  - `Figure_1-1.png`: A visual representation of algorithm comparisons.



## Getting Started
### Requirements
- Python (with `NetworkX` for graph analysis)
- Any compatible IDE or text editor

### Example Usage
Implementations of both algorithms can be found in the `src` directory. Run the scripts to visualize how each algorithm handles different graph structures and pathfinding scenarios.

### Running the Code
1. Clone the repository:
   ```bash
    git clone https://github.com/leonking1990/CSCI-411-project_report.git
   ```
2. Navigate to the project folder
   ```bash
    cd pathfinding-algorithms
   ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
4. Run the comparison test:
   ```bash
    python Comparison_Test.py
   ```

### Visuals
Refer to the figure (```Figure_1-1.png```) for graphical insights into the algorithm's performance and heuristics.
![Figure 1-1: Algorithm Comparison](images/Figure_1-1.png)

## References

- GeeksforGeeks. "Difference Between Dijkstra’s Algorithm and A* Search Algorithm." [Read here](https://www.geeksforgeeks.org/difference-between-dijkstras-algorithm-and-a-search-algorithm/).
- Stanford University. "A* Comparison." [Read here](https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html).
- Coding Clutch. "The Most Popular Pathfinding Algorithms Explained: A* to Dijkstra’s." [Read here](https://codingclutch.com/the-most-popular-pathfinding-algorithms-explained-a-to-dijkstras/).

