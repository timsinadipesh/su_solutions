import copy
import math
import random
import networkx as nx
import matplotlib.pyplot as plt

def min_cut(graph, target):
    """
    Contracts the graph until it has target number of vertices.
    """
    while len(graph) > target:
        # Select a random edge (start, finish)
        start = random.choice(list(graph.keys()))
        finish = random.choice(graph[start])

        # Merge the finish node into the start node
        for edge in graph[finish]:
            if edge != start:
                graph[start].append(edge)
        
        # Redirect all edges pointing to finish to point to start
        for edge in graph[finish]:
            graph[edge].remove(finish)
            if edge != start:
                graph[edge].append(start)
        
        # Remove the merged node
        del graph[finish]

    # The min cut is the number of edges in the remaining graph
    min_cut_value = len(graph[list(graph.keys())[0]])
    return min_cut_value

def draw_graph(graph):
    G = nx.Graph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)
    nx.draw(G, with_labels=True)
    plt.show()

def read_graph_from_file(filename):
    """
    Reads a graph from a file and returns it as an adjacency list.
    """
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = list(map(int, line.strip().split()))
            node = parts[0]
            edges = parts[1:]
            graph[node] = edges
    return graph

def main():
    filename = "KargerMinCut.txt"
    graph = read_graph_from_file(filename)
    draw_graph(graph)

    iterations = 1000
    min_cuts = []
    for i in range(iterations):
        graph_copy = copy.deepcopy(graph)
        min_cuts.append((i + 1, min_cut(graph_copy, 2)))

    # Print statistics of the graph
    edge_list = [len(edges) for edges in graph.values()]
    total_edges = sum(edge_list)
    print(f"Total nodes:   {len(graph)}")
    print(f"Total edges:   {total_edges // 2}")
    print(f"Avg degree:    {total_edges / len(edge_list)}")
    print(f"Max degree:    {max(edge_list)}")
    print(f"Min degree:    {min(edge_list)}")
    print(f"Iter, Max cut: {max(min_cuts, key=lambda x: x[1])}")
    print(f"Iter, Min cut: {min(min_cuts, key=lambda x: x[1])}")

if __name__ == '__main__':
    main()
