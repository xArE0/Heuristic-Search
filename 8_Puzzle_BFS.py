from collections import deque
import copy

# Goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions with their coordinate change
MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def manhattan_distance(state):
    """Calculate total Manhattan distance of the current state from the goal state."""
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = (val - 1) // 3, (val - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_blank_position(state):
    """Find the position of the blank (0) tile."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    """Check if the state is the goal state."""
    return state == GOAL_STATE

def state_to_tuple(state):
    """Convert 2D list state to a tuple for hashing in sets."""
    return tuple([num for row in state for num in row])

def generate_moves(state):
    """Generate all valid moves from the current state."""
    blank_i, blank_j = get_blank_position(state)
    possible_moves = []

    for move, (di, dj) in MOVES.items():
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            # Swap blank with the target tile
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            possible_moves.append((move, new_state))
    return possible_moves

def bfs(start_state):
    """Breadth-First Search to find the optimal path to the goal."""
    queue = deque()
    visited = set()

    queue.append((start_state, [], 0))
    visited.add(state_to_tuple(start_state))

    print("Initial State:")
    for row in start_state:
        print(row)
    print("Initial Manhattan Distance:", manhattan_distance(start_state))
    print()

    while queue:
        current_state, path, depth = queue.popleft()

        if is_goal(current_state):
            print("Goal reached!")
            return path

        for move, next_state in generate_moves(current_state):
            state_key = state_to_tuple(next_state)
            if state_key not in visited:
                visited.add(state_key)
                heuristic = manhattan_distance(next_state)
                print(f"Explored Move: {move}")
                for row in next_state:
                    print(row)
                print("Manhattan Distance:", heuristic)
                print()
                queue.append((next_state, path + [move], depth + 1))

    return None

# Example input
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]

solution_path = bfs(initial_state)

if solution_path:
    print("Optimal solution path (moves):")
    print(solution_path)
else:
    print("No solution found.")
