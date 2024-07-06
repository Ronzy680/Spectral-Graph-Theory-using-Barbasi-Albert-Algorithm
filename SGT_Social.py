import matplotlib.pyplot as plt
import numpy as np

def generate_social_network(num_nodes, seed=None):
    
    np.random.seed(seed)

    # Generate a fully connected network
    adjacency_matrix = np.ones((num_nodes, num_nodes)) - np.eye(num_nodes)

    return adjacency_matrix

def plot_social_network(adjacency_matrix, node_labels):
   
    num_nodes = adjacency_matrix.shape[0]

    plt.figure(figsize=(8, 8))
    plt.title("Social Network Analysis")


    # Plot nodes
    for i in range(num_nodes):
        plt.scatter(np.random.randn(1), np.random.randn(1), s=100, alpha=0.7, label=f"User {node_labels[i]}")

    # Connect all nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            plt.plot([np.random.randn(1), np.random.randn(1)], [np.random.randn(1), np.random.randn(1)], 'k-', alpha=0.3)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()


num_nodes = 10
seed = 42

# Generate a fully connected social network
social_network = generate_social_network(num_nodes, seed)

# Plot the social network with all users connected
plot_social_network(social_network, range(1, num_nodes + 1))
