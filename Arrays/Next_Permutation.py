

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    left, right = i + 1, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
# Example usage:
arr = [1, 2, 3]
next_permutation(arr)
print(arr)  # Output: [1, 3, 2] (the next permutation of [1, 2, 3]) 
