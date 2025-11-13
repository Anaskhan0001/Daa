def knapsack_01(weights, values, capacity):
    n = len(weights)
    # Create DP table with (n+1) rows and (capacity+1) columns
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include or exclude the item, whichever gives maximum value
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# -----------------------
# Main Program with User Input

weights = []
values = []

n = int(input("Enter number of items: "))
capacity = int(input("Enter capacity of knapsack: "))

for i in range(n):
    weight = int(input(f"\nEnter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

# Solve the 0-1 Knapsack problem
max_value = knapsack_01(weights, values, capacity)

print(f"\nMaximum value in knapsack: {max_value}")
