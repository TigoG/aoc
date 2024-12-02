def safe_report?(report)
  # Check if the differences are valid and whether the report is strictly increasing or strictly decreasing
  increasing = true
  decreasing = true

  (0..report.length - 2).each do |i|
    diff = (report[i + 1] - report[i]).abs

    # Check if the difference is within the valid range (1 to 3)
    if diff < 1 || diff > 3
      return false  # If any difference is out of range, the report is unsafe
    end

    # Check if the report is strictly increasing or strictly decreasing
    increasing &&= report[i + 1] > report[i]
    decreasing &&= report[i + 1] < report[i]
  end

  # The report must be either strictly increasing or strictly decreasing
  increasing || decreasing
end

# Read the input file
input_file = 'input.txt'

# Read and process the reports from the file
reports = File.readlines(input_file).map do |line|
  line.split.map(&:to_i)  # Split by space and convert each item to an integer
end

# Count how many reports are safe
safe_reports_count = reports.count { |report| safe_report?(report) }

puts "Number of safe reports: #{safe_reports_count}"
