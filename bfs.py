# Implementation of BFS using Queue

from collections import defaultdict

class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def BFS(self, source_node):
        visited = []  # list for visited nodes
        queue = []    # initialize queue
        queue.append(source_node)  # add the source node to the visited list and queue
        visited.append(source_node)
        while queue:  # repeat until queue is empty
            first_in_queue = queue.pop(0) # take first element of queue and print
            print(first_in_queue, end=" ")
            for neighbour in self.graph[first_in_queue]: # look for neighbours of the element
                if neighbour not in visited: # if element is not in the visited list then add it to the visited list and the queue
                    visited.append(neighbour)
                    queue.append(neighbour)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
print("\nBreadth First Traversal (starting from vertex 0)")
g.BFS(0)
print("\nBreadth First Traversal (starting from vertex 1)")
g.BFS(1)
print("\nBreadth First Traversal (starting from vertex 3)")
g.BFS(3)

'''Time complexity is O(V+E)'''