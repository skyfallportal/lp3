# Define a function to solve the Fractional Knapsack Problem.
def fractional_knapsack():
    # Define the weights and values of items.
    weights = [10, 20, 30]  # Weight of each item
    values = [60, 100, 120]  # Value of each item
    capacity = 50  # Total capacity of the knapsack
    res = 0  # Initialize the result to 0

    # Pair the weights and values of items and sort them by the value-to-weight ratio in descending order.
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        # If the capacity is exhausted, exit the loop (the bag is fully filled).
        if capacity <= 0:
            break
        # If the weight of the current item exceeds the remaining capacity, take a fraction of it to fill the bag to its limit.
        if pair[0] > capacity:
            # Calculate the value of the fraction to be added to the result.
            res += int(capacity * (pair[1] / pair[0]))
            # Reduce the capacity to zero as the bag is fully filled.
            capacity = 0
        else:  # If the weight of the current item can be accommodated completely.
            # Add the entire item to the bag and update the result.
            res += pair[1]
            # Reduce the available capacity by the weight of the item.
            capacity -= pair[0]

    # Print the maximum value that can be obtained.
    print(res)

# Entry point of the program.
if __name__ == "__main__":
    # Call the fractional_knapsack function to solve the problem and print the result.
    fractional_knapsack()



'''
This code implements the Fractional Knapsack Problem using a greedy algorithm. The Fractional Knapsack Problem involves selecting items from a set with given weights and values to maximize the total value while not exceeding a specified capacity. Here's the code with comments explaining it line by line:


Explanation of the concept used in this code:

- The code implements the Fractional Knapsack Problem using a greedy strategy. It sorts the items based on their value-to-weight ratio in descending order, which means it considers items with the highest value-to-weight ratio first.

- It iterates through the sorted items and, for each item, checks whether it can be fully accommodated in the knapsack (i.e., its weight is less than or equal to the remaining capacity).

- If the item's weight exceeds the remaining capacity, it takes a fraction of the item to fill the bag to its limit, maximizing the value. It calculates the fraction based on the available capacity.

- The result is updated as items are added to the bag, and the available capacity is adjusted accordingly.

- The final result, obtained by calling `fractional_knapsack()`, represents the maximum value that can be obtained by selecting items according to their value-to-weight ratio while respecting the capacity constraint.
'''
'''

The Fractional Knapsack Problem is a classic optimization problem that can be solved using a greedy algorithm. It involves selecting items from a set with given weights and values to maximize the total value while not exceeding a specified capacity (or weight limit). In this problem, unlike the 0/1 Knapsack Problem, you can take fractions of items, which makes it a fractional knapsack problem.

Here's how the Fractional Knapsack Problem is typically described:

- You are given a set of items, each with an associated weight (w_i) and a value (v_i).
- You have a knapsack with a maximum weight capacity (W).
- Your goal is to select a combination of items to place in the knapsack, subject to the constraint that the total weight of the selected items does not exceed the knapsack's capacity, and you want to maximize the total value of the selected items.

The key difference between the Fractional Knapsack Problem and the 0/1 Knapsack Problem is that in the fractional version, you can take fractions of items. This makes it possible to select parts of an item, depending on its value-to-weight ratio.

Here's how the greedy algorithm works to solve the Fractional Knapsack Problem:

1. Calculate the value-to-weight ratio (v_i / w_i) for each item in the set.

2. Sort the items based on their value-to-weight ratio in non-increasing order (highest ratio items first).

3. Initialize the result variable (total value) to zero and the current weight variable (current weight) to zero.

4. Iterate through the sorted items:
   - If adding the entire item to the knapsack doesn't exceed the weight capacity (W):
     - Add the entire item to the knapsack.
     - Update the total value and current weight accordingly.
   - If adding the entire item would exceed the weight capacity, take a fraction of the item to fill the remaining capacity of the knapsack.
     - Calculate the fraction as (W - current weight) / w_i, where w_i is the weight of the current item.
     - Add the fraction of the item to the knapsack.
     - Update the total value proportionally to the fraction taken.
     - The knapsack is now full, so break from the loop.

5. Return the total value, which represents the maximum value that can be obtained from the items selected for the knapsack.

The greedy algorithm works well for the Fractional Knapsack Problem because it always selects items with the highest value-to-weight ratio first. This approach ensures that the knapsack is filled with items that offer the most value for their weight, resulting in an optimal solution. However, it may not work for other variants of the knapsack problem where items cannot be fractionally divided.
'''