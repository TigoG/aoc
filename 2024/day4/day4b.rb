def count_xmas_xmas_occurrences(grid)
  rows = grid.length
  cols = grid[0].length
  count = 0

  # Directions for the four possible diagonals
  directions = [
    [1, 1],  # Down-right
    [1, -1], # Down-left
    [-1, 1], # Up-right
    [-1, -1] # Up-left
  ]

  # Function to check if the "X-MAS" pattern can be found in a given direction
  def can_find_xmas_xmas?(grid, r, c, dr, dc)
    # Calculate the positions for the "X-MAS" pattern
    m1 = [r, c]
    a = [r + dr, c + dc]
    s1 = [r + 2 * dr, c + 2 * dc]
    s2 = [r - dr, c - dc]
    m2 = [r - 2 * dr, c - 2 * dc]

    # Ensure we're not out of bounds
    positions = [m1, a, s1, s2, m2]
    return false if positions.any? { |nr, nc| nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length }

    # Check if we can find the "X-MAS" pattern in the forward direction
    if grid[m1[0]][m1[1]] == 'M' && grid[a[0]][a[1]] == 'A' && grid[s1[0]][s1[1]] == 'S' &&
       grid[s2[0]][s2[1]] == 'A' && grid[m2[0]][m2[1]] == 'M'
      return true
    end

    # Check if we can find the "X-MAS" pattern in the backward direction
    if grid[m1[0]][m1[1]] == 'M' && grid[a[0]][a[1]] == 'S' && grid[s1[0]][s1[1]] == 'A' &&
       grid[s2[0]][s2[1]] == 'S' && grid[m2[0]][m2[1]] == 'M'
      return true
    end

    false
  end

  # Iterate over each cell in the grid
  grid.each_with_index do |row, r|
    row.each_char.with_index do |_, c|
      # Check all directions
      directions.each do |dr, dc|
        if can_find_xmas_xmas?(grid, r, c, dr, dc)
          count += 1
        end
      end
    end
  end

  count
end

# Read the input grid from the file input.txt
input_grid = File.readlines("input.txt").map(&:chomp)

# Call the function and print the result
result = count_xmas_xmas_occurrences(input_grid)
puts "The X-MAS pattern appears #{result} times."
