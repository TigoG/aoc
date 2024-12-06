from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split("\n")
    
    rules = []
    updates = []
    
    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif line:
            updates.append(list(map(int, line.split(","))))
    
    return rules, updates

def validate_update(ordering_rules, update):
    # Filter rules to only include pages in the current update
    update_set = set(update)
    filtered_rules = [(x, y) for x, y in ordering_rules if x in update_set and y in update_set]
    
    # Build a graph and in-degree count from the filtered rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x, y in filtered_rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree.setdefault(x, 0)  # Ensure all nodes are initialized
    
    # Topological sorting to check for valid order
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if the sorted order matches the update order
    update_index = {page: i for i, page in enumerate(update)}
    for i, page in enumerate(sorted_order):
        if update_index[page] != i:
            return False
    return len(sorted_order) == len(update)

def find_middle_page(update):
    # Middle page is the one at index len(update) // 2
    return update[len(update) // 2]

def main(file_path):
    rules, updates = parse_input(file_path)
    valid_middle_pages = []
    
    for update in updates:
        if validate_update(rules, update):
            valid_middle_pages.append(find_middle_page(update))
    
    result = sum(valid_middle_pages)
    return result

# Example Usage
if __name__ == "__main__":
    file_path = "input.txt"  # Replace with your input file path
    result = main(file_path)
    print(f"Sum of middle pages from correctly ordered updates: {result}")
