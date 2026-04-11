
def generate_pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
# Example usage:
n = 5       
pascal_triangle = generate_pascal_triangle(n)
print(f"Input: n = {n}")
print("Output:")
for row in pascal_triangle:
    print(row)      
    