
#This is Dutch National Flag Algorithm. The idea is to maintain three pointers: low, mid, and high. 
# The low pointer is used to track the position of the first 1, the mid pointer is used to track the current element being processed, and the high pointer is used to track the position of the first 2. 
# We iterate through the array and swap elements based on their values (0s to the left, 1s in the middle, and 2s to the right) until we have processed all elements.
# The time complexity of this code is O(n) because we are iterating through the array once. The space complexity is O(1) because we are using only a constant amount of extra space for the pointers and temporary variables.

def sort_array_of_0s_1s_2s(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
# Example usage:
arr = [2, 0, 1, 2, 1, 0]
sorted_arr = sort_array_of_0s_1s_2s(arr)
print(sorted_arr)  # Output: [0, 0, 1, 1, 2, 2] 
