""""

Hard: (10 points)
Write a Python function that takes a NetworkX graph as input and returns 
  the number of nodes in the graph that have a degree greater than 5

"""
import networkx as nx

def count_nodes(graph, degree_threshold=5):
    degree_nodes = [node for node, degree in graph.degree() if degree > degree_threshold] # only if greater than 5
    return len(degree_nodes)

# Example usage
if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(10, 20), (20, 30), (30, 40), (10, 30), (20, 40), (20, 50), (50, 60)])  
    print("# of nodes with degree > 5:", count_nodes(G))

