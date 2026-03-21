
#Kadan's algorithm is used to find the maximum sum of a contiguous subarray in an array of integers.
#  The algorithm works by iterating through the array and keeping track of the current sum of the subarray. 
# If the current sum becomes negative, it resets to zero, as a negative sum would not contribute to a maximum sum in future iterations. 
# The algorithm also keeps track of the maximum sum encountered during the iteration.
# The time complexity of this code is O(n) because we are iterating through the array once. 
# The space complexity is O(1) because we are using only a constant amount of extra space for the variables.
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    ansStart = 0
    ansEnd = 0
    start = 0

    for i in range(len(arr)):
        if current_sum == 0:
            start = i

        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            ansStart = start
            ansEnd = i

        if current_sum < 0:
            current_sum = 0

    return max_sum
# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = max_subarray_sum(arr)
print(result)  # Output: 6 (subarray [4,-1,2,1])    
