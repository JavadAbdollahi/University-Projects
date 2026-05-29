import random
import time
import sys

# Set the number of elements in the list (you can change this)
num_elements = 30000

# Set how many elements to show before and after sorting (you can change this)
display_count = 10

# Increase the maximum recursion depth limit (needed for large lists)
sys.setrecursionlimit(100000000)

# A dictionary to store the time taken for sorting each list with different pivot options
sorting_times = {}

# Function to record and print the time taken for sorting each list
def record_time(list_name, pivot_choice, time_taken):
    if list_name not in sorting_times:
        sorting_times[list_name] = {}
    sorting_times[list_name][pivot_choice] = time_taken

# The quick sort function with different pivot choices
def quick_sort(arr, pivot_choice='middle'):
    if len(arr) <= 1:  # If the list has 1 or 0 elements, it's already sorted
        return arr
    else:
        # Choose the pivot element based on the selected pivot option
        if pivot_choice == 'first':  # Pivot is the first element
            pivot = arr[0]
        elif pivot_choice == 'last':  # Pivot is the last element
            pivot = arr[-1]
        elif pivot_choice == 'random':  # Pivot is a random element
            pivot = random.choice(arr)
        elif pivot_choice == 'median_of_three':  # Pivot is the median of the first, middle, and last elements
            first = arr[0]
            middle = arr[len(arr) // 2]
            last = arr[-1]
            pivot = sorted([first, middle, last])[1]  # Get the middle value
        else:  # Default: pivot is the middle element
            pivot = arr[len(arr) // 2]

        # Split the list into smaller, equal, and larger parts based on the pivot
        left, middle, right = [], [], []

        # Loop through the list and divide it based on the pivot
        for x in arr:
            if x < pivot:
                left.append(x)  # Elements smaller than pivot go to the left
            elif x > pivot:
                right.append(x)  # Elements larger than pivot go to the right
            else:
                middle.append(x)  # Elements equal to pivot go to the middle

        # Recursively sort the left and right parts and join everything together
        return quick_sort(left, pivot_choice) + middle + quick_sort(right, pivot_choice)

# Function to create lists: sorted, reversed, worst case for middle pivot, worst case for median pivot, and random list
def create_lists(size):
    sorted_list = list(range(1, size + 1))  # Create a sorted list from 1 to size
    reversed_list = sorted_list[::-1]  # Reverse the sorted list to make it descending
    random_list = random.sample(range(1, size + 1), size)  # Create a random shuffled list
    worst_case_middle_list = sorted_list[size//2:] + sorted_list[:size//2]  # Worst case for middle pivot
    worst_case_median_list = list(range(1, size, 4)) + list(range(size, 1, -4)) + list(range(2, size, 4)) + list(range(size-1, 1, -4))
    return sorted_list, reversed_list, worst_case_middle_list, worst_case_median_list, random_list

# Function to sort and display the time and result for each list
def sort_and_show(arr, pivot_choice, list_name, display_count):
    # Start measuring the time before sorting
    start_time = time.time()
    
    # Sort the list using the selected pivot
    sorted_arr = quick_sort(arr, pivot_choice=pivot_choice)
    
    # End measuring the time after sorting
    end_time = time.time()
    
    # Calculate how much time it took to sort the list
    time_taken = end_time - start_time
    
    # Record the time taken for comparison later
    record_time(list_name, pivot_choice, time_taken)
    
    # Show the result and time taken
    print(f"\n-------------------- {list_name} Sorted with '{pivot_choice}' Pivot --------------------")
    print(f"Sorting took: {time_taken:.6f} seconds\n")

    # Show the first, middle, and last few elements after sorting
    print(f"First {display_count} elements after sorting:")
    print(sorted_arr[:display_count])
    
    print(f"\nMiddle {display_count} elements after sorting:")
    print(sorted_arr[(len(sorted_arr)//2 - display_count//2):(len(sorted_arr)//2 + display_count//2)])
    
    print(f"\nLast {display_count} elements after sorting:")
    print(sorted_arr[-display_count:])
    print("--------------------------------------------------------------\n")

# Function to print all the sorting times for comparison
def show_all_sorting_times():
    print("\nAll sorting times for each list and pivot choice:")
    print("--------------------------------------------------------------")
    for list_name, pivots in sorting_times.items():
        print(f"\n{list_name}:")
        for pivot_choice, time_taken in pivots.items():
            print(f"  Pivot choice '{pivot_choice}': {time_taken:.6f} seconds")
    print("--------------------------------------------------------------")

# Create the lists: sorted, reversed, worst-case, and random
sorted_list, reversed_list, worst_case_middle_list, worst_case_median_list, random_list = create_lists(num_elements)

# Display the initial states of the lists before sorting
print(f"\nInitial states of the lists {num_elements} (only showing first, middle, and last {display_count} elements):")
print("--------------------------------------------------------------")

# List of lists to display
lists = [
    ('Sorted List', sorted_list),
    ('Reversed List', reversed_list),
    ('Worst Case for Middle Pivot', worst_case_middle_list),
    ('Worst Case for Median Pivot', worst_case_median_list),
    ('Random List', random_list)
]

# Loop through the lists and display their initial states
for list_name, arr in lists:
    print(f"{list_name} (Initial state):")
    print(f"First {display_count} elements:", arr[:display_count])
    print(f"Middle {display_count} elements:", arr[(len(arr)//2 - display_count//2):(len(arr)//2 + display_count//2)])
    print(f"Last {display_count} elements:", arr[-display_count:])
    print("--------------------------------------------------------------")

# Test sorting for each list using different pivot choices
print("\nTesting sorting for each list with different pivot choices:")
pivot_choices = ['first', 'middle', 'last', 'random', 'median_of_three']

# Perform sorting for each pivot choice
for pivot in pivot_choices:
    print(f"\nTesting sorting with '{pivot}' pivot for all lists:")
    for list_name, arr in lists:
        sort_and_show(arr, pivot, list_name, display_count)

# Finally, display all the recorded sorting times for comparison
show_all_sorting_times()
