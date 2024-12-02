'''''
Hard: (7 points)

3. Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.


Time Complexity: O(n)
Explanation: Both np.max and np.min functions iterate through the array once, each taking O(n) time.
Therefore, the overall time complexity is O(n) since we're performing two independent O(n) operations.

''''

import numpy as np
array = np.random.randint(low=0, high=10, size=10)
print("Our array:", array) # Generated out array like before

def max_difference(array):
    if len(array) < 2:
        return None  # Handle case where there aren't enough elements
    max_val = np.max(array)  # Find the maximum value in the array
    min_val = np.min(array)  # Find the minimum value in the array
    return max_val - min_val  # Return the maximum difference

print('Maximum Difference in Our Array:', max_difference(array))


## Output:
# Maximum Difference in Our Array: 
