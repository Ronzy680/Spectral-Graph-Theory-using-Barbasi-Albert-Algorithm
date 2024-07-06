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

    # Adjust layout for better visualization
    layout = np.random.rand(num_nodes, 2) * 2 - 1

    # Plot nodes
    for i in range(num_nodes):
        plt.scatter(layout[i, 0], layout[i, 1], s=100, alpha=0.7, label=f"User {node_labels[i]}")

    # Connect nodes with edges that touch the nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i, j] == 1:
                # Calculate edge midpoint and offset vectors towards nodes
                midpoint = (layout[i] + layout[j]) / 2
                offset_i = (layout[i] - midpoint) * 0.1
                offset_j = (layout[j] - midpoint) * 0.1

                # Plot edge with slight adjustments to touch nodes
                plt.plot([layout[i, 0], midpoint[0] + offset_j[0]],
                         [layout[i, 1], midpoint[1] + offset_j[1]],
                         'k-', alpha=0.3)
                plt.plot([layout[j, 0], midpoint[0] - offset_i[0]],
                         [layout[j, 1], midpoint[1] - offset_i[1]],
                         'k-', alpha=0.3)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()


num_nodes = 10
seed = 42

# Generate a fully connected social network
social_network = generate_social_network(num_nodes, seed)

# Plot the social network with edges touching nodes
plot_social_network(social_network, range(1, num_nodes + 1))