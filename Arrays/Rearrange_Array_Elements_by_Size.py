
#here we rearrgane positive and negative numbers in the array in alternative way.

def rearrange_array(arr):
    pos = []
    neg = []
    
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    
    result = []
    i, j = 0, 0
    
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    
    while i < len(pos):
        result.append(pos[i])
        i += 1
    
    while j < len(neg):
        result.append(neg[j])
        j += 1
    
    return result
# Example usage:
arr = [-1, -2, 3, -4, 5, -6]
result = rearrange_array(arr)
print(result)  # Output: [-1, 3, -2, -4, 5, -6] (or any other valid rearrangement)   