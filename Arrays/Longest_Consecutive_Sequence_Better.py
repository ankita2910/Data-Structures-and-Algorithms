#Even this is optimal in worst case scenarios!

def longest_consecutive_sequence(arr):
    longest = 1
    CntCurr = 0
    lastSmaller = float('-inf')
    arr.sort()

    for i in range(len(arr)):
        if arr[i] == lastSmaller + 1:
            CntCurr += 1
            lastSmaller = arr[i]
        elif arr[i] != lastSmaller:
            # longest = max(longest, CntCurr)
            CntCurr = 1
            lastSmaller = arr[i]
        longest = max(longest, CntCurr)
    return longest
# Example usage:
arr = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(arr)
print(result)  # Output: 4 (the longest consecutive sequence is [1, 2, 3, 4])