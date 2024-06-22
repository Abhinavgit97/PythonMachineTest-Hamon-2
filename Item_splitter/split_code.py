import math
import random


def split_items(items, ratios):
    # Check if the item list and ratio list are not empty
    if not items or not ratios:
        return "Error: Item list and ratio list should not be empty"

    # Check if all ratios are positive
    if any(r <= 0 for r in ratios):
        return "Error: Ratios should be positive numbers"

    # Check if the ratios sum is approximately 1 using math.isclose
    if not math.isclose(sum(ratios), 1, rel_tol=1e-3):
        return "Error: Ratios must sum to 1"

    # Shuffle the items randomly
    random.shuffle(items)

    # Calculate the total number of items
    total_items = len(items)

    # Initialize list to store the final items
    split_lists = []
    start_index = 0

    # Iterating over the ratios
    for ratio in ratios:

        part_length = int(ratio * total_items)

        split_lists.append(items[start_index : start_index + part_length])
        start_index += part_length

    return split_lists


if __name__ == "__main__":
    # Example usage
    items = [1, 2, 3, 4, 5, 6, 10]
    ratios = [0.5, 0.3, 0.2]
    result = split_items(items, ratios)
    print(result)
