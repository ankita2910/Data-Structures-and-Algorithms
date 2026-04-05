def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Move Right: Traverse top row from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Move Down: Traverse right column from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Move Left: Traverse bottom row from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        # Move Up: Traverse left column from bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Input: matrix = {matrix}")
print(f"Output: {spiral_order(matrix)}")
