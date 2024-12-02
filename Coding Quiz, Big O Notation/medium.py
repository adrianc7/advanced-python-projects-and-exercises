'''''
Medium: (5 points)
2. Given an array of integers, write a function that finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.

Time Complexity: O(n log n)
Explanation: The np.unique function iterates through the array to identify unique elements, which takes O(n).
The np.sort function sorts the unique elements, which takes O(m log m), where m is the number of unique elements.
In the worst case, m can be equal to n, so the overall time complexity is O(n log n).
'''''

import numpy as np

# Generate an array of random integers between 0 and 10, size 10
array = np.random.randint(low=0, high=10, size=10)
print("Our array:", array)

def second_largest(array):
    unique_elements = np.unique(array)  # Remove duplicates
    if len(unique_elements) < 2:
        return None  # Handle case where there aren't enough unique elements
    sorted_elements = np.sort(unique_elements)  # Sort the unique elements
    return sorted_elements[-2]  # Return the second largest element

print('Second Largest Element in Our Array:', second_largest(array))

## Output:
# Second Largest Element in Our Array: 7