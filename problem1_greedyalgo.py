# ============================================================
# Problem 1: Solving Dijkstra’s Shortest Path Algorithm Using
# Greedy Algorithm
# ============================================================

"""Greedy Algorithm: Dijkstra's Shortest Path

Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a 
source vertex to all other vertices in a weighted graph with non-negative edge weights. 
This implementation allows users to input a graph, specify whether it is directed or 
undirected, and then compute the shortest paths from a chosen source vertex.
"""
INF = float('inf')

# input helpers
def get_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a value >= {min_value}.")
            continue
        return value

# yes/no input helper
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please answer 'y' or 'n'.")

# graph construction and Dijkstra's algorithm implementation
def build_graph():
    print("Graph Setup:")
    n = get_int("Enter number of vertices: ", min_value=1)

    # Collects a display name for each vertex, defaulting to 'A', 'B', ..., 'Z', 'V26', 'V27', etc. 
    labels = []
    for i in range(n):
        default = chr(65 + i) if i < 26 else f"V{i}"
        name = input(f"Name of vertex {i + 1} (leave blank for '{default}'): ").strip()
        labels.append(name if name else default)

    # Looks for empty neighbour list per vertex
    index = {label: i for i, label in enumerate(labels)}
    adj = [[] for _ in range(n)]

    # Asks the user whether the graph is directed or undirected and how many edges it contains.
    directed = get_yes_no("Is the graph directed? (y/n): ")
    m = get_int("Enter number of edges: ", min_value=0)

    # Reads edges from user input, ensuring valid vertex names and non-negative weights.
    print("For each edge, enter: <source> <destination> <weight>  (weight must be >= 0)")
    for e in range(m):
        while True:
            raw = input(f"Edge {e + 1}: ").split()
            if len(raw) != 3:
                print("Please enter exactly 3 values separated by spaces.")
                continue
            u_name, v_name, w_raw = raw
            if u_name not in index or v_name not in index:
                print("Unknown vertex name. Available vertices: " + ", ".join(labels))
                continue
            try:
                w = float(w_raw)
            except ValueError:
                print("Weight must be a number.")
                continue
            # Dijkstra's algorithm requires non-negative edge weights.
            if w < 0:
                print("Dijkstra's algorithm requires non-negative edge weights.")
                continue
            u, v = index[u_name], index[v_name]
            adj[u].append((v, w))
            # If the graph is undirected, add the reverse edge as well.
            if not directed:
                adj[v].append((u, w))
            break

    # Returns the vertex labels, their corresponding indices, and the adjacency list representation of the graph.
    return labels, index, adj

# Core algorithm
def dijkstra(n, adj, src):
    dist = [INF] * n
    prev = [None] * n
    visited = [False] * n
    dist[src] = 0
    settle_order = []

    # Each iteration settles one vertex, the one with the smallest tentative distance.
    for _ in range(n):
        # Greedy choice: settle the unvisited vertex currently closest to the source.
        u = -1
        best = INF
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i

        # If no unvisited vertex is reachable, we can stop early.
        if u == -1:
            break

        # Mark the chosen vertex as visited and record its distance.
        visited[u] = True
        settle_order.append((u, dist[u]))

        # Update the distances to its neighbors if a shorter path is found through u.
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    return dist, prev, settle_order

# Path reconstruction
def reconstruct_path(prev, src, target):
    # If the target is unreachable from the source, return None.
    if target != src and prev[target] is None:
        return None
    path = [target]
    cur = target
    while cur != src:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path

# Output formatting and display
def format_num(x):
    return "0" if x == 0 else f"{x:g}"

# Displays the results of Dijkstra's algorithm, including the order in which vertices were settled and the shortest paths from the source to all other vertices.
def display_results(labels, src, dist, prev, settle_order):
    print(f"\n Greedy Selection Order (source: {labels[src]})")
    print(f"{'Step':<6}{'Vertex Settled':<18}{'Distance from Source':<22}")
    print("-" * 46)
    for step, (u, d) in enumerate(settle_order, start=1):
        print(f"{step:<6}{labels[u]:<18}{format_num(d):<22}")

    # Table 2: Shortest paths from the source to all vertices, including unreachable ones.
    print(f"\n=== Shortest Paths from '{labels[src]}' ===")
    print(f"{'Vertex':<12}{'Distance':<12}{'Path'}")
    print("-" * 46)
    for i in range(len(labels)):
        if dist[i] == INF:
            print(f"{labels[i]:<12}{'INF':<12}unreachable")
        else:
            path = reconstruct_path(prev, src, i)
            path_str = " -> ".join(labels[p] for p in path)
            print(f"{labels[i]:<12}{format_num(dist[i]):<12}{path_str}")

# Main program loop
def main():
    print("Dijkstra's Shortest Path (Greedy Algo)")

    # Build the graph based on user input
    labels, index, adj = build_graph()

    # Allow the user to repeatedly run Dijkstra's algorithm from different source vertices until they choose to exit.
    while True:
        print("\nAvailable vertices:", ", ".join(labels))
        while True:
            src_name = input("Enter source vertex to run Dijkstra's algorithm from: ").strip()
            if src_name in index:
                break
            print("Unknown vertex. Please choose one from the list above.")
        src = index[src_name]

        # Run Dijkstra's algorithm and display the results
        dist, prev, settle_order = dijkstra(len(labels), adj, src)
        display_results(labels, src, dist, prev, settle_order)

        # Ask the user if they want to run the algorithm again from a different source vertex. If not, exit the loop and end the program.
        if not get_yes_no("\nRun again from a different source vertex? (y/n): "):
            break

# Entry point for the program. If this script is run directly, the main function will be executed.
if __name__ == "__main__":
    main()

