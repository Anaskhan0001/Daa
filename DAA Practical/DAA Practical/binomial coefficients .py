def binomial_coefficient(n, k):
    # Create a (n+1) x (k+1) table
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate binomial coefficients using DP
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases: C(i, 0) = C(i, i) = 1
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # DP relation: C(n, k) = C(n-1, k-1) + C(n-1, k)
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C


# --------- Main Program with User Input ---------
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# Get the whole table
C = binomial_coefficient(n, k)

# Print DP Table
print("\nDP Table (Binomial Coefficients):")
for i in range(n + 1):
    for j in range(k + 1):
        print(f"{C[i][j]:5}", end=" ")   # formatted spacing
    print()

# Final result
print(f"\nBinomial Coefficient C({n}, {k}) = {C[n][k]}")
