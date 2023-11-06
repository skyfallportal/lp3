# Define a function to solve the 0/1 Knapsack Problem.
def solve_knapsack():
    # Define the values and weights of items.
    val = [50, 100, 150, 200]  # Value array
    wt = [8, 16, 32, 40]      # Weight array
    W = 64                     # Knapsack capacity
    n = len(val) - 1           # Number of items (index of the last item)

    # Define a recursive function for the knapsack problem.
    def knapsack(W, n):
        # Base case: If there are no more items or the remaining capacity is zero, return zero.
        if n < 0 or W <= 0:
            return 0
        
        # If the weight of the current item is greater than the remaining capacity, skip it.
        if wt[n] > W:
            return knapsack(W, n - 1)
        else:
            # Calculate the maximum value by either including or excluding the current item.
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
            # max(including the current item, excluding the current item)

    # Call the knapsack function with the given capacity and the index of the last item.
    print(knapsack(W, n))

# Entry point of the program.
if __name__ == "__main__":
    # Call the solve_knapsack function to solve the knapsack problem and print the result.
    solve_knapsack()

'''
This code solves the 0/1 Knapsack Problem using a recursive approach. The 0/1 Knapsack Problem is a classic optimization problem where you have a set of items with values and weights, and you need to select a combination of items to maximize the total value while not exceeding a given weight constraint. Here's the code with comments:

Explanation of the concept used in this code:
- The code implements the 0/1 Knapsack Problem using a recursive function `knapsack(W, n)` that returns the maximum value that can be obtained with a remaining capacity `W` and by considering the first `n` items.

- The base cases are when there are no more items to consider (`n < 0`) or when the remaining capacity is zero (`W <= 0`), in which case the function returns zero.

- If the weight of the current item is greater than the remaining capacity (`wt[n] > W`), it's not considered, and the function is called recursively without including it.

- Otherwise, the function calculates the maximum value by considering two options:
  - Including the current item: Adding the value of the current item to the result and calling the function recursively with the remaining capacity and one less item (`val[n] + knapsack(W - wt[n], n - 1)`).
  - Excluding the current item: Calling the function recursively with the same capacity and one less item (`knapsack(W, n - 1)`).
  The result is the maximum of these two options.

- The final result, obtained by calling `knapsack(W, n)`, represents the maximum value that can be obtained while respecting the weight constraint of the knapsack.

Here's a formal description of the 0/1 Knapsack Problem:

You are given a set of items, each with an associated value and weight.
You have a knapsack with a limited weight capacity.
Your goal is to select a subset of the items to include in the knapsack in such a way that the total weight of the selected items does not exceed the knapsack's capacity, and the total value of the selected items is maximized.
The name "0/1 Knapsack" comes from the binary choice you have for each item: you can either choose to include the item in the knapsack (denoted as 1) or leave it out (denoted as 0).
'''