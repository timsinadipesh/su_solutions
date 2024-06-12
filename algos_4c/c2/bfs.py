# breadth first search implementation

from collections import deque

def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    
    visited.add(start_node)
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


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

bfs('A')
