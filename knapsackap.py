def knapsack_greedy(N, W, values, weights):
    # Calculate value-to-weight ratios for all items
    ratios = [(values[i] / weights[i], i) for i in range(N)]
    ratios.sort(reverse = True)
    total_value = 0
    total_weight = 0
    for ratio, item in ratios:
        if total_weight + weights[item] <= W:
            total_value += values[item]
            total_weight += weights[item]
    return total_value

# Example usage
N = 3
W = 4
values = [1, 2, 3]
weights = [4, 5, 1]

result = knapsack_greedy(N, W, values, weights)
print("Maximum profit is "+str(result))