def count_xmas_occurrences(grid)
  rows = grid.length
  cols = grid[0].length
  word = "XMAS"
  word_length = word.length
  count = 0

  # Define directions for horizontal, vertical, and diagonal checks
  directions = [
    [0, 1],  # Right
    [0, -1], # Left
    [1, 0],  # Down
    [-1, 0], # Up
    [1, 1],  # Diagonal down-right
    [1, -1], # Diagonal down-left
    [-1, 1], # Diagonal up-right
    [-1, -1] # Diagonal up-left
  ]

  # Function to check if "XMAS" can be found starting at (r, c) in a given direction
  def can_find_word?(grid, word, r, c, dr, dc)
    word.each_char.with_index do |char, idx|
      nr = r + dr * idx
      nc = c + dc * idx
      # Check if we're within bounds and match the character
      return false if nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length || grid[nr][nc] != char
    end
    true
  end

  # Iterate over each cell in the grid
  grid.each_with_index do |row, r|
    row.each_char.with_index do |_, c|
      # Check all directions
      directions.each do |dr, dc|
        if can_find_word?(grid, word, r, c, dr, dc)
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
result = count_xmas_occurrences(input_grid)
puts "The word 'XMAS' appears #{result} times."
