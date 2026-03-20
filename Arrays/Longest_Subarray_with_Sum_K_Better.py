#IT is contiguous subarray
#The time complexity of this code is O(n) because we are iterating through the array once and performing constant time operations for each element. 
# The space complexity is O(n) in the worst case, when all elements in the array are unique and we store all of their cumulative sums in the map.
#  However, in practice, the space complexity may be less than O(n) if there are duplicate sums, as we only store the first occurrence of each sum in the map.
def longest_subarray_with_sum_k(arr, k):
    sum_map = {}
    current_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum == k:
            max_length = i + 1
        
        if (current_sum - k) in sum_map:
            max_length = max(max_length, i - sum_map[current_sum - k])
        
        if current_sum not in sum_map:   #This is where the code handles negative numbers. We only store the first occurrence of each sum in the map, so if we encounter the same sum again, we won't update the map and we will still be able to find the correct subarray length when we encounter a negative number.
            sum_map[current_sum] = i
            
    return max_length
# Example usage:
arr = [1, -1, 5, -2, 3]
k = 3
result = longest_subarray_with_sum_k(arr, k)
print(result)  # Output: 4 (subarray [1, -1, 5, -2])