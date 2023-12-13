from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        heuristic = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    target_row, target_col = divmod(value - 1, 3)
                    heuristic += abs(i - target_row) + abs(j - target_col)
        return heuristic

    def is_goal(self):
        return self.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def get_successors(self):
        successors = []
        zero_row, zero_col = self.find_zero()

        for i, j in [(zero_row - 1, zero_col), (zero_row, zero_col - 1),
                     (zero_row, zero_col + 1), (zero_row + 1, zero_col)]:
            if 0 <= i < 3 and 0 <= j < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_row][zero_col], new_state[i][j] = new_state[i][j], new_state[zero_row][zero_col]
                successors.append(PuzzleNode(new_state, self, (i, j), self.cost + 1))

        return successors

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def print_solution(self):
        if self.parent is not None:
            self.parent.print_solution()
        print(f"Move {self.move}:")
        print_board(self.state)
        print()

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = PriorityQueue()
    frontier.put(initial_node)

    visited = set()

    while not frontier.empty():
        current_node = frontier.get()

        if current_node.is_goal():
            current_node.print_solution()
            return

        visited.add(tuple(map(tuple, current_node.state)))

        successors = current_node.get_successors()
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in visited:
                frontier.put(successor)

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    print("Initial State:")
    print_board(initial_state)

    a_star(initial_state)

