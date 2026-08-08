# CSC2103_Final-Assessment

# Project Overview
This project implements 3 algorithm-based solutions using different algorithmic approaches:
1. Greedy Algorithm (Dijkstra's Shortest Path Algorithm)
2. Dynamic Programming (Coin Change Problem)
3. Heuristic Algorithm (A* Search Algorithm)

All the programs were developed in Python as console-based applications.

# Requirements
- Python 3.x

# Executing the Programs
1. Download or clone this GitHub repository
2. Open a terminal in the project folder
3. Run the Python file for the required problem
4. Follow instructions shown in the console and enter the required inputs

# Project Structure
CSC2103_Final-Assessment/
├── problem1_greedyalgo.py
├── problem2_coin_change_dp.py
├── problem3_astar_pathfinding.py
├── README.md
└── Sample_input_output/
    ├── problem1_sample.txt
    ├── problem2_sample.txt
    └── problem3_sample.txt

# Problem 1: Dijkstra's Shortest Path Algorithm
Approach: Greedy Algorithm

Dijkstra's algorithm finds the shortest paths from a selected source vertex to reachable vertices in a weighted graph with non-negative edge weights.

Features:
- supports directed and undirected graphs
- allows custom vertex names and edge weights
- display selected vertices in order
- displays shortest distances and paths
- handles unreachable vertices by showing 'INF'
- allows repeated searches from different source vertices

Source code: problem1_greedyalgo.py

# Problem 2: Coin Change Problem
Approach: Dynamic Programming

The Coin Change algorithm finds the minimum number of coins needed to form a given target amount and shows the coin combination used.

Features:
- allow customize of coin denominations
- target amount entered in sen
- display minimum number of coins required
- display which coins were used and its quantities
- handles cases where the target amount cannot be formed

Source code: problem2_coin_change_dp.py

# Problem 3: A* Search Algorithm
Approach: Heuristic Algorithm

The A* Search algorithm finds a path between a starting point and a goal point on a grid with obstacles. It uses Manhattan distance to guide the search.

Features:
- allow customize of grid and obstacles
- allow choosing of starting and goal positions
- display cells explored during the search
- display final path and number of steps
- display path cost and heuristic information
- allow to run another search

Source code: problem3_astar_pathfinding.py

# Testing
Each programs was tested using different input cases to ensure the correctness and reliability of the implementation. 

# AI Usage
AI tools were used as supplementary assistance during the development process. Assistance included understanding the algorithm concepts, review of code logic, and debugging.

Further details are provided in 6. Declaration of AI Usage section of the final report.
