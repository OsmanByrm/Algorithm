"""
QUICK SORT ALGORITHM
===================
Simple explanation: Pick a "pivot" element, put all smaller elements to its left 
and all larger elements to its right. Then repeat for both sides.
It's like organizing people by height - pick someone, put shorter people on left, taller on right.
"""

def quick_sort(arr, low=0, high=None):
    """
    Sort an array using the quick sort algorithm.
    
    Time complexity: O(n log n) average case, O(n²) worst case
    Space complexity: O(log n) for recursion stack
    """
    
    # Set high to last index if not provided
    if high is None:
        high = len(arr) - 1
        print(f"Starting Quick Sort with: {arr}")
    
    # Step 1: Base case - if we have 1 or 0 elements, nothing to sort
    if low < high:
        
        # Step 2: Partition the array and get the pivot position
        # After partitioning, pivot will be in its correct final position
        pivot_index = partition(arr, low, high)
        
        print(f"After partitioning around pivot {arr[pivot_index]}:")
        print(f"  Array: {arr}")
        print(f"  Elements {arr[low:pivot_index]} are <= {arr[pivot_index]}")
        print(f"  Elements {arr[pivot_index+1:high+1]} are >= {arr[pivot_index]}")
        
        # Step 3: Recursively sort elements before and after partition
        print(f"Sorting left side: {arr[low:pivot_index]}")
        quick_sort(arr, low, pivot_index - 1)
        
        print(f"Sorting right side: {arr[pivot_index+1:high+1]}")
        quick_sort(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Partition the array around a pivot element.
    Put all smaller elements to the left, larger elements to the right.
    """
    
    # Step 1: Choose the last element as pivot
    pivot = arr[high]
    print(f"\nPartitioning {arr[low:high+1]} with pivot {pivot}")
    
    # Step 2: Index of smaller element (where next smaller element should go)
    i = low - 1
    
    # Step 3: Go through all elements except the pivot
    for j in range(low, high):
        
        print(f"  Comparing {arr[j]} with pivot {pivot}")
        
        # Step 4: If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            print(f"    {arr[j]} <= {pivot}, swapping to position {i}")
            print(f"    Array now: {arr}")
        else:
            print(f"    {arr[j]} > {pivot}, leaving in place")
    
    # Step 5: Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"  Placing pivot {pivot} at position {i + 1}")
    print(f"  Final partition: {arr}")
    
    # Return the position of pivot
    return i + 1

# Example: Let's sort a list of numbers
if __name__ == "__main__":
    # Create an unsorted list
    numbers = [10, 7, 8, 9, 1, 5]
    print("Original list:", numbers)
    print("="*60)
    
    # Sort the list
    sorted_numbers = quick_sort(numbers.copy())
    
    print("="*60)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")
    
    print("\n" + "="*30)
    print("Sorting ages:")
    ages = [25, 18, 35, 22, 28]
    print("Original ages:", ages)
    sorted_ages = quick_sort(ages.copy())
    print("Final sorted ages:", sorted_ages) 