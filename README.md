# 8-Puzzle Solver

## Overview

This Python code implements the breadth-first search algorithm to solve the 8-puzzle problem. The goal is to rearrange a 3x3 grid of numbered tiles into a specific target state.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/collinblessing/8-puzzle-solver.git
    cd 8-puzzle-solver
    ```

2. Run the solver:

    ```bash
    python main.py
    ```

## How it Works

The code defines a `Node` class representing a node in the search tree. Each node contains information about its state, parent node, and the action that led to its creation.

### Functions

1. **`breadth_first_search(initial_state, goal_state)`**
   - Performs breadth-first search starting from the `initial_state` to reach the `goal_state`.
   - Uses a queue (`frontier`) to manage nodes to be explored and a set (`explored`) to track visited states.

2. **`get_successors(state)`**
   - Generates successor states of a given `state` by moving the empty tile in different directions.

3. **`reconstruct_path(node)`**
   - Traces back the path from the goal state to the initial state by following parent nodes.

4. **`get_inversion_count(state)`**
   - Calculates the inversion count of a given state, determining its solvability.

## Coupling and Cohesion

The code exhibits good cohesion, with each function having a clear and specific role in solving the 8-puzzle problem. The `Node` class encapsulates relevant attributes, promoting cohesion within the codebase. The functions work cohesively to implement the breadth-first search algorithm.

## Single Responsibility Principle

Each function adheres to the Single Responsibility Principle, with a clear and singular purpose. However, to enhance code readability and maintainability, it is suggested to extract the inversion count check into a separate function.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
