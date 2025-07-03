"""
FIBONACCI ALGORITHM
==================
Simple explanation: A sequence where each number is the sum of the two numbers before it.
It starts with 0, 1, then each next number is: previous number + number before that.
Example: 0, 1, 1, 2, 3, 5, 8, 13, 21...
It appears in nature - like flower petals, pinecones, and seashells!
"""

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Time complexity: O(2^n) - very slow for large numbers
    Space complexity: O(n) - due to recursion stack
    """
    
    print(f"Calculating fibonacci({n})")
    
    # Step 1: Base cases - the first two Fibonacci numbers
    if n <= 0:
        print(f"  fibonacci(0) = 0")
        return 0
    elif n == 1:
        print(f"  fibonacci(1) = 1")
        return 1
    
    # Step 2: For other numbers, add the two previous Fibonacci numbers
    print(f"  fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2})")
    result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    print(f"  fibonacci({n}) = {result}")
    return result

def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using iteration (much faster).
    
    Time complexity: O(n) - much better!
    Space complexity: O(1) - only uses a few variables
    """
    
    print(f"Calculating fibonacci({n}) iteratively:")
    
    # Step 1: Handle base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Step 2: Start with the first two Fibonacci numbers
    prev_prev = 0  # fibonacci(0)
    prev = 1       # fibonacci(1)
    
    print(f"  Starting: fibonacci(0) = {prev_prev}, fibonacci(1) = {prev}")
    
    # Step 3: Calculate each Fibonacci number up to n
    for i in range(2, n + 1):
        # Step 4: Current Fibonacci number = sum of previous two
        current = prev + prev_prev
        print(f"  fibonacci({i}) = {prev} + {prev_prev} = {current}")
        
        # Step 5: Move forward - what was "previous" becomes "previous previous"
        prev_prev = prev
        prev = current
    
    return prev

def fibonacci_sequence(count):
    """
    Generate a list of the first 'count' Fibonacci numbers.
    """
    
    print(f"Generating first {count} Fibonacci numbers:")
    
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    # Start with the first two numbers
    sequence = [0, 1]
    
    # Generate the rest
    for i in range(2, count):
        next_fib = sequence[i-1] + sequence[i-2]
        sequence.append(next_fib)
        print(f"  fibonacci({i}) = {sequence[i-1]} + {sequence[i-2]} = {next_fib}")
    
    return sequence

# Example: Let's calculate some Fibonacci numbers
if __name__ == "__main__":
    print("FIBONACCI NUMBERS")
    print("="*50)
    
    # Example 1: Calculate single Fibonacci number (small number for recursion)
    print("Example 1: Recursive method (slow but shows the concept)")
    result = fibonacci_recursive(6)
    print(f"fibonacci(6) = {result}")
    
    print("\n" + "="*50)
    
    # Example 2: Calculate single Fibonacci number (iterative - faster)
    print("Example 2: Iterative method (fast)")
    result = fibonacci_iterative(10)
    print(f"fibonacci(10) = {result}")
    
    print("\n" + "="*50)
    
    # Example 3: Generate a sequence of Fibonacci numbers
    print("Example 3: First 12 Fibonacci numbers")
    fib_sequence = fibonacci_sequence(12)
    print(f"Sequence: {fib_sequence}")
    
    print("\n" + "="*30)
    print("Fun fact: Fibonacci numbers appear in nature!")
    print("- Number of petals on flowers")
    print("- Spiral patterns in pinecones and sunflowers")  
    print("- Branching patterns in trees") 