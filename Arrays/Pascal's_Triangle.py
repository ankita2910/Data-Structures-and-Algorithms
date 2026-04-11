
# Very important: always remeber the range here
# in generate function define row =[1] as the first row by default
# then append ans to the row list and return it one row every time
# in pascal_triangle function, keep range to print the traignel from 1 to n+1 as we are using 1 based indexing in generate function 
# look at Striver's code for 0 based indexing

def generate(n):
    ans = 1
    row = [1]
    for col in range(1, n):
        
        ans = ans * (n - col) // col
        row.append(ans)
    return row

def pascal_triangle(n):
    triangle = []
    for i in range(1, n + 1):
        triangle.append(generate(i))
    return triangle
# Example usage:
n = 5
pascal_triangle_result = pascal_triangle(n)
print(f"Input: n = {n}")
print("Output:")
for row in pascal_triangle_result:
    print(row)