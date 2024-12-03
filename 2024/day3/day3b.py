import re

def sum_enabled_mul(input_data):
    # Regex patterns for valid instructions
    mul_regex = r"mul\((\d+),(\d+)\)"
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"

    # Initialize state
    is_enabled = True
    total_sum = 0

    # Process input sequentially
    for match in re.finditer(rf"{mul_regex}|{do_regex}|{dont_regex}", input_data):
        instruction = match.group()

        if re.match(do_regex, instruction):
            # Enable mul instructions
            is_enabled = True
        elif re.match(dont_regex, instruction):
            # Disable mul instructions
            is_enabled = False
        else:
            # Process mul(X,Y) if enabled
            if is_enabled:
                x, y = map(int, re.match(mul_regex, instruction).groups())
                total_sum += x * y

    return total_sum

if __name__ == "__main__":
    # Read input from file
    with open("input.txt", "r") as file:
        input_data = file.read()

    # Compute and print the result
    print(sum_enabled_mul(input_data))