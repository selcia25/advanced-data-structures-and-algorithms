def tsp_nearest_neighbour(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    path = [start]
    visited[start] = True
    total_dist = 0
    current_vertex = start
    while len(path) < num_vertices:
        next_vertex = None
        min = float('inf')
        for neighbor in range(num_vertices):
            if not visited[neighbor] and graph[current_vertex][neighbor] < min:
                next_vertex = neighbor
                min = graph[current_vertex][neighbor]
        path.append(next_vertex)
        visited[next_vertex] = True
        total_dist += min
        current_vertex = next_vertex
    return path, total_dist
graph = [[0,2,9,10], [1,0,6,4], [15,7,0,8], [6,3,12,0]]
start_vertex = 0
print(tsp_nearest_neighbour(graph, start_vertex))