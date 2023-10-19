class Graph:
    def __init__(self,n):
        self.vertices = n  #number of vertices
        self.graph = []

    def add_edge(self, from_vertice, to_vertice, weight):
        self.graph.append([from_vertice, to_vertice, weight])

    # to find parent of the given vertex
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def union(self, parent, rank, a, b):
        a_root = self.find(parent, a)
        b_root = self.find(parent, b)
        if rank[b_root] > rank[a_root] :
            parent[a_root] = b_root
        elif rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        else: 
            parent[b_root] = a_root
            rank[a_root] += 1

    def KruskalAlgo(self):
        MST = []
        e = 0  # Current edge being processed
        r = 0  # No. of edges
        self.graph = sorted(self.graph, key = lambda item : item[2]) 
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
    # total no. of edges must be self.vertices - 1
        while r < self.vertices - 1:
            from_vertice = self.graph[e][0]
            to = self.graph[e][1]
            weight = self.graph[e][2]
            e += 1
            a = self.find(parent, from_vertice)
            b = self.find(parent, to)
            if a != b:
                r += 1
                MST.append([from_vertice,to,weight])
                self.union(parent, rank, a, b)

        print("The edges of the MST are:")

        for from_vertice,to,weight in MST:
            print("(",from_vertice,",",to,")","-->",weight)

G = Graph(6)

G.add_edge(0, 1, 2) 
G.add_edge(0, 3, 1) 
G.add_edge(0, 4, 4) 
G.add_edge(1, 2, 3) 
G.add_edge(1, 3, 3) 
G.add_edge(1, 5, 7) 
G.add_edge(2, 3, 5) 
G.add_edge(2, 5, 8) 
G.add_edge(3, 4, 9) 
  
G.KruskalAlgo() 