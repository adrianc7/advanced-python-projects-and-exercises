'''

Easy: (5 points)
Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.


'''

import networkx as nx # Downloaded thru terminal

def node_count(graph):
    return graph.number_of_nodes()


# Example Usage of this Function (will print the # of nodes)
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(10, 20), (20, 30)])  
    print("Number of nodes:", node_count(G)) # Output is 3