"""Greedy Algorithm: Dijkstra's Shortest Path"""

INF = float('inf')


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


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please answer 'y' or 'n'.")


def build_graph():
    print("Graph Setup:")
    n = get_int("Enter number of vertices: ", min_value=1)

    labels = []
    for i in range(n):
        default = chr(65 + i) if i < 26 else f"V{i}"
        name = input(f"Name of vertex {i + 1} (leave blank for '{default}'): ").strip()
        labels.append(name if name else default)

    index = {label: i for i, label in enumerate(labels)}
    adj = [[] for _ in range(n)]

    directed = get_yes_no("Is the graph directed? (y/n): ")
    m = get_int("Enter number of edges: ", min_value=0)

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
            if w < 0:
                print("Dijkstra's algorithm requires non-negative edge weights.")
                continue
            u, v = index[u_name], index[v_name]
            adj[u].append((v, w))
            if not directed:
                adj[v].append((u, w))
            break

    return labels, index, adj


def dijkstra(n, adj, src):
    dist = [INF] * n
    prev = [None] * n
    visited = [False] * n
    dist[src] = 0
    settle_order = []

    for _ in range(n):
        # Greedy choice: settle the unvisited vertex currently closest to the source.
        u = -1
        best = INF
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i
        if u == -1:
            break

        visited[u] = True
        settle_order.append((u, dist[u]))

        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    return dist, prev, settle_order


def reconstruct_path(prev, src, target):
    if target != src and prev[target] is None:
        return None
    path = [target]
    cur = target
    while cur != src:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path


def format_num(x):
    return "0" if x == 0 else f"{x:g}"


def display_results(labels, src, dist, prev, settle_order):
    print(f"\n Greedy Selection Order (source: {labels[src]})")
    print(f"{'Step':<6}{'Vertex Settled':<18}{'Distance from Source':<22}")
    print("-" * 46)
    for step, (u, d) in enumerate(settle_order, start=1):
        print(f"{step:<6}{labels[u]:<18}{format_num(d):<22}")

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


def main():
    print("Dijkstra's Shortest Path (Greedy Algo)")

    labels, index, adj = build_graph()

    while True:
        print("\nAvailable vertices:", ", ".join(labels))
        while True:
            src_name = input("Enter source vertex to run Dijkstra's algorithm from: ").strip()
            if src_name in index:
                break
            print("Unknown vertex. Please choose one from the list above.")
        src = index[src_name]

        dist, prev, settle_order = dijkstra(len(labels), adj, src)
        display_results(labels, src, dist, prev, settle_order)

        if not get_yes_no("\nRun again from a different source vertex? (y/n): "):
            break

if __name__ == "__main__":
    main()

