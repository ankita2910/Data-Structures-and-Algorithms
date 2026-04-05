def get_spiral_order(matrix):
    result = []
    # Make a copy if you don't want to destroy the original matrix
    temp_matrix = [list(row) for row in matrix]
    
    while temp_matrix:
        # 1. Get the first row
        result.extend(temp_matrix.pop(0))
        
        # 2. Get the last element of each remaining row (Right Column)
        if temp_matrix and temp_matrix[0]:
            for row in temp_matrix:
                result.append(row.pop())
        
        # 3. Get the last row in reverse (Bottom Row)
        if temp_matrix:
            result.extend(temp_matrix.pop()[::-1])
            
        # 4. Get the first element of each remaining row from bottom to top (Left Column)
        if temp_matrix and temp_matrix[0]:
            for row in reversed(temp_matrix):
                result.append(row.pop(0))
                
    return result

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = get_spiral_order(matrix)

print(f"Input:  matrix = {matrix}")
print(f"Output: {output}")
