
import os

# Function to initialize the game grid
def initialize_grid(size=4):
    return [[0 for _ in range(size)] for _ in range(size)]

# Function to add a new tile (2 or 4) to a random empty cell
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Function to print the game grid
def print_grid(grid):
    os.system('clear')  # Clear the console (for Linux/Mac, use 'cls' for Windows)
    print("2048 Game\n")
    for row in grid:
        print(" ".join(str(cell).rjust(4) for cell in row))
    print()

# Function to check if the game is over
def is_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    return True

# Function to merge tiles in a row
def merge(row):
    new_row = [0] * len(row)
    j = 0
    for i in range(len(row)):
        if row[i] != 0:
            if new_row[j] == 0:
                new_row[j] = row[i]
            elif new_row[j] == row[i]:
                new_row[j] *= 2
                j += 1
            else:
                j += 1
                new_row[j] = row[i]
    return new_row

# Function to move tiles in a grid
def move(grid, direction):
    if direction == 'left':
        for i in range(len(grid)):
            grid[i] = merge(grid[i])
    elif direction == 'right':
        for i in range(len(grid)):
            grid[i] = merge(grid[i][::-1])[::-1]
    elif direction == 'up':
        grid = [list(col) for col in zip(*grid)]
        for i in range(len(grid)):
            grid[i] = merge(grid[i])
        grid = [list(col) for col in zip(*grid)]
    elif direction == 'down':
        grid = [list(col) for col in zip(*grid)]
        for i in range(len(grid)):
            grid[i] = merge(grid[i][::-1])[::-1]
        grid = [list(col) for col in zip(*grid)]
    return grid

# Main game loop
def main():
    size = 4
    grid = initialize_grid(size)
    add_new_tile(grid)
    add_new_tile(grid)
    while True:
        print_grid(grid)
        if is_game_over(grid):
            print("Game Over!")
            break
        direction = input("Enter direction (W/A/S/D): ").strip().lower()
        if direction in ['w', 'a', 's', 'd']:
            grid = move(grid, 'up') if direction == 'w' else \
                   move(grid, 'left') if direction == 'a' else \
                   move(grid, 'down') if direction == 's' else \
                   move(grid, 'right')
            add_new_tile(grid)
        else:
            print("Invalid direction. Use W/A/S/D to move.")
    print_grid(grid)

if __name__ == "__main__":
    main()



