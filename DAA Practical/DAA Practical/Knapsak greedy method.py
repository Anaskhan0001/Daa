# Function to solve Fractional Knapsack Problem
def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    
    # Calculate value-to-weight ratio for each item and store item index
    ratio = []
    for i in range(n):
        density = values[i] / weights[i]
        ratio.append((density, weights[i], values[i], i + 1))  # (density, weight, value, item number)

    # Sort items by descending ratio
    ratio.sort(reverse=True)

    total_value = 0.0
    items_taken = []

    print("\nProfit Densities in Decreasing Order:")
    print("Item\tWeight\tValue\tProfit Density")
    for r, w, v, idx in ratio:
        print(f"{idx}\t{w:.2f}\t{v:.2f}\t{r:.2f}")

    print("\nItems taken in the knapsack:")
    for r, weight, value, idx in ratio:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            items_taken.append((idx, weight, value, 1.0))  # Whole item taken
        else:
            fraction = capacity / weight
            total_value += value * fraction
            items_taken.append((idx, capacity, value * fraction, fraction))  # Fraction taken
            break  # Knapsack is full

    for idx, wt_taken, val_taken, frac in items_taken:
        if frac == 1.0:
            print(f"Item {idx}: 100% taken, Weight = {wt_taken:.2f}, Value = {val_taken:.2f}")
        else:
            print(f"Item {idx}: {frac*100:.1f}% taken, Weight = {wt_taken:.2f}, Value = {val_taken:.2f}")

    return total_value

# -------------------
# Main Program with User Input

weights = []
values = []

n = int(input("Enter number of items: "))
capacity = float(input("Enter capacity of knapsack: "))

for i in range(n):
    weight = float(input(f"\nEnter weight of item {i+1}: "))
    value = float(input(f"Enter value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

# Solve the problem
max_value = fractional_knapsack(capacity, weights, values)

print(f"\nTotal Profit (Maximum value in knapsack): {max_value:.2f}")
