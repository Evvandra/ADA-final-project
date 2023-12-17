import matplotlib.pyplot as plt

coordinates = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 10),
    'D': (3, 6),
    'E': (4, 2),
    'F': (5, 8),
    'G': (6, 12),
    'H': (7, 1),
    'I': (8, 16),
    'J': (9, 4),
    'K': (10, 14),
    'L': (11, 7),
    'M': (12, 15),
    'N': (13, 5),
    'O': (14, 11),
    'P': (15, 9),
}

# Connecting the points in the order they are listed
route_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'A']

# Print the optimal route
print("Optimal Route:")
for point in route_order:
    print(f"{point}: {coordinates[point]}")

# Plotting the coordinates
x, y = zip(*coordinates.values())
plt.scatter(x, y)

# Connecting the points in the order they are listed
for i in range(len(route_order) - 1):
    plt.plot([coordinates[route_order[i]][0], coordinates[route_order[i + 1]][0]],
             [coordinates[route_order[i]][1], coordinates[route_order[i + 1]][1]], 'b-')

plt.title('Optimal Route')
plt.show()
