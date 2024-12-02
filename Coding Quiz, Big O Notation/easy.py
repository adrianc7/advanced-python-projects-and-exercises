'''''
Easy: (3 points)

1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

Time Complexity: O(n)
Explanation: The np.sum function iterates through all the elements in the array exactly once.
Time Complexity Explanation:
Here, n refers to the number of elements in the array, so the time complexity is linear, O(n).
'''' 

import numpy as np
array = np.random.randint(low=0, high=10, size=10)
print(array)
# Our: array: [4 7 2 8 0 3 9 4 1 2]



def array_sum(array):
    total_sum = np.sum(array)
    return total_sum


print('Array Total Sum:', array_sum(array))


## Output:
# Array Total Sum: 45
