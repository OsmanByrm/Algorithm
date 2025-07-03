"""
SELECTION SORT ALGORITHM
=======================
Simple explanation: Find the smallest item in the list and put it at the beginning.
Then find the next smallest and put it in the second position. Repeat until done.
It's like organizing your bookshelf by always picking the thinnest remaining book first.
"""

def selection_sort(arr):
    """
    Sort an array by repeatedly finding the minimum element and placing it at the beginning.
    
    Time complexity: O(n²) - similar to bubble sort
    Space complexity: O(1) - sorts in place
    """
    
    n = len(arr)
    print(f"Starting with: {arr}")
    
    # Step 1: Go through each position in the list
    for i in range(n):
        
        print(f"\nStep {i + 1}: Finding smallest element for position {i}")
        
        # Step 2: Assume current element is the smallest
        min_index = i
        print(f"  Currently assuming {arr[i]} at position {i} is smallest")
        
        # Step 3: Look through the rest of the list to find smaller element
        for j in range(i + 1, n):
            print(f"    Checking {arr[j]} at position {j}")
            
            # Step 4: If we find a smaller element, remember its position
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"      Found smaller! New smallest: {arr[j]} at position {j}")
        
        # Step 5: If we found a smaller element, swap it to the current position
        if min_index != i:
            print(f"  Swapping {arr[i]} with {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print(f"  {arr[i]} is already in correct position")
        
        print(f"  After step {i + 1}: {arr}")
    
    return arr

# Example: Let's sort a list of numbers
if __name__ == "__main__":
    # Create an unsorted list
    numbers = [29, 10, 14, 37, 13]
    print("Original list:", numbers)
    print("="*50)
    
    # Make a copy so we don't change the original
    numbers_copy = numbers.copy()
    
    # Sort the list
    sorted_numbers = selection_sort(numbers_copy)
    
    print("="*50)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")
    
    print("\n" + "="*30)
    print("Sorting fruits by alphabetical order:")
    fruits = ["banana", "apple", "cherry", "date"]
    print("Original:", fruits)
    sorted_fruits = selection_sort(fruits.copy())
    print("Sorted:", sorted_fruits) 