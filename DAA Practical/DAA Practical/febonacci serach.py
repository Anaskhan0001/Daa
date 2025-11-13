# -----------------------------------------
# Fibonacci – Recursive and Iterative
# With Step Counting
# -----------------------------------------

# -------- Recursive Version --------
rec_steps = 0
def recursive_fib(n):
    global rec_steps
    rec_steps += 1                 # count each recursive call

    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


# -------- Iterative (Non-recursive) Version --------
iter_steps = 0
def iterative_fib(n):
    global iter_steps
    iter_steps = 0                 # reset step counter

    if n <= 1:
        iter_steps += 1
        return n

    a, b = 0, 1
    iter_steps += 1                # initialization counted

    for _ in range(2, n + 1):
        iter_steps += 1            # each loop iteration counted
        a, b = b, a + b

    return b


# --------------- MAIN PROGRAM ---------------
n = int(input("Enter value of n: "))

# Recursive Method
rec_steps = 0
try:
    rec_result = recursive_fib(n)
except RecursionError:
    rec_result = None

# Iterative Method
iter_result = iterative_fib(n)

# ------------ OUTPUT ------------
print("\n===== RECURSIVE OUTPUT =====")
print(f"Fibonacci({n}) =", rec_result)
print(f"Recursive Steps =", rec_steps)

print("\n===== NON-RECURSIVE (ITERATIVE) OUTPUT =====")
print(f"Fibonacci({n}) =", iter_result)
print(f"Iterative Steps =", iter_steps)
