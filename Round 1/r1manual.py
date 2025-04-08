import numpy as np
import itertools

# Define the currencies in order: [Snowball, Pizza, Silicon, SeaShell]
currencies = ["Snowball", "Pizza", "Silicon", "SeaShell"]

M = np.array([
    [0.0, 1.45, 0.52, 0.72],    # From Snowball
    [0.70, 0.0, 0.31, 0.48],    # From Pizza
    [1.95, 3.10, 0.0, 1.49],    # From Silicon
    [1.34, 1.98, 0.64, 0.0]     # From SeaShell
])

start_currency = 3
end_currency = 3
num_trades = 5

max_profit = 0
best_path = []

# Generate all possible trade paths of length 6 (5 trades = 6 nodes), starting and ending with SeaShell
for path in itertools.product(range(4), repeat=num_trades - 1):
    full_path = [start_currency] + list(path) + [end_currency]
    value = 1.0
    valid = True
    for i in range(num_trades):
        rate = M[full_path[i]][full_path[i+1]]
        if rate == 0:
            valid = False
            break
        value *= rate
    if valid and value > max_profit:
        max_profit = value
        best_path = full_path

# Convert index path to currency names
best_path_named = [currencies[i] for i in best_path]
max_profit, best_path_named

print(best_path_named)