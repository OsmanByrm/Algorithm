"""
FACTORIAL ALGORITHM
==================
Simple explanation: Multiply a number by all the smaller positive numbers.
factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
It's used to count the number of ways to arrange things.
Example: How many ways can 3 people sit in 3 chairs? 3! = 6 ways
"""

def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Time complexity: O(n) - we calculate n numbers
    Space complexity: O(n) - recursion stack grows with n
    """
    
    print(f"Calculating factorial({n})")
    
    # Step 1: Base case - factorial of 0 and 1 is 1
    if n <= 1:
        print(f"  factorial({n}) = 1 (base case)")
        return 1
    
    # Step 2: Recursive case - n! = n × (n-1)!
    print(f"  factorial({n}) = {n} × factorial({n-1})")
    result = n * factorial_recursive(n - 1)
    print(f"  factorial({n}) = {result}")
    return result

def factorial_iterative(n):
    """
    Calculate factorial using iteration (more efficient).
    
    Time complexity: O(n) - same as recursive
    Space complexity: O(1) - only uses one variable
    """
    
    print(f"Calculating factorial({n}) iteratively:")
    
    # Step 1: Handle base case
    if n <= 1:
        print(f"  factorial({n}) = 1 (base case)")
        return 1
    
    # Step 2: Start with 1 and multiply by each number up to n
    result = 1
    print(f"  Starting with result = 1")
    
    for i in range(2, n + 1):
        # Step 3: Multiply result by current number
        result = result * i
        print(f"  Step {i-1}: result = result × {i} = {result}")
    
    return result

def factorial_with_list_visualization(n):
    """
    Calculate factorial and show the multiplication as a list.
    """
    
    print(f"Factorial({n}) breakdown:")
    
    if n <= 1:
        return 1
    
    # Step 1: Create list of numbers from n down to 1
    numbers = list(range(n, 0, -1))  # [n, n-1, n-2, ..., 2, 1]
    print(f"  Numbers to multiply: {numbers}")
    
    # Step 2: Show the multiplication step by step
    result = 1
    multiplication_steps = []
    
    for number in numbers:
        result *= number
        multiplication_steps.append(str(number))
        print(f"    {' × '.join(multiplication_steps)} = {result}")
    
    return result

def permutations_example(n, r):
    """
    Show how factorial is used to calculate permutations (arrangements).
    P(n,r) = n! / (n-r)! = number of ways to arrange r items from n items
    """
    
    print(f"Permutations: How many ways to arrange {r} items from {n} items?")
    
    n_factorial = factorial_iterative(n)
    nr_factorial = factorial_iterative(n - r)
    
    result = n_factorial // nr_factorial  # Use // for integer division
    
    print(f"  P({n},{r}) = {n}! / ({n}-{r})! = {n_factorial} / {nr_factorial} = {result}")
    return result

# Example: Let's calculate some factorials
if __name__ == "__main__":
    print("FACTORIAL NUMBERS")
    print("="*50)
    
    # Example 1: Calculate factorial using recursion
    print("Example 1: Recursive method")
    result = factorial_recursive(5)
    print(f"5! = {result}")
    
    print("\n" + "="*50)
    
    # Example 2: Calculate factorial using iteration
    print("Example 2: Iterative method (more efficient)")
    result = factorial_iterative(6)
    print(f"6! = {result}")
    
    print("\n" + "="*50)
    
    # Example 3: Visual breakdown
    print("Example 3: Visual breakdown")
    result = factorial_with_list_visualization(4)
    print(f"Final result: 4! = {result}")
    
    print("\n" + "="*50)
    
    # Example 4: Real-world application - permutations
    print("Example 4: Real-world application")
    print("How many ways can 5 students line up in a row?")
    lineup_ways = factorial_iterative(5)
    print(f"Answer: 5! = {lineup_ways} ways")
    
    print("\nHow many ways to choose and arrange 3 students from 8 students?")
    arrangement_ways = permutations_example(8, 3)
    print(f"Answer: {arrangement_ways} ways") 