from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, source):
        visited = set()
        queue = []
        queue.append(source)
        visited.add(source)
        while queue:
            first = queue.pop(0)
            print(first, end=" ")
            for neighbour in self.graph[first]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def DFS(self, source):
        visited = set()
        self.dfs(visited, self.graph, source)

    def dfs(self, visited, graph, source):
        if source not in visited:
            visited.add(source)
            print(source, end=" ")
            for neighbour in graph[source]:
                self.dfs(visited, graph, neighbour)

    def IDDFS(self, source, target, maxdepth):
        for i in range(maxdepth):
            if self.DLS(source, target, i):
                return True
        return False
    
    def DLS(self, source, target, maxdepth):
        if source == target:
            return True
        if maxdepth <=0:
            return False
        for i in self.graph[source]:
            if self.DLS(i, target, maxdepth-1):
                return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
print("\nDFS: ")
g.DFS(2)
print("\nID:")
target = 6; maxDepth = 3; src = 0
 
if g.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")