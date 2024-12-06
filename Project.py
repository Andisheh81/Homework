import itertools
import time
import random

def all_subsets(nums):
    subsets = []
    for r in range(1, len(nums) + 1):
        subsets.extend(itertools.combinations(nums, r))  # Find combinations of length r
    return subsets

def find_max_subset(acts, starts, ends):
    """
    Finds the largest subset of activities such that no two activities overlap.

    Parameters:
    acts (list): List of activity identifiers.
    starts (list): List of start times corresponding to activities.
    ends (list): List of finish times corresponding to activities.

    Returns:
    list: Indices of the activities in the maximum non-overlapping subset.
    """
    best_subset = []  # To store the largest valid subset found
    subsets = all_subsets(acts)  # Generate all possible subsets

    for subset in subsets:
        valid = True  # Flag to check if the current subset is valid
        sorted_subset = sorted(subset, key=lambda x: ends[x - 1])  # Sort subset by finish times

        # Check for overlaps in the sorted subset
        for i in range(len(sorted_subset) - 1):
            if ends[sorted_subset[i] - 1] > starts[sorted_subset[i + 1] - 1]:
                valid = False
                break

        # Update best_subset if the current subset is valid and longer than the current best_subset
        if valid and len(sorted_subset) > len(best_subset):
            best_subset = sorted_subset

    return best_subset

# Generate random data for runtime measurement
N = 10 # Number of activities
activities = list(range(1, N + 1))  # Activity identifiers (1-based index)
start_times = [random.randint(1,100) for _ in range(N)]  # Random start times
finish_times = [start_times[i] + random.randint(1, 10) for i in range(N)]  # Finish times slightly after start times

# Measure execution time of the algorithm
start_time = time.time()  # Record start time
solution = find_max_subset(activities, start_times, finish_times)  # Find the solution
end_time = time.time()  # Record end time

# Sort the solution subset for readability
sorted_solution = sorted(solution)

# Display the results
print("Activities:", activities)
print("Start Times:", start_times)
print("Finish Times:", finish_times)
if solution:
    print("Maximum Non-Overlapping Subset:", sorted_solution)
    print("Length of Non-Overlapping Subset:", len(sorted_solution))
else:
    print("No valid subset found.")
print("Running Time:", (end_time - start_time) * 1e6, "microseconds")
