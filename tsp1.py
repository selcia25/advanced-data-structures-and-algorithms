import heapq

def tsp_branch_and_bound(graph, start):
    num_cities = len(graph)
    all_cities = set(range(num_cities))
    min_distance = float('inf')
    optimal_path = []
    
    # Priority queue to store partial paths
    queue = [(0, start, [start])]
    
    while queue:
        distance, current_city, path = heapq.heappop(queue)
        
        # Check if the path is complete
        if len(path) == num_cities:
            distance += graph[current_city][start]
            
            # Update the minimum distance and optimal path
            if distance < min_distance:
                min_distance = distance
                optimal_path = path
        
        # Explore the next cities
        for city in all_cities - set(path):
            new_distance = distance + graph[current_city][city]
            
            # Calculate the lower bound only if there are unvisited cities
            unvisited_cities = all_cities - set(path)
            if unvisited_cities:
                lower_bound = new_distance + min(graph[current_city][k] for k in unvisited_cities)
                
                # Prune branches if the lower bound exceeds the current minimum distance
                if lower_bound < min_distance:
                    heapq.heappush(queue, (new_distance, city, path + [city]))
    
    return optimal_path, min_distance

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start = 0
optimal_path, min_distance = tsp_branch_and_bound(distances, start)
print(f"Optimal path: {optimal_path}\nMinimum distance: {min_distance}")
