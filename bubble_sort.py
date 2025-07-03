"""
BUBBLE SORT ALGORITHM
====================
Simple explanation: Compare pairs of adjacent items and swap them if they're in wrong order.
Keep doing this until no more swaps are needed. Large items "bubble up" to the end.
It's like sorting cards by repeatedly comparing neighbors and swapping if needed.
"""

def bubble_sort(arr):
    """
    Sort an array by repeatedly comparing adjacent elements and swapping them if needed.
    
    Time complexity: O(n²) - not very efficient for large lists
    Space complexity: O(1) - sorts in place, no extra memory needed
    """
    
    n = len(arr)
    print(f"Starting with: {arr}")
    
    # Step 1: We need to do multiple passes through the list
    for i in range(n):
        
        # Step 2: Track if we made any swaps in this pass
        swapped = False
        print(f"\nPass {i + 1}:")
        
        # Step 3: Go through the unsorted part of the list
        # After each pass, the largest element is in its correct position
        for j in range(0, n - i - 1):
            
            # Step 4: Compare adjacent elements
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")
            
            # Step 5: If they're in wrong order, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Python swap
                swapped = True
                print(f"    Swapped! Now: {arr}")
            else:
                print(f"    No swap needed")
        
        # Step 6: If no swaps were made, the list is sorted
        if not swapped:
            print(f"No swaps in this pass - list is sorted!")
            break
    
    return arr

# Example: Let's sort a list of numbers
if __name__ == "__main__":
    # Create an unsorted list
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", numbers)
    print("="*50)
    
    # Make a copy so we don't change the original
    numbers_copy = numbers.copy()
    
    # Sort the list
    sorted_numbers = bubble_sort(numbers_copy)
    
    print("="*50)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")
    
    print("\n" + "="*30)
    print("Sorting names:")
    names = ["Charlie", "Alice", "Bob", "Diana"]
    print("Original:", names)
    sorted_names = bubble_sort(names.copy())
    print("Sorted:", sorted_names) 