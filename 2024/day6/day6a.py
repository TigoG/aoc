def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def move_guard(grid, start_x, start_y, direction):
    visited = set()  # Set to track distinct positions visited by the guard
    directions = ['^', '>', 'v', '<']  # Direction order: up, right, down, left
    dx = [-1, 0, 1, 0]  # x offset for each direction
    dy = [0, 1, 0, -1]  # y offset for each direction
    direction_index = directions.index(direction)
    
    x, y = start_x, start_y
    rows, cols = len(grid), len(grid[0])
    
    while 0 <= x < rows and 0 <= y < cols:
        visited.add((x, y))  # Mark the current position as visited
        
        # If there's an obstacle, turn right
        if grid[x][y] == '#':
            direction_index = (direction_index + 1) % 4  # Turn right 90 degrees
        else:
            # Move forward in the current direction
            x += dx[direction_index]
            y += dy[direction_index]
    
    return visited

def count_visited_positions(grid, start_x, start_y, direction):
    # Get the visited positions by simulating the guard's movement
    visited_positions = move_guard(grid, start_x, start_y, direction)
    return len(visited_positions)

# Read the grid from input.txt
file_path = 'input.txt'
grid = read_grid(file_path)

# Find the starting position of the guard (represented by ^)
start_x, start_y = None, None
direction = None

# Locate the guard's starting position
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            start_x, start_y = i, j
            direction = '^'  # The guard starts facing up
            break
    if start_x is not None:
        break

# Calculate the number of distinct positions visited
if start_x is not None and start_y is not None:
    print(count_visited_positions(grid, start_x, start_y, direction))
else:
    print("Guard starting position not found.")
