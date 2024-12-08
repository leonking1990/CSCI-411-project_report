import networkx as nx
import time
import matplotlib.pyplot as plt
import random
import numpy as np

# Generate test graphs
def generate_graphs(num_graphs, num_nodes, edge_probability_range):
    graphs = []
    for _ in range(num_graphs):
        edge_probability = random.uniform(*edge_probability_range)
        G = nx.gnp_random_graph(num_nodes, edge_probability, directed=False)
        for (u, v) in G.edges():
            G[u][v]['weight'] = random.randint(1, 10)
        graphs.append(G)
    return graphs

# Measure runtime for a single algorithm
def measure_runtime(graph, algorithm, source, target, heuristic=None):
    try:
        start_time = time.time()
        if algorithm == "dijkstra":
            nx.single_source_dijkstra_path(graph, source) # I am using a liberty here ask if that is okay
        elif algorithm == "a_star":
            nx.astar_path(graph, source, target, heuristic=heuristic)
        return time.time() - start_time
    except nx.NetworkXNoPath:
        return None  # No path between source and target

# Custom heuristic for A* (example: returns 0 for generic graphs)
def custom_heuristic(u, v):
    return 0  # Adjust based on specific graph requirements

# Test and record runtimes
def test_algorithms(graphs, algorithm):
    runtimes = []
    for G in graphs:
        nodes = list(G.nodes)
        if len(nodes) < 2:
            continue
        source, target = random.sample(nodes, 2)
        runtime = measure_runtime(G, algorithm, source, target)
        if runtime is not None:  # Skip graphs with no valid path
            runtimes.append(runtime)
    return runtimes


# Main execution
def run_experiment(graph_sizes, edge_probability_range, num_repeats):
    avg_dijkstra_times = []
    avg_a_star_times = []
    dijkstra_std_devs = []
    a_star_std_devs = []
    
    for size in graph_sizes:
        dijkstra_runtimes = []
        a_star_runtimes = []
        
        for _ in range(num_repeats):
            graphs = generate_graphs(1, size, edge_probability_range)
            dijkstra_runtimes.extend(test_algorithms(graphs, "dijkstra"))
            a_star_runtimes.extend(test_algorithms(graphs, "a_star"))
        
        avg_dijkstra_times.append(np.mean(dijkstra_runtimes))
        avg_a_star_times.append(np.mean(a_star_runtimes))
        dijkstra_std_devs.append(np.std(dijkstra_runtimes))
        a_star_std_devs.append(np.std(a_star_runtimes))
    
    return graph_sizes, avg_dijkstra_times, dijkstra_std_devs, avg_a_star_times, a_star_std_devs

# Plot results with scatter and error bars
def plot_results(graph_sizes, avg_dijkstra_times, dijkstra_std_devs, avg_a_star_times, a_star_std_devs):
    plt.errorbar(graph_sizes, avg_dijkstra_times, yerr=dijkstra_std_devs, fmt='o', label="Dijkstra's Algorithm", capsize=5)
    plt.errorbar(graph_sizes, avg_a_star_times, yerr=a_star_std_devs, fmt='o', label="A* Algorithm", capsize=5)
    plt.xlabel("Graph Size (Number of Nodes)")
    plt.ylabel("Average Runtime (seconds)")
    plt.title("Runtime Comparison with Error Bars")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to get graph sizes based on user input
def get_graph_sizes():
    while True:
        try:
            start = int(input("Enter the starting graph size (minimum 10): "))
            end = int(input("Enter the ending graph size (maximum 5000): "))
            
            if start < 10 or end > 5000 or start >= end:
                print("Please enter a starting size of at least 10 and an ending size greater than the start and up to 5000.")
                continue
            
            if end <= 100:
                step = 10
            elif end <= 500:
                step = 20
            else:
                sizes = [10, 50, 100]
                sizes.extend(range(200, end + 1, 100))
                return sizes
            
            return list(range(start, end + 1, step))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Parameters
graph_sizes = get_graph_sizes()  # Sizes of graphs
edge_probability_range = (0.1, 0.3)     # Range of edge densities
num_repeats = 5                         # Repeat for averaging

# Run experiment and plot
sizes, avg_d_times, d_std_devs, avg_a_times, a_std_devs = run_experiment(graph_sizes, edge_probability_range, num_repeats)
plot_results(sizes, avg_d_times, d_std_devs, avg_a_times, a_std_devs)
