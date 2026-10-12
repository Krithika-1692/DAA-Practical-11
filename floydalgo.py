
# Floyd-Warshall Algorithm

INF = float('inf')

n = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix (use INF for no edge):")
dist = []

for i in range(n):
    row = input().split()
    dist.append([INF if x.upper() == "INF" else int(x) for x in row])

# Floyd-Warshall algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# Display shortest distance matrix
print("Shortest distance matrix:")
for row in dist:
    print(*["INF" if x == INF else int(x) for x in row])
print("\nEN.No:92460118606")