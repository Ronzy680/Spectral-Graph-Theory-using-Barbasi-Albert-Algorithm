import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def generate_power_law_network(num_nodes, alpha, seed=None):
    np.random.seed(seed)

    # Generate power-law degree distribution
    degrees = np.arange(1, num_nodes + 1)
    degree_probs = 1 / np.power(degrees, alpha)
    degree_probs /= degree_probs.sum()

    # Generate degrees for each node
    node_degrees = np.random.choice(degrees, size=num_nodes, p=degree_probs)

    # Plot degree distribution
    plt.figure(figsize=(8, 6))
    plt.title("Power-law Degree Distribution")
    plt.plot(degrees, degree_probs, 'o', color='b', markersize=8)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree (log scale)')
    plt.ylabel('Probability (log scale)')
    plt.show()

    return node_degrees

def generate_and_visualize_network(num_nodes, m, alpha, seed=None):
    # Generate artificial power-law degree distribution
    degrees = generate_power_law_network(num_nodes, alpha, seed) 

    # Create a graph (Preferential attachment would be ideal, this is a workaround)
    G = nx.complete_graph(num_nodes)  # For now, make a complete graph

    # Assign approximate power-law degrees (ideally would change structure, not just degrees)
    new_degrees = dict(zip(G.nodes(), degrees))
    nx.set_node_attributes(G, new_degrees, 'degree')

    # Degree Distribution Analysis
    plot_degree_distribution(G)

    # Network Visualization
    layout = nx.spring_layout(G)  # Or explore other layouts
    plt.figure(figsize=(8, 8))
    plt.title("Social Network Analysis (Artificially Adjusted Degrees)")
    nx.draw(G, pos=layout, with_labels=True, node_size=400) 
    plt.show() 

def plot_degree_distribution(G):
    degrees = [d for n, d in G.degree()]  # Extract degrees
    plt.hist(degrees)
    plt.xlabel("Degree (k)")
    plt.ylabel("Number of Nodes")
    plt.title("Degree Distribution")
    plt.loglog() 
    plt.legend(['Degree Distribution'])  
    plt.show()

# Example usage
num_nodes = 20
alpha = 2.5
m = 2  # Parameter for preferential attachment (not fully used here)
seed = 42

generate_and_visualize_network(num_nodes, m, alpha, seed)
