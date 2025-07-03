"""
MERGE SORT ALGORITHM
===================
Simple explanation: Divide the list into halves until you have individual items, 
then merge them back together in sorted order.
It's like organizing two piles of sorted papers into one big sorted pile.
"""

def merge_sort(arr):
    """
    Sort an array using the divide-and-conquer approach.
    
    Time complexity: O(n log n) - much better than O(n²) algorithms
    Space complexity: O(n) - needs extra space for merging
    """
    
    # Step 1: Base case - if list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    print(f"Dividing: {arr}")
    
    # Step 2: Divide the list into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    
    print(f"  Left half: {left_half}")
    print(f"  Right half: {right_half}")
    
    # Step 3: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Step 4: Merge the sorted halves back together
    result = merge(left_sorted, right_sorted)
    print(f"Merged {left_sorted} and {right_sorted} -> {result}")
    
    return result

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """
    
    result = []  # The merged list
    left_index = 0  # Index for left list
    right_index = 0  # Index for right list
    
    # Step 1: Compare elements from both lists and add smaller one to result
    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] <= right[right_index]:
            # Left element is smaller or equal, add it to result
            result.append(left[left_index])
            left_index += 1
        else:
            # Right element is smaller, add it to result
            result.append(right[right_index])
            right_index += 1
    
    # Step 2: Add any remaining elements from left list
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    
    # Step 3: Add any remaining elements from right list
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    
    return result

# Example: Let's sort a list of numbers
if __name__ == "__main__":
    # Create an unsorted list
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", numbers)
    print("="*60)
    
    # Sort the list
    sorted_numbers = merge_sort(numbers.copy())
    
    print("="*60)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")
    
    print("\n" + "="*30)
    print("Sorting words:")
    words = ["banana", "apple", "cherry", "date", "elderberry"]
    print("Original:", words)
    sorted_words = merge_sort(words.copy())
    print("Final sorted:", sorted_words) 