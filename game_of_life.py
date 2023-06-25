import random
import time

def initialize_board(rows, cols, border_mode):
    if border_mode == 'no_border':
        board = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    else:
        border_value = 1 if border_mode == 'alive' else 0
        board = [[border_value if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 else random.choice([0, 1]) for j in range(cols)] for i in range(rows)]
    return board

def print_board(board):
    for row in board:
        for cell in row:
            print('█' if cell else ' ', end=' ')
        print()
    print()

def get_neighbor_count(board, row, col, border_mode):
    count = 0
    rows, cols = len(board), len(board[0])
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for offset in offsets:
        r = row + offset[0]
        c = col + offset[1]

        if border_mode == 'no_border':
            if r >= 0 and r < rows and c >= 0 and c < cols and board[r][c] == 1:
                count += 1
        else:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                count += 0 if border_mode == 'dead' else 1
            else:
                if board[r][c] == 1:
                    count += 1

    return count

def update_board(board, border_mode):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for row in range(len(board)):
        for col in range(len(board[0])):
            count = get_neighbor_count(board, row, col, border_mode)
            if border_mode != 'no_border' and (row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1):
                new_board[row][col] = board[row][col]
            elif board[row][col] == 1:
                if count == 2 or count == 3:
                    new_board[row][col] = 1
            else:
                if count == 3:
                    new_board[row][col] = 1

    return new_board

def run_game(rows, cols, generations, delay, border_mode):
    board = initialize_board(rows, cols, border_mode)

    for generation in range(generations):
        print(f"Generation {generation + 1}:")
        print_board(board)
        board = update_board(board, border_mode)
        time.sleep(delay)

# Example usage
rows = 12  # Add 2 for border
cols = 12  # Add 2 for border

print("Game of Life - Border Modes")
print("1. No Borders")
print("2. Borders with Dead Cells")
print("3. Borders with Alive Cells")
mode = int(input("Choose a mode (1-3): "))

if mode == 1:
    border_mode = 'no_border'  # No borders
elif mode == 2:
    border_mode = 'dead'  # Borders treated as dead cells
elif mode == 3:
    border_mode = 'alive'  # Borders treated as alive cells
else:
    print("Invalid mode. Using default mode: No Borders")
    border_mode = 'no_border'

generations = int(input("Enter the number of generations: "))
delay = float(input("Enter the delay (in seconds) between generations: "))

run_game(rows, cols, generations, delay, border_mode)
