import matplotlib.pyplot as plt
import networkx as nx

# Preferential attachment network generation
num_nodes = 20
m = 5  # Number of edges to attach from new nodes each step
G = nx.barabasi_albert_graph(num_nodes, m)

# Define the degree distribution plotting function
def plot_degree_distribution(G):
    
    degrees = [G.degree(n) for n in G.nodes()]
 
    

# Analyze the degree distribution
plot_degree_distribution(G) 
def plot_degree_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)
    plt.xlabel("Degree (k)")
    plt.ylabel("Number of Nodes")
    plt.title("Degree Distribution")
    plt.loglog() 
    plt.legend(['Degree Distribution']) 
    
# Visualize the network 
plt.figure(figsize=(8,6)) 
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees)
plt.xlabel("Degree (k)")
plt.ylabel("Number of Nodes")
plt.title("Degree Distribution")
plt.loglog()  # Plot on a log-log scale
plt.legend(['Degree Distribution'])  # Add the legend here

plt.figure(figsize=(8, 8))
plt.title("Social Network Analysis")
nx.draw(G, with_labels=True, node_size=400) 
proxy_artist = plt.Line2D((0,1),(0,0), color='k', linestyle='-')
plt.legend([proxy_artist], ['Edge']) 

plt.show() 
