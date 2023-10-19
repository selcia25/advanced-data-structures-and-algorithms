from collections import deque


def tsp_bfs(distances, start):
    num_cities = len(distances)
    all_cities = set(range(num_cities))
    min_distance = float('inf')
    optimal_path = []

    # Create a queue to store states
    queue = deque([(start, [start], 0)])

    while queue:
        current_city, path, distance = queue.popleft()

        if len(path) == num_cities:
            # If all cities have been visited, check if it's a better solution
            distance += distances[current_city][start]
            if distance < min_distance:
                min_distance = distance
                optimal_path = path
        else:
            # Generate new states by adding unvisited cities to the path
            for city in all_cities - set(path):
                new_distance = distance + distances[current_city][city]
                if new_distance < min_distance:
                    queue.append((city, path + [city], new_distance))

    return optimal_path, min_distance


# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0

optimal_path, min_distance = tsp_bfs(distances, start_city)

print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
