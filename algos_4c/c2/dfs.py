# depth first search implementation

from collections import deque

def dfs(start_node):
    visited = set()
    stack = [start_node]
    
    visited.add(start_node)
    
    while stack:
        current_node = stack.pop()
        print(current_node, end=" ")
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)


# test
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'E'],
    'D': ['G'],
    'E': ['F', 'H'],
    'F': ['I'],
    'G': [],
    'H': ['J'],
    'I': ['K'],
    'J': [],
    'K': []
}

dfs('A')
