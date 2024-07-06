import matplotlib.pyplot as plt
import numpy as np


def generate_power_law_network(num_nodes, alpha, seed=None):
   
    np.random.seed(seed)

    # Generate power-law degree distribution
    degrees = np.arange(1, num_nodes + 1)
    degree_probs = 1 / np.power(degrees, alpha)
    degree_probs /= degree_probs.sum()

    # Generate degrees for each node
    node_degrees = np.random.choice(degrees, size=num_nodes, p=degree_probs)

    # Plot degree distribution
    plt.figure(figsize=(10, 6))
    plt.title("Power-law Degree Distribution")
    plt.plot(degrees, degree_probs, 'o', color='b', markersize=8)  # fixed keyword
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree (log scale)')
    plt.ylabel('Probability (log scale)')
    plt.show()

    return node_degrees


# Example usage
num_nodes = 20
alpha = 2.5
seed = 42
degrees = generate_power_law_network(num_nodes, alpha, seed)

print(degrees)
