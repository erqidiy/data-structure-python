#!/usr/bin/python3

def dfs(graph, v, visited):
    visited.append(v)
    print(v, end=' ')

    for w in graph[v]:
        if w not in visited:
            dfs(graph, w, visited)


def bfs(graph, start):
    visited = [start]
    queue = [start]

    print(start, end=' ')
    
    while bool(queue):
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                print(w, end=' ')
                visited.append(w)
                queue.append(w)
    


if __name__ == "__main__":
    """
    graph = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'C', 'E'],
            'C': ['A', 'B', 'D'],
            'D': ['A', 'C', 'E'],
            'E': ['B', 'C', 'D']
        }
    """
    graph = {
            'A': ['B', 'C'],
            'B': ['A', 'E'],
            'C': ['D', 'E'],
            'D': [],
            'E': []
        
    }

    visited = []
    dfs(graph, 'A', visited)
    print()

    bfs(graph, 'A')
    print()
