# ============================================================
# Problem 3: Heuristic Algorithm
# A* Search for Path Finding
# ============================================================

import heapq  # Priority queue — used for input/output only, not core algorithm

# Calculate Manhattan Distance from cell a to cell b
# Used as the heuristic estimate (h) in A*
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* algorithm — finds shortest path from start to goal on the grid
# Returns the path (list of cells) and all explored cells
def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # Priority queue: stores (f_score, cell)
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}               # Tracks which cell each cell was reached from
    g_score = {start: 0}        # Actual steps taken from start to each cell
    f_score = {start: heuristic(start, goal)}  # g + h for each cell
    closed_set = set()           # Cells already fully processed

    while open_set:
        # Get the cell with lowest f_score
        _, current = heapq.heappop(open_set)

        # Skip if already processed
        if current in closed_set:
            continue
        closed_set.add(current)

        # Goal reached — trace path backwards from goal to start
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, closed_set

        # Check all 4 neighbours: up, down, left, right
        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = (r + dr, c + dc)
            nr, nc = neighbour

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue  # Out of bounds
            if grid[nr][nc] == 1:
                continue  # Wall
            if neighbour in closed_set:
                continue  # Already processed

            tentative_g = g_score[current] + 1  # Each step costs 1

            # Update neighbour if this path is cheaper
            if tentative_g < g_score.get(neighbour, float('inf')):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g
                f_score[neighbour] = tentative_g + heuristic(neighbour, goal)
                heapq.heappush(open_set, (f_score[neighbour], neighbour))

    return None, closed_set  # No path found


# Print the grid with search results overlaid
def print_grid(grid, path, start, goal, explored):
    print()
    print("Legend: S=Start  G=Goal  #=Wall  *=Path  .=Explored  O=Open")
    print()

    path_set = set(path) if path else set()

    for r in range(len(grid)):
        row_str = ""
        for c in range(len(grid[0])):
            cell = (r, c)
            if cell == start:
                row_str += " S "
            elif cell == goal:
                row_str += " G "
            elif grid[r][c] == 1:
                row_str += " # "
            elif cell in path_set:
                row_str += " * "
            elif cell in explored:
                row_str += " . "
            else:
                row_str += " O "
        print(row_str)
    print()


# Prompt user to enter grid size and cell values
def get_grid_input():
    print("=" * 55)
    print("       A* PATHFINDING - CSC2103 GROUP PROJECT")
    print("=" * 55)
    print("\nGrid cell values: 0 = open, 1 = wall/obstacle")
    print()

    while True:
        try:
            rows = int(input("Enter number of rows (3-15): "))
            cols = int(input("Enter number of columns (3-15): "))
            if 3 <= rows <= 15 and 3 <= cols <= 15:
                break
            print("  Rows and columns must be between 3 and 15.")
        except ValueError:
            print("  Invalid input. Enter integers only.")

    print(f"\nEnter the grid row by row.")
    print(f"Each row: {cols} values separated by spaces (0 or 1).")
    print(f"Example row: 0 0 1 0 0\n")

    grid = []
    for r in range(rows):
        while True:
            try:
                row_input = input(f"  Row {r+1}: ").strip().split()
                if len(row_input) != cols:
                    print(f"  Need exactly {cols} values.")
                    continue
                row = [int(x) for x in row_input]
                if not all(v in (0, 1) for v in row):
                    print("  Only 0 or 1 allowed.")
                    continue
                grid.append(row)
                break
            except ValueError:
                print("  Invalid input. Use 0s and 1s only.")

    return grid, rows, cols


# Prompt user to enter a valid coordinate (not a wall, not out of bounds)
def get_coordinate(label, rows, cols, grid):
    while True:
        try:
            r = int(input(f"  {label} row (0 to {rows-1}): "))
            c = int(input(f"  {label} col (0 to {cols-1}): "))
            if not (0 <= r < rows and 0 <= c < cols):
                print("  Out of bounds.")
            elif grid[r][c] == 1:
                print("  That cell is a wall. Choose an open cell.")
            else:
                return (r, c)
        except ValueError:
            print("  Enter integers only.")


# Print the final path as a step-by-step table
def print_path_table(path):
    print(f"  {'Step':<6} {'Row':<6} {'Col':<6}")
    print(f"  {'-'*18}")
    for i, (r, c) in enumerate(path):
        label = "(Start)" if i == 0 else "(Goal)" if i == len(path) - 1 else ""
        print(f"  {i:<6} {r:<6} {c:<6} {label}")
    print()


# Main program — runs the full A* search flow
def main():
    grid, rows, cols = get_grid_input()

    print("\nSet Start and Goal positions (must be open cells — value 0):")
    start = get_coordinate("Start", rows, cols, grid)
    goal  = get_coordinate("Goal",  rows, cols, grid)

    if start == goal:
        print("\nStart and Goal are the same cell. No search needed.")
        return

    print("\nRunning A* Search...")
    path, explored = astar(grid, start, goal)

    print_grid(grid, path if path else [], start, goal, explored)

    print("=" * 55)
    print("                    RESULTS")
    print("=" * 55)

    if path:
        print(f"\n  Path FOUND from {start} to {goal}")
        print(f"  Path length : {len(path)} cells  ({len(path)-1} steps)")
        print(f"  Cells explored by A* : {len(explored)}")
        print()
        print("  Path sequence:")
        print_path_table(path)

        print("  Cost Summary")
        print(f"  {'g(n) - actual cost to goal':<35}: {len(path)-1}")
        print(f"  {'h(n) - heuristic at start (Manhattan)':<35}: {heuristic(start, goal)}")
        print(f"  {'f(n) = g(n) + h(n)':<35}: {len(path)-1 + heuristic(start, goal)}")
        print()
        print("  NOTE: A* uses heuristic (Manhattan distance) to guide")
        print("  the search. It is NOT guaranteed to be optimal if the")
        print("  heuristic overestimates (inadmissible). Here, Manhattan")
        print("  distance is admissible for 4-directional grids, so the")
        print("  result IS optimal for this configuration.")
    else:
        print(f"\n  No path found from {start} to {goal}.")
        print(f"  Cells explored before giving up: {len(explored)}")
        print("\n  The grid may be fully blocked. Try removing some walls.")

    print("\n" + "=" * 55)

    again = input("\nRun another search? (y/n): ").strip().lower()
    if again == 'y':
        print()
        main()
    else:
        print("\nExiting. Goodbye.")


# Run main only when this file is executed directly
if __name__ == "__main__":
    main()