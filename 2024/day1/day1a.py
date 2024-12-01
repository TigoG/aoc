def main():
    print("day 1 - part 1")

    # Read input from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Split lines into two lists
    left_list, right_list = split_list(lines)

    # Convert string lists to integer lists
    left_list = list(map(int, left_list))
    right_list = list(map(int, right_list))

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Ensure the lists have the same length
    assert len(left_list) == len(right_list)

    # Calculate total distance
    total_distance = sum(get_difference(left_list[i], right_list[i]) for i in range(len(left_list)))

    print(f"The total difference for part 1 is: {total_distance}")


def split_list(lines):
    """
    Splits a list of strings into two lists of strings,
    separated by whitespace.
    """
    left_list = []
    right_list = []

    for line in lines:
        numbers = line.split()
        left_list.append(numbers[0])
        right_list.append(numbers[1])

    return left_list, right_list


def get_difference(a, b):
    """
    Returns the absolute difference between two integers.
    """
    return abs(a - b)


if __name__ == "__main__":
    main()
