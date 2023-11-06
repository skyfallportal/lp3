# Define a recursive function to calculate the nth Fibonacci number.
def recursive_fibonacci(n):
    # Base case: If n is 0 or 1, return n.
    if n <= 1:
        return n
    else:
        # Recursive case: Calculate the nth Fibonacci number by summing the (n-1)th and (n-2)th Fibonacci numbers.
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Define a non-recursive function to calculate Fibonacci numbers.
def non_recursive_fibonacci(n):
    # Initialize the first two Fibonacci numbers.
    first = 0
    second = 1
    # Print the first two Fibonacci numbers.
    print(first)
    print(second)
    # Use a while loop to calculate and print the remaining Fibonacci numbers.
    while n - 2 > 0:
        # Calculate the next Fibonacci number by adding the current values of 'first' and 'second'.
        third = first + second
        # Update 'first' and 'second' for the next iteration.
        first = second
        second = third
        # Print the newly calculated Fibonacci number.
        print(third)
        # Decrement 'n' to keep track of how many more Fibonacci numbers need to be generated.

# Entry point of the program.
if __name__ == "__main__":
    # Set the value of 'n' to 10, indicating that you want to calculate the first 10 Fibonacci numbers.
    n = 10
    # Calculate and print the first 10 Fibonacci numbers using the recursive approach.
    for i in range(n):
        print(recursive_fibonacci(i))
    
    # Calculate and print the first 10 Fibonacci numbers using the non-recursive approach.
    non_recursive_fibonacci(n)
