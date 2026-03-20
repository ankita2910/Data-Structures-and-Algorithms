#This is two pointer approach.

def longest_subarray_with_sum_k(arr, k):
    left = 0
    right = 0
    current_sum = arr[0]
    max_len = 0
    n = len(arr)

    while right < n:
        # shrink window if sum > k
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1

        # check if sum == k
        if current_sum == k:
            max_len = max(max_len, right - left + 1)

        # expand window
        right += 1
        if right < n:
            current_sum += arr[right]

    return max_len
# Example usage:
arr = [1, 1, 5, 2, 3]
k = 3
result = longest_subarray_with_sum_k(arr, k)
print(result)  # Output: 2 (subarray [1, 1, 5, 2])    