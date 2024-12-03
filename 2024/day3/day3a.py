import re

def sum_valid_mul(input_data):
    # Regex to match valid mul(X,Y) patterns
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.findall(regex, input_data)
    
    # Compute the product for each match and sum them
    result = sum(int(x) * int(y) for x, y in matches)
    return result

if __name__ == "__main__":
    # Read input from the file
    with open("input.txt", "r") as file:
        input_data = file.read()
    
    # Compute and print the result
    print(sum_valid_mul(input_data))
