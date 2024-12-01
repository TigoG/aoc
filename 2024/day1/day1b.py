from collections import Counter

def main():
    print("day 1 - part 2")

    # Read input from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Split lines into two lists
    left_list, right_list = split_list(lines)

    # Convert string lists to integer lists
    left_list = list(map(int, left_list))
    right_list = list(map(int, right_list))

    # Solve Part 1 (Optional: Comment out if not needed)
    part1_total_difference = solve_part1(left_list, right_list)
    print(f"The total difference for part 1 is: {part1_total_difference}")

    # Solve Part 2
    similarity_score = solve_part2(left_list, right_list)
    print(f"The similarity score for part 2 is: {similarity_score}")


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


def solve_part1(left_list, right_list):
    """
    Solve Part 1: Calculate the total difference between sorted lists.
    """
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Ensure the lists have the same length
    assert len(left_list) == len(right_list)

    # Calculate total distance
    total_difference = sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list)))
    return total_difference


def solve_part2(left_list, right_list):
    """
    Solve Part 2: Calculate the similarity score based on frequency counts.
    """
    # Count occurrences of each number in the right list
    right_counter = Counter(right_list)

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counter.get(num, 0)

    return similarity_score


if __name__ == "__main__":
    main()
