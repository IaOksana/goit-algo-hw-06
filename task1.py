''' Task 1

Create a graph using the networkX library to model a real-world network (e.g., a city's 
transportation network, a social network, or an Internet topology).

info: 📖 The real network can be chosen at your discretion if you cannot come up with your 
network close to reality.

Visualize the created graph, and analyze the main characteristics (for example, the number of 
vertices and edges, the degree of vertices).

- Create and visualize a graph model of a real network.
- The main characteristics are analyzed. '''

import networkx as nx
import matplotlib.pyplot as plt
from graph_utils import create_graph

# Run the main operation.
def main():
    # Create the graph
    graph = create_graph()

    # Visualize the graph
    plt.figure(figsize=(8, 6))  # Adjust figure size if needed
    nx.draw(graph, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Simple Social Network')
    plt.show()

    # Analyze the main characteristics
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    degree_centrality = nx.degree_centrality(graph)

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print("Degree centrality:")
    for node, centrality in degree_centrality.items():
        print(f"  {node}: {centrality}")


if __name__ == "__main__":
    main()