

def count_subarrays_with_sum_k(arr, k):
    count = 0
    current_sum = 0
    sum_freq = {0: 1}  # {0:1} allows the algorithm to count subarrays whose sum equals k starting from index 0.

    for num in arr:
        current_sum += num

        if (current_sum - k) in sum_freq:
            count += sum_freq[current_sum - k]

        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
        # The .get() method avoids key errors by using get() to return 0 if current_sum is not already in sum_freq.
    return count
# Example usage:
arr = [1, 1, 1,2,3,1,2,3,1]
k = 2
result = count_subarrays_with_sum_k(arr, k)
print(result)  
