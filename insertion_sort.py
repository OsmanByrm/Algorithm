"""
INSERTION SORT ALGORITHM
========================
Simple explanation: Take each item and insert it into the correct position among the already sorted items.
It's like organizing playing cards in your hand - you pick up each new card and slide it into the right spot.
"""

def insertion_sort(arr):
    """
    Sort an array by building a sorted portion one element at a time.
    
    Time complexity: O(n²) worst case, but O(n) for nearly sorted arrays
    Space complexity: O(1) - sorts in place
    """
    
    print(f"Starting with: {arr}")
    
    # Step 1: Start from the second element (index 1)
    # The first element is already "sorted" by itself
    for i in range(1, len(arr)):
        
        # Step 2: Take the current element to be inserted
        current_element = arr[i]
        print(f"\nStep {i}: Inserting {current_element} into sorted portion")
        print(f"  Sorted portion so far: {arr[:i]}")
        print(f"  Element to insert: {current_element}")
        
        # Step 3: Find the correct position for current element
        # Start from the position just before current element
        j = i - 1
        
        # Step 4: Move elements that are larger than current_element to the right
        while j >= 0 and arr[j] > current_element:
            print(f"    {arr[j]} > {current_element}, so moving {arr[j]} to the right")
            arr[j + 1] = arr[j]  # Move element one position to the right
            j -= 1  # Check the next element to the left
        
        # Step 5: Insert current element at the correct position
        arr[j + 1] = current_element
        print(f"    Inserting {current_element} at position {j + 1}")
        print(f"  After insertion: {arr}")
    
    return arr

# Example: Let's sort a list of numbers
if __name__ == "__main__":
    # Create an unsorted list
    numbers = [5, 2, 4, 6, 1, 3]
    print("Original list:", numbers)
    print("="*50)
    
    # Make a copy so we don't change the original
    numbers_copy = numbers.copy()
    
    # Sort the list
    sorted_numbers = insertion_sort(numbers_copy)
    
    print("="*50)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")
    
    print("\n" + "="*30)
    print("Sorting student grades:")
    grades = [85, 92, 78, 96, 88]
    print("Original grades:", grades)
    sorted_grades = insertion_sort(grades.copy())
    print("Sorted grades:", sorted_grades) 