def has_cycle(graph, v, visited, recursion_stack):
    visited.add(v)
    recursion_stack.add(v)
    for neighbor in graph[v]:
        if neighbor in recursion_stack:
            return True
        if neighbor not in visited and has_cycle(graph, neighbor, visited, recursion_stack):
            return True
    recursion_stack.remove(v)
    return False

def has_cycle_in_graph(graph):
    visited = set()
    recursion_stack = set()
    for v in graph:
        if v not in visited and has_cycle(graph, v, visited, recursion_stack):
            return True
    return False

num_vertices = int(input("Enter the number of vertices in the graph: "))
num_edges = int(input("Enter the number of edges in the graph: "))

# Initialize the adjacency list with empty lists for each vertex
graph = {v: [] for v in range(1, num_vertices + 1)}

# Read the edges from the user
print("Enter the edges in the format 'source destination':")
for _ in range(num_edges):
    source, destination = map(int, input().split())
    graph[source].append(destination)

if has_cycle_in_graph(graph):
    print("The graph contains cycles.")
else:
    print("The graph does not contain cycles.")