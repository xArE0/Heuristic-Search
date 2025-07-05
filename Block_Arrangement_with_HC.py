def heuristic(state, goal):
    """Heuristic: count how many blocks are out of place compared to the goal."""
    return sum(1 for i in range(len(state)) if state[i] != goal[i])

def get_neighbors(state):
    """Generate neighbors by swapping adjacent blocks."""
    neighbors = []
    for i in range(len(state) - 1):
        new_state = state.copy()
        # Swap adjacent blocks
        new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
        neighbors.append((new_state, f"swap({i}, {i+1})"))
    return neighbors

def hill_climbing(start_state, goal_state):
    """Hill Climbing algorithm to solve the block arrangement problem."""
    current_state = start_state
    current_h = heuristic(current_state, goal_state)
    path = []

    print("Initial Stack:", current_state)
    print("Initial Heuristic:", current_h)
    print()

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_h = current_h

        # Evaluate all neighbors to find the one with lowest heuristic
        for state, move in neighbors:
            h = heuristic(state, goal_state)
            print("Evaluating:", state, "| Heuristic:", h)
            if h < next_h:
                next_h = h
                next_state = (state, move)

        print()

        # No better neighbor found
        if next_state is None:
            print("Stuck at local minimum or reached goal.")
            break

        # Move to better neighbor
        current_state, move = next_state
        current_h = next_h
        path.append(move)
        print("Move:", move)
        print("Current Stack:", current_state)
        print("Current Heuristic:", current_h)
        print()

        # If goal reached
        if current_h == 0:
            break

    if current_h == 0:
        print("Goal reached!")
        print("Solution path:", path)
    else:
        print("Hill Climbing got stuck. Best state found:")
        print("Final Stack:", current_state)
        print("Path tried:", path)

# Example input
initial_stack = ['C', 'A', 'D', 'B']
goal_stack = ['A', 'B', 'C', 'D']

hill_climbing(initial_stack, goal_stack)
