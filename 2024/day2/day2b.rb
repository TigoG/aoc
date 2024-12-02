# Check if a report is safe (Part 1 conditions)
def safe_report?(report)
  increasing = true
  decreasing = true

  # Check if the report is strictly increasing or strictly decreasing
  (0..report.length - 2).each do |i|
    diff = (report[i + 1] - report[i]).abs

    # If the difference is out of range (not between 1 and 3), the report is unsafe
    if diff < 1 || diff > 3
      return false
    end

    # Check if the report is strictly increasing or strictly decreasing
    increasing &&= report[i + 1] > report[i]
    decreasing &&= report[i + 1] < report[i]
  end

  # The report must be either strictly increasing or strictly decreasing
  increasing || decreasing
end

# Check if a report can be made safe by removing a single level (Part 2)
def safe_report_with_dampener?(report)
  # First, check if the report is already safe
  return true if safe_report?(report)

  # If not safe, try removing each level one by one
  (0..report.length - 1).each do |i|
    new_report = report[0...i] + report[i+1..-1]
    return true if safe_report?(new_report)  # If removing one level makes it safe, it's considered safe
  end

  false  # If no removal makes it safe, it's still unsafe
end

# Read the input file
input_file = 'input.txt'

# Read and process the reports from the file
reports = File.readlines(input_file).map do |line|
  line.split.map(&:to_i)  # Split by space and convert each item to an integer
end

# Part 1: Count how many reports are safe without modifications
safe_reports_part_1 = reports.count { |report| safe_report?(report) }

# Part 2: Count how many reports are safe with Problem Dampener (by removing one level)
safe_reports_part_2 = reports.count { |report| safe_report_with_dampener?(report) }

puts "Part 1 - Number of safe reports without modification: #{safe_reports_part_1}"
puts "Part 2 - Number of safe reports with Problem Dampener: #{safe_reports_part_2}"
