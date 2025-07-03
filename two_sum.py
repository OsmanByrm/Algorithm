"""
TWO SUM ALGORITHM
================
Simple explanation: Find two numbers in a list that add up to a target number.
Return the positions (indices) of these two numbers.
It's like having a shopping list with prices and finding two items that cost exactly $20 together.
"""

def two_sum_brute_force(arr, target):
    """
    Find two numbers that add up to target using brute force approach.
    
    Time complexity: O(n²) - we check every possible pair
    Space complexity: O(1) - only use a few variables
    """
    
    print(f"Looking for two numbers that add up to {target}")
    print(f"Array: {arr}")
    print("Brute force approach - checking every possible pair:")
    
    # Step 1: Try every possible pair of numbers
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Start from i+1 to avoid using same number twice
            
            # Step 2: Check if current pair adds up to target
            current_sum = arr[i] + arr[j]
            print(f"  Checking: {arr[i]} + {arr[j]} = {current_sum}")
            
            if current_sum == target:
                # Step 3: Found the pair! Return their positions
                print(f"  ✓ Found it! {arr[i]} at index {i} + {arr[j]} at index {j} = {target}")
                return [i, j]
    
    # Step 4: No pair found
    print(f"  No two numbers add up to {target}")
    return []

def two_sum_hash_map(arr, target):
    """
    Find two numbers that add up to target using hash map (much faster).
    
    Time complexity: O(n) - we only go through the list once
    Space complexity: O(n) - we store numbers in a hash map
    """
    
    print(f"Looking for two numbers that add up to {target}")
    print(f"Array: {arr}")
    print("Hash map approach - much faster:")
    
    # Step 1: Create a hash map to store numbers and their positions
    seen_numbers = {}  # Dictionary: {number: index}
    
    # Step 2: Go through each number in the list
    for i, current_number in enumerate(arr):
        
        # Step 3: Calculate what number we need to reach the target
        needed_number = target - current_number
        print(f"  Position {i}: {current_number}, need {needed_number} to reach {target}")
        
        # Step 4: Check if we've seen the needed number before
        if needed_number in seen_numbers:
            # Step 5: Found the pair! Return their positions
            previous_index = seen_numbers[needed_number]
            print(f"  ✓ Found it! {arr[previous_index]} at index {previous_index} + {current_number} at index {i} = {target}")
            return [previous_index, i]
        
        # Step 6: Remember this number and its position for future checks
        seen_numbers[current_number] = i
        print(f"    Remembering: {current_number} is at position {i}")
    
    # Step 7: No pair found
    print(f"  No two numbers add up to {target}")
    return []

def two_sum_all_pairs(arr, target):
    """
    Find ALL pairs of numbers that add up to target (not just the first one).
    """
    
    print(f"Finding ALL pairs that add up to {target}")
    print(f"Array: {arr}")
    
    pairs = []
    
    # Check every possible pair
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append([i, j])
                print(f"  Found pair: {arr[i]} (index {i}) + {arr[j]} (index {j}) = {target}")
    
    if not pairs:
        print(f"  No pairs found that add up to {target}")
    
    return pairs

# Example: Let's find pairs that add up to different targets
if __name__ == "__main__":
    print("TWO SUM ALGORITHM")
    print("="*60)
    
    # Example 1: Basic example with brute force
    numbers = [2, 7, 11, 15]
    target = 9
    print("Example 1: Brute Force Method")
    result1 = two_sum_brute_force(numbers, target)
    print(f"Result: {result1}")
    
    print("\n" + "="*60)
    
    # Example 2: Same example with hash map (faster)
    print("Example 2: Hash Map Method (faster)")
    result2 = two_sum_hash_map(numbers, target)
    print(f"Result: {result2}")
    
    print("\n" + "="*60)
    
    # Example 3: Finding all pairs
    numbers_with_duplicates = [1, 2, 3, 4, 5, 6, 4, 3]
    target = 7
    print("Example 3: Finding ALL pairs")
    all_pairs = two_sum_all_pairs(numbers_with_duplicates, target)
    print(f"All pairs that sum to {target}: {all_pairs}")
    
    print("\n" + "="*60)
    
    # Example 4: Real-world scenario
    print("Example 4: Real-world scenario")
    print("Shopping: Find two items that cost exactly $50 together")
    prices = [25, 30, 15, 35, 20, 45]
    item_names = ["Shirt", "Jeans", "Socks", "Jacket", "Hat", "Shoes"]
    target_budget = 50
    
    print(f"Items and prices: {list(zip(item_names, prices))}")
    result = two_sum_hash_map(prices, target_budget)
    
    if result:
        item1, item2 = result
        print(f"You can buy: {item_names[item1]} (${prices[item1]}) + {item_names[item2]} (${prices[item2]}) = ${target_budget}")
    else:
        print("No two items cost exactly $50 together") 