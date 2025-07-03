"""
BINARY SEARCH ALGORITHM
========================
Simple explanation: Look for an item in a SORTED list by repeatedly cutting the list in half.
It's like guessing a number between 1-100 by always guessing the middle and adjusting based on "higher" or "lower".
NOTE: The list MUST be sorted for this to work!
"""

def binary_search(arr, target):
    """
    Search for a target value in a SORTED array by dividing the search space in half each time.
    
    Time complexity: O(log n) - much faster than linear search for large lists
    Space complexity: O(1) - we only use a few variables
    """
    
    # Step 1: Set up boundaries - start and end of our search area
    left = 0  # Start of the list
    right = len(arr) - 1  # End of the list
    
    # Step 2: Keep searching while there's still area to search
    while left <= right:
        
        # Step 3: Find the middle position
        middle = (left + right) // 2  # // means divide and round down
        print(f"Checking middle position {middle}, value: {arr[middle]}")
        
        # Step 4: Check if we found our target
        if arr[middle] == target:
            print(f"Found {target} at position {middle}")
            return middle
        
        # Step 5: If target is smaller, search the left half
        elif arr[middle] > target:
            print(f"{target} is smaller than {arr[middle]}, searching left half")
            right = middle - 1  # Eliminate right half
        
        # Step 6: If target is larger, search the right half
        else:
            print(f"{target} is larger than {arr[middle]}, searching right half")
            left = middle + 1  # Eliminate left half
    
    # Step 7: If we exit the loop, target wasn't found
    print(f"{target} not found in the list")
    return -1

# Example: Let's search in a sorted list
if __name__ == "__main__":
    # Create a SORTED list (very important!)
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 89, 99]
    print("Sorted list:", sorted_numbers)
    print()
    
    # Example 1: Search for a number that exists
    print("Searching for 23:")
    result1 = binary_search(sorted_numbers, 23)
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: Search for a number that doesn't exist
    print("Searching for 50:")
    result2 = binary_search(sorted_numbers, 50) 