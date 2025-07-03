"""
LINEAR SEARCH ALGORITHM
=======================
Simple explanation: Look through each item in a list one by one until you find what you're looking for.
It's like looking for a book on a shelf by checking each book from left to right.
"""

def linear_search(arr, target):
    """
    Search for a target value in an array by checking each element one by one.
    
    Time complexity: O(n) - worst case we check every element
    Space complexity: O(1) - we only use a few variables
    """
    
    # Step 1: Start from the beginning of the list
    for i in range(len(arr)):
        
        # Step 2: Check if current element matches what we're looking for
        if arr[i] == target:
            # Step 3: If found, return the position (index)
            print(f"Found {target} at position {i}")
            return i
    
    # Step 4: If we've checked all elements and didn't find it
    print(f"{target} not found in the list")
    return -1  # Return -1 to indicate not found

# Example: Let's search in a list of numbers
if __name__ == "__main__":
    # Create a sample list
    numbers = [10, 25, 3, 47, 8, 15, 92, 6]
    print("List:", numbers)
    print()
    
    # Example 1: Search for a number that exists
    print("Searching for 47:")
    result1 = linear_search(numbers, 47)
    
    print()
    
    # Example 2: Search for a number that doesn't exist
    print("Searching for 100:")
    result2 = linear_search(numbers, 100)
    
    print()
    
    # Example 3: Search in a list of names
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    print("Names list:", names)
    print("Searching for 'Charlie':")
    result3 = linear_search(names, "Charlie") 