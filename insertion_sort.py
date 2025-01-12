"""
========================
INSERTION SORT ALGORITHM
========================
This script implements the insertion sort algorithm to sort a list of numbers in ascending order.

Author: Unique Karanjit
Date: Jan 7, 2025
"""

def insertion_sort(arr):
    """
    Sort the given list based on insertion sort algorithm.

    Parameters:
        arr (list): List of numbers to be sorted.

    Returns:
        list: The sorted list in decreasing order.
    """
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # The current element to be inserted in the sorted portion
        key = arr[i]
        
        # Initialize the variable to find the position for the key in the sorted portion
        j = i - 1
        
        # Shift elements in the sorted portion that are greater than the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key

    return arr


# Main block to demonstrate the insertion sort
if __name__ == "__main__":
    # Example list to sort
    numbers = [12, 11, 13, 5, 6]

    print("Original list:", numbers)

    # Sort the list
    sorted_numbers = insertion_sort(numbers)

    print("Sorted list:", sorted_numbers)

